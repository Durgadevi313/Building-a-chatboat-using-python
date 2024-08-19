import tkinter as tk
from nltk.chat.util import Chat, reflections

# Define the pairs for the chatbot responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you ?",
        ["I'm doing good, how about you?", "I'm fine, thank you!"]
    ],
    [
        r"what is your name ?",
        ["My name is ChatBot.", "I'm called ChatBot."]
    ],
    [
        r"quit",
        ["Bye-bye!", "It was nice talking to you!"]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that.", "Can you please rephrase?"]
    ]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Function to handle sending messages
def send_message():
    user_input = entry_box.get()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    chat_log.config(state=tk.DISABLED)

    response = chatbot.respond(user_input)
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "Bot: " + response + "\n\n")
    chat_log.config(state=tk.DISABLED)

    entry_box.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("ChatBot")

# Create and place the chat log
chat_log = tk.Text(root, bd=1, bg="white", height="8", width="50", font="Arial")
chat_log.config(state=tk.DISABLED)
chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create and place the entry box
entry_box = tk.Entry(root, bd=1, bg="white", width="29", font="Arial")
entry_box.grid(row=1, column=0, padx=10, pady=10)

# Create and place the send button
send_button = tk.Button(root, text="Send", width="12", height=5, bd=1, bg="lightblue", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Run the main event loop
root.mainloop()
