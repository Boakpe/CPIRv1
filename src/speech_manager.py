import time
from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History

set_api_key("56662a0794b219b1d16af5d26028d65f")

def cumprimentos() -> None:
    periodo_do_dia = time.localtime().tm_hour
    if 6 <= periodo_do_dia < 12:
        periodo_do_dia = "Bom dia"
    elif 12 <= periodo_do_dia < 18:
        periodo_do_dia = "Boa tarde"
    else:
        periodo_do_dia = "Boa noite"
    mensagem = f"{periodo_do_dia}, por favor tire a foto da etiqueta para identificação do destinatário."
    audio = generate(
        text=mensagem,
        voice="Michael",
        model="eleven_multilingual_v2"
        )
    play(audio)

def erro() -> None:
    mensagem = "Houve um erro na leitura da etiqueta, por favor tente novamente."
    audio = generate(
        text=mensagem,
        voice="Michael",
        model="eleven_multilingual_v2"
        )
    play(audio)

def sucesso() -> None: 
    mensagem = "A etiqueta foi lida com sucesso, por favor coloque o objeto na caixa."
    audio = generate(
        text=mensagem,
        voice="Michael",
        model="eleven_multilingual_v2"
        )
    play(audio)

def tentativasexcedidas() -> None:
    mensagem = "O número de tentativas excedeu o limite, o programa será reiniciado. Espere um momento."
    audio = generate(
        text=mensagem,
        voice="Michael",
        model="eleven_multilingual_v2"
        )
    play(audio)