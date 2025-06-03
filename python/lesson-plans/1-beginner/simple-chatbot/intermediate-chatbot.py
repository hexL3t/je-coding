# Intermediate Chatbot: Uses a dictionary for cleaner responses
# and stores the user's name for a personal touch.

# This function checks the user's input and returns a matching response
def get_response(user_input, name):
    # Dictionary that maps keywords to specific chatbot responses
    responses = {
        'how are you': "I'm doing great, thanks for asking! 😊",
        'weather': "I can't check the weather right now, but I hope it's lovely where you are! ☀️",
        'joke': "Why did the math book look sad? Because it had too many problems! 😂",
        'hobby': "I love chatting with humans like you! 💬",
    }

    # Loop through the keywords and check if any are in the user's input
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]

    # If the input includes the word "name", respond accordingly
    if 'name' in user_input:
        if name == "":
            return "My name is Chatbot! What's yours?"
        else:
            return f"Nice to chat with you, {name}! 😊"
    
    # Default reply if nothing matches
    return "I'm still learning new things. Thanks for your patience! 😅"

# This function runs the chatbot and handles user interaction
def intermediate_chatbot():
    print("Hello! I'm your improved chatbot 🤖. Type 'bye' to end the chat.")

    name = ""  # This variable stores the user's name

    while True:
        # Get the user's message and convert it to lowercase
        user_input = input("You: ").lower()

        # If the user types 'bye', end the chat
        if user_input == 'bye':
            print("Chatbot: Goodbye! 👋")
            break

        # If the user tells their name, extract it and respond
        elif "my name is" in user_input:
            name = user_input.replace("my name is", "").strip().capitalize()
            print(f"Chatbot: Nice to meet you, {name}! 😄")

        else:
            # Get a response using the response function
            response = get_response(user_input, name)
            print("Chatbot:", response)

# Start the chatbot
intermediate_chatbot()
