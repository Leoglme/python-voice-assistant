import os
import time
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS


class voiceAssistant:
    def __init__(self):
        pass

    def speak(self, text):
        tts = gTTS(text, lang="fr")
        filename = "Typing.mp3"
        tts.save(filename)
        playsound(filename)

    def get_audio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio, language="fr-FR")
                print(said)
            except Exception as e:
                print("Exception: " + str(e))

        return said
