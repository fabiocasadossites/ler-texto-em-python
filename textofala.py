from gtts import gTTS

texto = "Clica agora no botão de like e deixa seu comentário"
lingua = "pt"

tts = gTTS(texto, lang=lingua)
tts.save("audio.mp3")

import os
os.system('ffplay -autoexit -nodisp audio.mp3')