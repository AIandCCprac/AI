import nltk
from nltk.chat.util import Chat,reflections
pairs=[
    [r"(.*)are you",["hello %1 i am jayesh chatbot how can i help you"]]
    [r"show me dress",["yes here are options"]]

]
chat=Chat(pairs,reflections)
chat.converse()