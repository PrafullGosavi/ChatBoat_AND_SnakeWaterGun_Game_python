import random

# Define a dictionary of responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thanks!", "I'm fine, thank you!", "I'm great, how about you?"],
    "what's your name": ["My name is Chatbot!", "I'm Chatbot, nice to meet you!"],
    "bye": ["Goodbye!", "Bye-bye!", "See you later!"]
}

# Define a function to handle user input
def respond(message):
    if message in responses:
        return random.choice(responses[message])
    else:
        return "I'm sorry, I don't understand what you're saying."

#Define a main function to run the chatbot
def main():
    print("Hello, I'm a chatbot. Ask me anything!")
    while True:
        message = input("You: ")
        if message.lower() == "exit":
            break
        else:
            print("Chatbot:", respond(message.lower()))

if __name__ == "__main__":
    main()
