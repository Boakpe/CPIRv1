import camera_manager as cm
import speech_manager as sm
from label_processor import LabelProcessor as lp

try: 
    cm.camera()
    print("Câmera inicializada com sucesso.")
    etiqueta_processor = lp()
    sm.cumprimentos()
    tentativas = 0
    while etiqueta_processor.processar_etiqueta() is None and tentativas < 4:
        sm.erro()
        tentativas += 1
    
    if tentativas == 4:
        sm.tentativasexcedidas()
    else:
        sm.sucesso()
except Exception as e:
    print("Erro inesperado, o programa será reiniciado.")
    print(e)