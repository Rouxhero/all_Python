import speech_recognition as sr  
from var import *


class boot :

	def __init__(self,name):
		self.name = name
		self.r  = sr.Recognizer()
		

	def __translate(self,audio):
		text = ""
		try:
		    text = [True,self.r.recognize_google(audio,language='fr-FR')]
		except sr.UnknownValueError:
		   text = [False,"L'audio n'as pas été compris"]
		except sr.RequestError as e:
		    text = [False,"Le service Google Speech API ne fonctionne plus" + format(e)]
		print(text)
		return text

	def __isMe(self,text):
		if text[0]:
			text = text[1]
			if text == 'stop':
				return [False,'stop']
			text = text.split(' ')
			print(text)
			if len(text)>1:
				for word in range(len(text)) :
					print(text[word])
					if text[word] in helloValue and word<len(text) :
						print(text[word+1])
						if text[word+1] == self.name:
							print('hey !')
							return [True," ".join(text[word+1:])]
				return [False,""]
			else :
				return [False,""]
		else :
			return [False,text]

	def listen(self):
		print("Dites quelque chose")
		audio = self.micro()
		return self.__translate(audio)

	def detect(self):
		audio = self.micro()
		data =  self.__isMe(self.__translate(audio))
		print(data)
		return data
	def micro(self):
		with sr.Microphone() as source:
			self.r.adjust_for_ambient_noise(source)
			audio =  self.r.listen(source)
		return audio