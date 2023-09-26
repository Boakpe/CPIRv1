import postmanidf as pmidf
import texttospeech as tts
from ticketidf import EtiquetaProcessor

try: 
    pmidf.camera()
    print("Câmera inicializada com sucesso.")
    etiqueta_processor = EtiquetaProcessor()
    tts.cumprimentos()
    tentativas = 0
    while etiqueta_processor.processar_etiqueta() is None and tentativas < 4:
        tts.erro()
        tentativas += 1
    
    if tentativas == 4:
        tts.tentativasexcedidas()
    else:
        tts.sucesso()
except:
    print("Erro inesperado, o programa será reiniciado.")