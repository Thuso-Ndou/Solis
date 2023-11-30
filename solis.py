import pyttsx3 as p
import speech_recognition as sr
import wikipedia as wp
import webbrowser as wb
import os
import smtplib
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
    speak("I am Solis ,And i will be your voice assistance. How may i help you?")
 
def takeCommand():
    # create an instance
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000 # take low sound
        r.adjust_for_ambient_noise(source,2.1) # listening to our voice
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
def sendEmail(to, content):
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.ehlo()
      server.starttls()
      server.login('myemail@gmail.com', 'mypassword')
      server.sendmail('myemail@gmail.com', to, content)
      server.close()
       
if __name__ == "__main__":
    greetMe()
    while True:
    #if 1:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wp.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            wb.open("youtube.com")
        elif 'who are you or what is your name' in query:
            speak("I am Solis personal AI assistance")
        elif 'open google' in query:
            wb.open("google.com")
        elif 'open chat gpt' in query:
            wb.open("chat.openai.com")
        elif 'play music' in query:
            music_dir = 'd:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            #codePath = ""
            os.startfile(Code.exe)
        elif 'send email' in query:
            try:
                speak("What should i send")
                content = takeCommand()
                to = "example@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
                
            except Exception as ex:
                print(ex)
                speak("I am unable to send the email")