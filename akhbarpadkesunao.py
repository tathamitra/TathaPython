import requests
import  json


def provide_headlines(item):
 # url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=64d99f86b3a74b6092238914e545a1a9'

 data = requests.get(
    'http://newsapi.org/v2/top-headlines?'
    'country=us&'
    'apiKey=64d99f86b3a74b6092238914e545a1a9'
)


 news=json.loads(data.text)
 return (news['articles'][item]['title'])


def speak(str):
 from win32com.client import Dispatch
 speak = Dispatch("SAPI.SpVoice")
 speak.Speak(str)


if __name__ == '__main__':
     # g = provide_headlines(0)
     print("Enter the number of headlines:")
     noumofheadlines = int(input())

     print( f"Top {noumofheadlines} news are :")
     for i in range(noumofheadlines):
        print(provide_headlines(i))
        speak(provide_headlines(i))