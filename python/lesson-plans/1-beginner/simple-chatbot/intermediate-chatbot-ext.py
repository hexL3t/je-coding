# Extension: This chatbot logs conversations to a text file
# and gives different greetings based on the time of day

import datetime  # Import the datetime module to check current time

# Function to return a greeting based on the time of day
def get_time_greeting():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning! ☀️"
    elif current_hour < 18:
        return "Good afternoon! 🌤"
    else:
        return "Good evening! 🌙"

# Function to log chat messages to a text file
def log_conversation(entry):
    with open("chat_log.txt", "a") as log_file:  # Open file in append mode
        log_file.write(entry + "\n")

# This function returns appropriate responses to user input
def get_response(user_input, name):
    responses = {
        'how are you': "I'm doing great, thanks for asking! 😊",
        'weather': "I can't check the weather right now, but I hope it's lovely where you are! ☀️",
        'joke': "Why did the math book look sad? Because it had too many problems! 😂",
        'hobby': "I love chatting with humans like you! 💬",
    }

    # Search for a keyword that matches the user's input
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]

    # Personalize response if name is mentioned
    if 'name' in user_input:
        return f"My name is Chatbot! What's yours?" if name == "" else f"Nice to chat with you, {name}! 😊"

    # Default message if nothing matches
    return "I'm still learning new things. Thanks for your patience! 😅"

# Main chatbot function that runs the conversation
def intermediate_chatbot():
    print("Hello! I'm your improved chatbot 🤖. Type 'bye' to end the chat.")
    
    # Show and log a time-based greeting
    greeting = get_time_greeting()
    print("Chatbot:", greeting)
    log_conversation("Chatbot: " + greeting)
    
    name = ""  # Placeholder for user's name

    while True:
        # Get and store the user input
        user_input = input("You: ").lower()
        log_conversation("User: " + user_input)

        if user_input == 'bye':
            goodbye = "Goodbye! 👋 Have a nice day!"
            print("Chatbot:", goodbye)
            log_conversation("Chatbot: " + goodbye)
            break

        # If user provides their name
        elif "my name is" in user_input:
            name = user_input.replace("my name is", "").strip().capitalize()
            response = f"Nice to meet you, {name}! 😄"
            print("Chatbot:", response)
            log_conversation("Chatbot: " + response)
        
        else:
            # Get response and log it
            response = get_response(user_input, name)
            print("Chatbot:", response)
            log_conversation("Chatbot: " + response)

# Start the chatbot
intermediate_chatbot()
