import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['how are you?', ['I am doing well, thank you.', 'I am good, thanks for asking.']],
    ['what is your name?', ['My name is Chatbot.', 'You can call me Chatbot.']],
    ['bye|goodbye', ['Goodbye!', 'Bye!', 'See you later!']],
    ['what can you do?', ['I can have conversations with you!', 'I am here to chat with you.']],
    ['tell me a joke', ['Why was the math book sad? Because it had too many problems!']],
    ['tell me about yourself', ['I am a chatbot created to have conversations with users.', 'I am programmed to chat with you and respond to your queries.']],
    ['(.*)', ['Sorry, I did not understand that.', 'Can you please repeat?']]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Define a function to start the conversation
def start_chat():
    print("Welcome to the Chatbot! Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

# Start the conversation
start_chat()
