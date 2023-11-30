import pyttsx3 as p
#import speechRecognition as sr
import datetime as dt

engine = p.init('espeak')

voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
#print(voices[16].id)
#print(rate)

engine.setProperty('voice', voices[29].id) # change voice name
engine.setProperty('rate', 180) # set the speech speed

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greetMe():
    hour = int(dt.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good Morning!")
    elif(hour >= 12 and hour < 18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Solis. How may i help you Thuso?")
 
def takeCommand():
    speak("")
        
if __name__ == "__main__":
    greetMe()