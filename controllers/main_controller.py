import sys
sys.path.append("..")   
from views import camera_manager as cm
from views import speech_manager as sm
from views import label_processor as lp

def run():
    try: 
        cm.camera()
        print("Câmera inicializada com sucesso.")
        etiqueta_processor = lp.LabelProcessor()
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