import postmanidf as pmidf
import texttospeech as tts
import ticketidf as tidf

try: 
    pmidf.camera()
    print("Câmera inicializada com sucesso.")
    tts.cumprimentos()
    tentativas = 0
    """ while not tidf.camera() and tentativas < 4:
        tts.erro()
        tentativas += 1 """
    
    if tentativas == 4:
        tts.tentativasexcedidas()
    else:
        tts.sucesso()
except:
    print("Erro inesperado, o programa será reiniciado.")