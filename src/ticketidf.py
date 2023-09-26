import pytesseract as tess
from PIL import Image
import re
import time
import cv2
import json

class EtiquetaProcessor:
    def __init__(self):
        self.image_path = "images/captured_image.jpg"
        self.camera_active = False  # Indica se a câmera está ativa

    def extrair_palavras_em_maiusculas(self, texto):
        palavras_em_maiusculas = re.findall(r'\b[A-Z]+\b', texto)
        linhas = texto.split('\n')
        
        for i, linha in enumerate(linhas):
            palavras = linha.split()
            palavras_em_maiusculas_linha = [palavra for palavra in palavras if palavra.isupper()]
            linhas[i] = ' '.join(palavras_em_maiusculas_linha)

        nova_string = '\n'.join(linhas)
        return nova_string

    def iniciar_camera(self):
        self.camera_active = True
        capture = cv2.VideoCapture(0)  # Abre a câmera padrão (0) - pode variar dependendo da câmera
        
        while self.camera_active:
            ret, frame = capture.read()  # Captura um quadro da câmera

            if ret:
                cv2.imshow("Camera", frame)  # Exibe a imagem da câmera em uma janela chamada "Camera"
                
                key = cv2.waitKey(1)  # Aguarda um pequeno intervalo de tempo (1 ms) e verifica se uma tecla foi pressionada
                
                if key == ord("q"):  # Se a tecla "q" for pressionada, encerra a câmera
                    self.camera_active = False
                elif key == ord(" "):  # Se a tecla de espaço for pressionada, tire a foto
                    cv2.imwrite(self.image_path, frame)  # Salva o quadro como uma imagem
                    self.camera_active = False
                
            else:
                print("Não foi possível capturar a imagem da webcam.")
                break

        capture.release()
        cv2.destroyAllWindows()  # Fecha todas as janelas abertas pelo OpenCV

    def processar_etiqueta(self):
        self.iniciar_camera()
        
        img = Image.open(self.image_path)
        text = tess.image_to_string(img)

        destNome = text[text.find("DESTINATARIO")+len("DESTINATARIO"):]
        destNome = self.extrair_palavras_em_maiusculas(destNome)
        destNome = destNome.strip()
        destNome = destNome[:destNome.find("\n")]

        dict = {
            "Nome": destNome,
            "Horario": time.strftime("%H:%M:%S"),
            "Data": time.strftime("%d/%m/%Y")
        }

        json_filename = f'logs/{destNome}_{time.strftime("%d-%m-%Y_%H-%M-%S")}.json'

        with open(json_filename, 'w') as json_file:
            json.dump(dict, json_file, indent=4, ensure_ascii=False)
        
        return json_filename

if __name__ == "__main__":
    etiqueta_processor = EtiquetaProcessor()
    json_filename = etiqueta_processor.processar_etiqueta()
    print(f'JSON criado: {json_filename}')
