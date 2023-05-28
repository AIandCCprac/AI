
#Bakery Chatbot
from nltk.chat.util import Chat, reflections
pairs =[
	['(.*) your name', ['My name is Washington!']],
]


print("Hello. Welcome to Foodies Bakery! How can I help you? [Note: Please use lowercase letters to converse.]")
chat = Chat(pairs, reflections)
chat.converse()

