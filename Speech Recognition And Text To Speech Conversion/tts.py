import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+0)
engine.say('The  quick   brown   fox  jumped   over   the   lazy   dog.')
engine.runAndWait()

##pip install pyttsx3
