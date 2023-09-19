import gtts
from pydub import AudioSegment
from pydub.playback import play

# Função para falar e reproduzir o áudio
def speak_and_play(text):
    tts = gtts.gTTS(text, lang="pt-br")
    audio = AudioSegment.from_mp3(tts.get_urls()[0])
    play(audio)

# Mensagem 1
speak_and_play("Por favor mostre a etiqueta para identificação do destinatário")

# Mensagem 2
speak_and_play("Houve um erro na leitura da etiqueta, por favor tente novamente")

# Mensagem 3
speak_and_play("A etiqueta foi lida com sucesso, por favor coloque o objeto na caixa")
