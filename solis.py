import pyttsx3 as p
import speech_recognition as sr
import datetime as dt

engine = p.init('espeak')

voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
#print(voices[9].id)
#print(rate)

engine.setProperty('voice', voices[9].id) # change voice name
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
    speak("I am Solis. How may i help you sir?")
 
def takeCommand():
    # create an instance
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Running...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("I don't understand")
        return "None"
    return query
        
if __name__ == "__main__":
    greetMe()
    while True:
        query = takeCommand().lower()