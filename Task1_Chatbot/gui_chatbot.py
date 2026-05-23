import tkinter as tk
import random
import datetime

# Create window
window = tk.Tk()
window.title("MONISH AI CHATBOT")
window.geometry("500x600")
window.configure(bg="#1e1e1e")

# Chat display area
chat_area = tk.Text(
    window,
    font=("Arial", 12),
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# User input box
user_input = tk.Entry(
    window,
    font=("Arial", 14),
    bg="#3c3f41",
    fg="white",
    insertbackground="white"
)
user_input.pack(padx=10, pady=10, fill=tk.X)

# Bot response function
def chatbot_response():

    user_text = user_input.get().lower()

    chat_area.insert(tk.END, "You : " + user_text + "\n")

    # Greeting responses
    if user_text == "hi" or user_text == "hello":

        greetings = [
            "Hello! Nice to meet you 😊",
            "Hi there! How can I help you?",
            "Hey! Hope you're having a great day 🚀"
        ]

        response = random.choice(greetings)

    elif "how are you" in user_text:
        response = "I am doing great 😊"

    elif "your name" in user_text:
        response = "My name is Monish AI Bot."

    elif "time" in user_text:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = "Current time is " + current_time

    elif "date" in user_text:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        response = "Today's date is " + current_date

    elif "joke" in user_text:

        jokes = [
            "Why do programmers hate nature? Too many bugs 😂",
            "Why was Python so popular? Because it had great features 😄"
        ]

        response = random.choice(jokes)

    elif "ai" in user_text:
        response = "AI means Artificial Intelligence."

    elif "motivate me" in user_text:
        response = "Believe in yourself 🚀"

    elif "bye" in user_text:
        response = "Goodbye! Have a productive day 😊"

    else:
        response = "Sorry, I don't understand that yet."

    # Display bot response
    chat_area.insert(tk.END, "Bot : " + response + "\n\n")

    # Clear input box
    user_input.delete(0, tk.END)

# Send button
send_button = tk.Button(
    window,
    text="Send",
    font=("Arial", 12),
    bg="#007acc",
    fg="white",
    command=chatbot_response
)

send_button.pack(pady=10)
# Enter key support
window.bind('<Return>', lambda event: chatbot_response())

# Run window
window.mainloop()