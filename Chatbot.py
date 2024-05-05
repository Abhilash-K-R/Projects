#Training a Chat Bot model
# importing necessary modules
import random
from nltk.chat.util import Chat,reflections

#Define Patterns and responses for Chatbot...
patterns=[
    (r'hi|hello|hii|hai',['hello there!..','Hay there wahat can i do for you..','hello','hii how can i assist you']),
    (r'who are you|tell me about you|you?',['I am a chat bot created by SIET students',
                                            'I will  give some info try.. to type something','I can give any kind of information...']),
    (r'what is python?|python?|tell me about python',
     ['python is an open source PL','it is a general purpose Programming Language','it is dynamic,interpreted, ang high level language']),
     (r'kohli?|who is kohli?|tell about virat',['click here: https://en.wikipedia.org/wiki/Virat_Kohli']),
    (r'show dhoni image|ms dhoni pic',['click here: https://wallpapercave.com/ms-dhoni-full-screen-wallpapers']),
    (r'good afternoon in kannada',['ಶುಭ ಅಪರಾಹ್ನ']),
    (r'ironman|show ironman|show a video of ironman',['click here: https://www.youtube.com/watch?v=naSe2x0-VUw']),
    (r'(.*)',['I\'m unable to understand..','please rephrase that..','sorry.. i didn\'t understand' ])
    ]

#Train the model with patterns and reflections
chatbot=Chat(patterns,reflections)

# create a function to interact with chatbot
def chat():
  print('Welcome to chatbot..type quit to exit....')
  while True:
    user_input=input('You: ')
    if user_input.lower()=='quit':
      print('Good Bye....')
      break
    else:
      response= chatbot.respond(user_input)
      print('ChatBot: ',response)

chat()
