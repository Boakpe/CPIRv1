import postmanidf as pmidf
import texttospeech as tts
import ticketidf as tidf

while True:
    try: 
        pmidf.camera()
        tts.cumprimentos()
        while not tidf.camera:
            tts.erro()
            # Se passar de 4 tentativas de leitura da etiqueta, o programa é encerrado
            # É salvo um arquivo .json com a data e hora da última tentativa
        tts.sucesso()
        # É salvo um arquivo .json com a data e hora e o nome do destinatário
        break
    except:
        pass