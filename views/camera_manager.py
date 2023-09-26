from keras.models import load_model
import cv2
import numpy as np

def camera():
    # Desativa a notação científica para maior clareza
    np.set_printoptions(suppress=True)

    # Carrega o modelo
    model = load_model("models/keras_model.h5", compile=False)

    # Carrega os rótulos (labels)
    class_names = open("models/labels.txt", "r").readlines()

    # A CAMERA pode ser 0 ou 1, dependendo da câmera padrão do seu computador
    camera = cv2.VideoCapture(0)

    carteiro_index = 0
    while True:
        # Captura a imagem da webcam
        ret, image = camera.read()

        # Redimensiona a imagem bruta para (224-altura, 224-largura) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        # Mostra a imagem em uma janela
        cv2.imshow("Imagem da Webcam", image)

        # Converte a imagem em um array numpy e a remodela para o formato de entrada do modelo
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normaliza o array de imagem
        image = (image / 127.5) - 1

        # Faz a previsão com o modelo
        prediction = model.predict(image)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Imprime a classe prevista e a pontuação de confiança
        print("Classe:", class_name[2:], end="")
        print("Pontuação de Confiança:", str(np.round(confidence_score * 100))[:-2], "%")

        if class_name[2:].strip() == "Carteiro":
            carteiro_index += 1
        else:
            carteiro_index = 0

        if carteiro_index == 10:
            print("Carteiro detectado!")
            return True

        # Aguarda a entrada do teclado
        keyboard_input = cv2.waitKey(200)

        # 27 é o código ASCII para a tecla Esc no seu teclado
        if keyboard_input == 27:
            break

    camera.release()
    cv2.destroyAllWindows()
