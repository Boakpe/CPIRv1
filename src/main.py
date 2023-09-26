import postmanidf as pmidf
import texttospeech as tts
import ticketidf as tidf
import aguardar_botao from interaction

try: 
    pmidf.camera()
    print("Câmera inicializada com sucesso.")
    tts.cumprimentos()
    tentativas = 0
    tidf.imagem_capturada_global = 0

    while tidf.imagem_capturada_global = 0 and tentativas < 4:
        tidf.imagem_capturada_global = aguardar_botao()
        if tidf.imagem_capturada_global = 0:
            tts.erro()
            tentativas += 1

    if tentativas == 4:
        tts.tentativasexcedidas()
    else:
        tts.sucesso()
        tidf.processar_etiqueta()
except:
    print("Erro inesperado, o programa será reiniciado.")