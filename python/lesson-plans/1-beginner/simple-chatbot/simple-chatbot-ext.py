# Project 9: Simple Chatbot
# This program creates a basic chatbot that can respond to simple user inputs.

def simple_chatbot():
    # Greet the user and explain how to end the conversation
    print("Hello! I'm a chatbot 🤖. Type 'bye' to end the conversation.")
    
    # Start an infinite loop to keep the conversation going
    while True:
        # Get user input and convert it to lowercase to make comparisons easier
        user_input = input("You: ").lower()
        
        # Check if the user wants to end the conversation
        if user_input == 'bye':
            print("Chatbot: Goodbye! 👋")
            break  # Exit the loop
        
        # Respond if the user asks "how are you"
        elif 'how are you' in user_input:
            print("Chatbot: I'm doing great, thank you! 😊")
        
        # Respond if the user mentions "name"
        elif 'name' in user_input:
            print("Chatbot: I'm Chatbot, nice to meet you! 😄")
        
        # Catch-all response if the chatbot doesn't understand the input
        else:
            print("Chatbot: I'm not sure how to respond to that. 😅")

# 🏆 Extension – Advanced Chatbot with More Conditionals
# This version adds more responses and feels more interactive!

def advanced_chatbot():
    # Greet the user and give simple instructions
    print("Hello! I'm your advanced chatbot 🤖. Type 'bye' to end the conversation.")
    
    # Start a loop that keeps the chatbot running until the user says "bye"
    while True:
        # Get the user's input and convert it to lowercase to make matching easier
        user_input = input("You: ").lower()
        
        # If the user types 'bye', end the conversation and break the loop
        if user_input == 'bye':
            print("Chatbot: Goodbye! 👋")
            break  # Exit the loop
        
        # If the user asks how the chatbot is doing
        elif 'how are you' in user_input:
            print("Chatbot: I'm doing great, thank you for asking! 😊")
        
        # If the user mentions "name"
        elif 'name' in user_input:
            print("Chatbot: I'm Chatbot, a friendly assistant! What's your name? 😊")
        
        # If the user asks about the weather
        elif 'weather' in user_input:
            print("Chatbot: I can't check the weather right now, but I hope it's sunny where you are! ☀️")
        
        # If the user wants to hear a joke
        elif 'joke' in user_input:
            print("Chatbot: Why don't skeletons fight each other? They don't have the guts! 😂")
        
        # Default reply if none of the conditions above are met
        else:
            print("Chatbot: I'm still learning, but I'll try my best to understand you! 😅")

# Call the function to start the chatbot
# simple_chatbot()

# Call the function to run the chatbot
advanced_chatbot()