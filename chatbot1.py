import re
import datetime

print("AI Chatbot started. Type 'exit' to quit.")

while True:
    user_input = input("You: ").lower()
    if re.search(r"\b(hi|hello|hey)\b", user_input):
        print("Chatbot: Hello! ")

    elif re.search(r"\bhow are you\b", user_input):
        print("Chatbot: I am functioning perfectly!")

    elif re.search(r"\byour name\b", user_input):
        print("Chatbot: I am an AI Rule-Based Chatbot.")

    elif re.search(r"\bnice to meet you\b", user_input):
        print("Chatbot: Nice to meet you too! ")

    elif re.search(r"\bthank you\b", user_input):
        print("Chatbot: your are welcome ! ")


    elif re.search(r"\b(today's date|current date|what is the date)\b", user_input):
        today = datetime.date.today()
        print("Chatbot: Today's date is", today)
    
    elif re.search(r"\b(current time|what is the time|time now)\b", user_input):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Chatbot: The current time is", current_time)


    elif user_input in ["exit", "bye"]:
        print("Chatbot: Goodbye! 👋")
        break
    else:
        print("Chatbot: I don't understand that -_-.")
        