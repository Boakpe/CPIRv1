import gtts
from playsound import playsound

tts = gtts.gTTS("Por favor mostre a etiqueta para identificação do destinátario", lang="pt-br")
tts.save("audios/cumprimentos.mp3")
playsound("audios/cumprimentos.mp3")

tts = gtts.gTTS("Houve um erro na leitura da etiqueta, por favor tente novamente", lang="pt-br")
tts.save("audios/erro.mp3")
playsound("audios/erro.mp3")

tts = gtts.gTTS("A etiqueta foi lida com sucesso, por favor coloque o objeto na caixa", lang="pt-br")
tts.save("audios/sucesso.mp3")
playsound("audios/sucesso.mp3")