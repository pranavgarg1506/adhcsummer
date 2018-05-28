#!/usr/bin/env python3

import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser as wb

r=sr.Recognizer()

with sr.Microphone() as  source:
	r.adjust_for_ambient_noise(source)
	print('What do u want to do? ')
	audio=r.listen(source)

try:
	speak=r.recognize_google(audio)
	print("You said: " + speak)
	#os.system(speak)
	striped = data.strip()
	new_data = striped.split()
	print(new_data)
	
	



except:
	print("Could Not Understand!!")
	pass
