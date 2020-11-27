import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

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

    speak('Hi Sir, I am Jarvis. How May I help You')


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

  elif 'open google' in query:
    webbrowser.open('google.com')

  elif 'open stackoverflow' in query:
   webbrowser.open('stackoverflow.com')

  elif 'play music' in query:
    music_dir = 'C:\\casual\\songs'
    songs=os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir,songs[0]))
  elif 'time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S")
      speak(f"the time is {strTime}")
  elif 'open code' in query:
      path= "C:\\Program Files\\Microsoft VS Code\\Code.exe"
      os.startfile(path)
  elif 'email to harry' in query:
      try:
          speak("what should i say?")
          content = takecommand()
          to = "tarit2014@gmail.com"
          sendmail(to,content)
          speak("Email has been sent")
      except Exception as e:
          print(e)
          print("sorry i am unable to send this email")



'''
mport win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'To address'
mail.Subject = 'Message subject'
mail.Body = 'Message body'
mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

# To attach a file to the email (optional):
attachment  = "Path to the attachment"
mail.Attachments.Add(attachment)

mail.Send()
'''