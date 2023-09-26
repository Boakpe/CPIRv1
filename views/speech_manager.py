import time
from elevenlabs import generate, play, set_api_key

set_api_key("56662a0794b219b1d16af5d26028d65f")

def periodo_do_dia(flag_artigo) -> str:
    periodo_do_dia = time.localtime().tm_hour
    if 6 <= periodo_do_dia < 12:
        periodo_do_dia = "Bom dia"
        if flag_artigo == True:
            periodo_do_dia = "um bom dia"
    elif 12 <= periodo_do_dia < 18:
        periodo_do_dia = "Boa tarde"
        if flag_artigo == True:
            periodo_do_dia = "uma boa tarde"
    else:
        periodo_do_dia = "Boa noite"
        if flag_artigo == True:
            periodo_do_dia = "uma boa noite"
    return periodo_do_dia
    
    

def cumprimentos() -> None:
    
    mensagem = f"{periodo_do_dia(False)}, por favor tire a foto da etiqueta para identificação do destinatário."
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
    mensagem = f"A etiqueta foi lida com sucesso, por favor coloque o objeto na caixa e tenha {periodo_do_dia(True)}."
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