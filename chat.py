import nltk
from nltk.chat.util import Chat, reflections

# Define some reflections to handle pronouns
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}

# Define some patterns and responses for the chatbot
pairs = [
    [
        r"hey",
        ["Hello ! How can I help you today?"]
    ],

[
        r"hello",
        ["yes! how can i help you."]
    ],

    [
        r"hru",
        ["I'm doing great, thanks for asking! How about you? 😊,." ]
    ],

    [
        r"what is your name",
        ["I am a chatbot.",]
    ],
    [
        r"how are you",
        ["I'm good, thank you! How can I assist you?"]
    ],
    [
        r"your name",
        ["I am a chatbot."]
    ],
    [
        r"what can you do",
        ["I can answer basic questions and engage in simple conversations."]
    ],
[
        r"who made you",
        ["developer Alok."]
    ],

    [
        r"who is prime minister of india",
        ["Narendra modi."]
    ],

    [
        r"who i am",
        ["i dont't know your name, but you are a good man"]
    ],


    [
        r"by",
        ["bye! Have a great day."]
    ],

    [
        r"quit",
        ["Goodbye! Have a great day."]
    ],
    [
        r"",
        ["I'm sorry, i don't have any batabase about your question"]
    ],

]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Run the chatbot
print("Hello! I'm a simple chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)

    # Break the loop if the user types 'quit'
    if user_input.lower() == 'quit':
        break