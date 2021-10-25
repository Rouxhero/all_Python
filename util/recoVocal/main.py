from boot import *
from win32com.client import Dispatch



name = input('what is my name ?')	
test = boot(name)
print('{} is now running'.format(test.name))
data = ""
while data != "stop":
	data = test.detect()
	if data[0]:
		data = data[1]
		print(data)
		Dispatch("SAPI.SpVoice").Speak(data)
		data = test.listen()
		print(data[1])
		Dispatch("SAPI.SpVoice").Speak(data[1])
	else :
		data = data[1]
		Dispatch("SAPI.SpVoice").Speak(data)

