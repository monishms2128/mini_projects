import datetime
import random
print("=" * 45)
print("      MONISH AI CHATBOT ")
print("=" * 45)
print("Type 'exit' to close the chatbot\n")

while True:

    user_input = input("You : ").lower()
    
    # Greetings
    if user_input == "hi" or user_input == "hello":

        greetings = [
            "Hello! Nice to meet you ",
            "Hi there! How can I help you?",
            "Hey! Hope you're having a great day ",
            "Hello Monish! "
        ]

        print("Bot :", random.choice(greetings))

    # Asking about AI
    elif "ai" in user_input:
        print("Bot : AI stands for Artificial Intelligence.")

    # Motivation
    elif "motivate me" in user_input:
        print("Bot : Believe in yourself. Every expert was once a beginner 🚀")

    # Asking favorite language
    elif "favorite language" in user_input:
        print("Bot : Python is my favorite programming language.")

    # Asking location
    elif "where are you from" in user_input:
        print("Bot : I live inside your computer ")

    # Asking time
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Bot : Current time is", current_time)

    # Asking date
    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot : Today's date is", current_date)

    # Thank you response
    elif "thank you" in user_input or "thanks" in user_input:
        print("Bot : You're welcome ")

    # Asking creator
    elif "who created you" in user_input:
        print("Bot : I was created by Monish during CODSOFT Internship.")

    # Joke feature
    elif "joke" in user_input:
        print("Bot : Why do programmers hate nature? Too many bugs ")

    # Asking name
    elif "your name" in user_input:
        print("Bot : My name is Monish AI Bot.")

    # Asking how are you
    elif "how are you" in user_input:
        print("Bot : I am doing great! Thanks for asking.")

    # Asking about internship
    elif "internship" in user_input:
        print("Bot : This internship helps students improve AI skills.")

    # Asking skills
    elif "skills" in user_input:
        print("Bot : Python, AI, Machine Learning, Communication")

    # Exit
    elif user_input == "exit":
        print("Bot : Goodbye Monish! Have a productive day ")
        break

    # Unknown input
    else:
        print("Bot : Sorry, I don't understand that yet.")
