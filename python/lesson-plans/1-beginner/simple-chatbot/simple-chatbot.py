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

# Call the function to start the chatbot
simple_chatbot()
