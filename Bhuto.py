import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import win32com.client as win32
import random
from googlesearch import search
import requests
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

dict1 = {"manager":"sourav.das@hyland.com",
         "kaka":"shubhenu.ganguly@hyland.com",
         "tatha": "tathagata.mitra@hyland.com",
         "partha": "partha.basak@hyland.com",
         "pitamaha": "debabrata.mandal@hyland.com"}
dict2 = {"one":"1","two":"2","three":"3"}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')

    speak('Hi Sir, I am Bhuto. How May I help You')

def provide_headlines(item):
  data = requests.get(
    'http://newsapi.org/v2/top-headlines?'
    'country=in&'
    'apiKey=64d99f86b3a74b6092238914e545a1a9'
  )
  news=json.loads(data.text)
  return (news['articles'][item]['title'])

def takecommand():
    '''
    It takes microphone input from user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try :
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
       print(e)
       print('say that again')
       return  "None"
    return  query


def sendmail(to,subject,body):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = dict1.get(to)

    mail.Subject = subject
    mail.Body = body
    mail.Display()




if __name__ == '__main__':

 wishme()
 while True:
  query = takecommand().lower()
 #logic executing task based on query
  if 'wikipedia' in query:
       speak('searching wikipedia.....')
       query=query.replace('wikipedia',"")
       results=wikipedia.summary(query,sentences=2)
       speak('According to wikipedia')
       print(results)
       speak(results)

  elif 'open youtube' in query:
      webbrowser.open('youtube.com')

  elif 'notepad' in query:
      os.system("notepad filename.txt")

  elif 'google' in query:
      speak('searching google.....')
      query = query.replace('google', "")
      speak(f'The top 3 links for {query} search are .....')
      for j in search(query, tld="co.in", num=3, stop=3, pause=2):
          speak(j)
          print(j)

  elif 'open stackoverflow' in query:
   webbrowser.open('stackoverflow.com')

  elif 'play music' in query:
    music_dir = 'C:\\casual\\songs'
    songs=os.listdir(music_dir)
    randint=random.randint(0,3)
    print(songs)
    os.startfile(os.path.join(music_dir,songs[randint]))

  elif 'time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S")
      speak(f"the time is {strTime}")
  elif 'open code' in query:
      path= "C:\\Program Files\\Microsoft VS Code\\Code.exe"
      os.startfile(path)
  elif 'email' in query:
      try:

          speak("whom to mail? ")
          To = takecommand().lower()
          speak("what should be the subject of mail ")
          Subject = takecommand()

          speak("what should the mail say")
          Body = takecommand()

          sendmail(To,Subject,Body)

      except Exception as e:
          print(e)
          print("sorry i am unable to send this email")


  elif 'news' in query:

      try:
          speak("Top 3 headlines")
          noOfHeadlines= takecommand()
          for i in range(3):
              print(provide_headlines(i))
              speak(provide_headlines(i))

      except Exception as e:
          print(e)
          print("Sorry this service is down at the moment")
