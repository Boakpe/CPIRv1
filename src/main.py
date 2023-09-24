import postmanidf as pmidf
import texttospeech as tts
import ticketidf as tidf

try: 
    pmidf.camera()
    print("Câmera inicializada com sucesso.")
    tts.cumprimentos()
    tentativas = 0
    imagem_processada = 0

    while imagem_processada = 0 and tentativas < 4:
        imagem_processada = tidf.capturar_imagem_webcam
        if imagem_processada = 0:
            tts.erro()
            tentativas += 1

    if tentativas == 4:
        tts.tentativasexcedidas()
    else:
        tts.sucesso()
except:
    print("Erro inesperado, o programa será reiniciado.")