from gtts import gTTS
file=open("moon.txt","r").read()
language="en"
speech=gTTS(text=str(file),lang=language,slow = False)
speech.save("audio.mp3")