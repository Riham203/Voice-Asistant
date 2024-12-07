import speech_recognition as spr
import pyttsx3 
import datetime
import webbrowser
import time

def listen():
    r=spr.Recognizer()
    with spr.Microphone() as src:
        voice("I'm listening")
        print("I'm listening")
        rec=r.listen(src)
        try:
            txt= r.recognize_google(rec)
            print("You said:", txt)
            return txt
        except spr.UnknownValueError:
            print("sorry, i can't hearyou ")
            voice("sorry, i can't hear you ")
            return None
        except spr.RequestError as e:
            print("Error in google speech recognition service")
            voice("Error in google speech recognition service")
            return None 

def voice(txt):
    eng=pyttsx3.init()
    eng.say(txt)
    eng.runAndWait()

def ans(txt):

    if "hello" in txt:
        print("hello, how can i help you?")
        voice("hello, how can i help you?")

    elif "time" in txt:
        cur=time.strftime("%H:%M")
        voice(f"the time is {cur}")
        print(f"the time is {cur}")

    elif "date" in txt:
        day=datetime.date.today()
        voice(f"the today's date is {day.strftime('%B %d, %Y')}")
        print(f"the today's date is {day.strftime('%B %d, %Y')}")

    elif "search" in txt:
        search=txt.split("search")[-1].strip()
        url = f"https://www.google.com/search?q={search}"
        webbrowser.open(url)
        voice(f"Search for {search}")
        print(f"searching for {search}")

    elif "exit" in txt:
        print("exiting...")
        voice("exiting")
        quit()

    elif "bye" in txt:
        voice("ok bye bye, take care and have a nice day")
        print("ok bye bye, take care and have a nice day")
        quit()

    else:
        print("I didn't understand. Please try again")
        voice("I didn't understand. Please try again.")

while True:
    text=listen()
    
    if text:
        ans(text)
        time.sleep(5)