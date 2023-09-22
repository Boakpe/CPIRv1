from keras.models import load_model
import cv2
import pytesseract
import numpy as np

def camera():
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("model/keras_model.h5", compile=False)

    # Load the labels
    class_names = open("model/labels.txt", "r").readlines()

    # CAMERA can be 0 or 1 based on default camera of your computer
    camera = cv2.VideoCapture(0)

    carteiro_index = 0
    flagCarteiro = False
    while True:
        # Grab the webcamera's image.
        ret, image = camera.read()

        # Resize the raw image into (224-height,224-width) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        # Show the image in a window
        cv2.imshow("Webcam Image", image)

        # Make the image a numpy array and reshape it to the models input shape.
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1
        
        if flagCarteiro:     
            text = pytesseract.image_to_string(image)
            print(text)

        else:
            # Predicts the model
            prediction = model.predict(image)
            index = np.argmax(prediction)
            class_name = class_names[index]
            confidence_score = prediction[0][index]

            # Print prediction and confidence score
            print("Class:", class_name[2:], end="")
            print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

            # Print prediction and confidence score
            print("Class:", class_name[2:], end="")
            print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

            if class_name[2:].strip() == "Carteiro":
                carteiro_index += 1
            else:
                carteiro_index = 0

            if carteiro_index == 10:
                print("Carteiro detectado!")
                flagCarteiro = True
                #return True

            # Listen to the keyboard for presses.
            keyboard_input = cv2.waitKey(200)

            # 27 is the ASCII for the esc key on your keyboard.
            if keyboard_input == 27:
                break  

    camera.release()
    cv2.destroyAllWindows()