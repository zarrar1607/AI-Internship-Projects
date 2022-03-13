import speech_recognition as sr
import pyttsx3
import webbrowser
def main():
 
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate+0)
        engine.say('How can I help you')
        engine.runAndWait()
 
        print("Please say something")

 
        audio = r.listen(source)
       
 
        print("Recognizing Now .... ")
        
 
 
        # recognize speech using google
 
        try:
            print("You have said \n" + r.recognize_google(audio))
##            print("Audio Recorded Successfully \n ")
            if r.recognize_google(audio)=='hello':
##                print('hi')
                engine.say('Hello')
                engine.runAndWait()
            if r.recognize_google(audio)=='how are you':
##                print('hi')
                engine.say('I am fine and how are you ?')
                engine.runAndWait()
            if r.recognize_google(audio)=='pantech':
##                print('hi')
                engine.say('opening')
                engine.runAndWait()
                webbrowser.open('https://www.pantechelearning.com/', new=2)
 
 
        except Exception as e:
            print("Error :  " + str(e))
 
 
 
 
        # write audio
 
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
        print("Recorded successfully")
 
 
if __name__ == "__main__":
    main()
