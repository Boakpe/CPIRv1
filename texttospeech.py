import gtts
from playsound import playsound
import time

def cumprimentos():
    periodo_do_dia = time.localtime().tm_hour
    if periodo_do_dia >= 6 and periodo_do_dia < 12:
        periodo_do_dia = "Bom dia, "
    elif periodo_do_dia >= 12 and periodo_do_dia < 18:
        periodo_do_dia = "Boa tarde, "
    elif periodo_do_dia >= 18 and periodo_do_dia < 24:
        periodo_do_dia = "Boa noite, "
    cumprimentos = periodo_do_dia + "por favor mostre a etiqueta para identificação do destinátario"
    tts = gtts.gTTS(cumprimentos, lang="pt-br")
    tts.save("audios/cumprimentos.mp3")
    playsound("audios/cumprimentos.mp3")

def erro():
    tts = gtts.gTTS("Houve um erro na leitura da etiqueta, por favor tente novamente", lang="pt-br")
    tts.save("audios/erro.mp3")
    playsound("audios/erro.mp3")

def sucesso():
    tts = gtts.gTTS("A etiqueta foi lida com sucesso, por favor coloque o objeto na caixa", lang="pt-br")
    tts.save("audios/sucesso.mp3")
    playsound("audios/sucesso.mp3")