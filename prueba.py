import pyttsx3
import speech_recognition as sr

from difflib import SequenceMatcher as SM
import random
import time



recognizer = sr.Recognizer()

microphone = sr.Microphone(device_index = 0)
palabra=""
eng = pyttsx3.init()
def recognizerMicAudio():
	
	print("Escuchando...")
	with microphone as source:
		audio = recognizer.listen(source)
		palabra = recognizer.recognize_google(audio, language="es-ES")

	return palabra
while palabra != "chao":
	palabra = recognizerMicAudio()
	print(palabra)		
	if palabra == "Hola":
		
		
		eng.say("hola luciano, estoy lista")
		eng.runAndWait()
eng.say("chau luciano; que tenga buen dia")
eng.runAndWait()

eng.setProperty("rate",140)

eng.setProperty("volume",1.0)

listVoices = eng.getProperty("voices")
eng.setProperty("voices",listVoices[1].id)


