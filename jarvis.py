import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import cv2
from requests import get
import pywhatkit
import smtplib
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("\nGood Morning Faizan")
        speak("Good Morning Faizan")
        strTime = datetime.datetime.now().strftime('%I:%M %p')
        print(f"The time is : {strTime}")
        speak(f"the time is {strTime}")

    elif hour>=12 and hour<18:
            print("\nGood Afternoon Faizan")
            speak("Good Afternoon Faizan")
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            print(f"The time is : {strTime}")
            speak(f"the time is {strTime}")
    
    else:
        print("\nGood Evening Faizan")
        speak("Good Evening Faizan")
        strTime = datetime.datetime.now().strftime('%I:%M %p')
        print(f"The time is : {strTime}")
        speak(f"the time is {strTime}")
    print("I am Jarvis. Please tell me how may I help you")
    speak("I am Jarvis. Please tell me how may I help you")
    

def takeCommand():
#it takes microphone input from user and return string

    r = sr.Recognizer()

    with sr.Microphone() as source:
       print("\nListening...")
       r.pause_threshold = 1
       audio = r.listen(source)
       
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : { query}\n")

    except Exception as e:
        #print(e)
        print("say that again please...")
        speak("say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('faizanthehellboy@gmail.com', 'vamyzmnfwskirmlb')
    server.sendmail('faizanthehellboy@gmail.com', to,content)
    server.close()
    
    

if __name__ == "__main__":
    
    wishMe()
    while True:
        query = takeCommand().lower()
        
        
        #wikipedia search
        if 'wikipedia'in query:
           speak("searching Wikipedia...")
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query,sentences=2) 
           speak("According to Wikipedia")
           print(results)
           speak(results)
        #end
           
        #daily use apps
        elif 'command prompt' in query:
            os.system("start cmd")
           
        elif "teams" in query:
            tpath = "C:\\Users\\faiza\\Desktop\\Microsoft Teams (work or school)" 
            os.startfile(tpath)
            
            
        elif "vs code" in query:
            vpath = "C:\\Users\\faiza\\Desktop\\Visual Studio Code"
            os.startfile(vpath)
        #end
        
        #camera
        elif 'camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()  
        #end
        
        
        #play music
        elif 'play music' in query:
            music_dir = 'C:\\Faizan programs\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))
        #end
        
        #ipaddress
        elif 'ip' in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"your IP adress is {ip}")
        #end
        
            
        #google
        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        #end
        
        #amizone
        elif 'open zone' in query:
            webbrowser.open("s.amizone.net")
        #end
        
        #send message to someone
        elif 'message' in query:
            pywhatkit.sendwhatmsg("+919967864057","hello gohar this is jarvis ", 21,55)

        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        #end
        
        #song on youtube
        elif 'play' in query:
            speak("sir, which song would uh like to hear ?")
            y = takeCommand().lower()
            pywhatkit.playonyt(f"{y}")
        #end
        
        #search on youtube
        elif 'open youtube' in query:
            speak("sir, what woud you like to search on youtube?")
            t = takeCommand().lower()
            pywhatkit.playonyt(f"{t}")
        #end
        
        #email
        elif "send email to" in query:
            try:
                speak("what should i say?")
                content = takeCommand().lower()
                to = "shupaw007@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("message not sent")
        #end
        
        #to close applications
        elif "close" in query:
            speak("okay sir, closing command prompt")
            os.system("TASKKILL /F /IM cmd.exe")
        #end
            
        #to find joke
        elif "joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        #end
        
        #time
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            print(strTime)
            speak(f"Sir, the time is {strTime}")
        #end
        
        #general replies
        elif 'name' in query:
            print("my name is jarvis")
            speak("my name is jarvis")
        
        elif 'single' in query:
            print("no sir , i am in relationship with wifi")
            speak("no sir , i am in relationship with wifi")
        #end
            

        




