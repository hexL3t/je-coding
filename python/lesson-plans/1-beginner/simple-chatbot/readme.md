Simple Chatbot
==============

A beginner-friendly Python chatbot that uses basic string matching to interact with users.
Perfect for students learning conditionals, loops, and input handling.

Project Objective
-----------------
Build a simple rule-based chatbot that:
- Greets the user
- Responds to common phrases like "how are you" or "what's your name"
- Uses conditionals and loops
- Ends the conversation when the user types 'bye'

Skills Practiced
----------------
- while loops
- if...elif...else conditionals
- String manipulation (.lower(), in)
- Terminal input/output

How to Run
----------
1. Make sure you have Python installed (version 3.6 or higher).
2. Download or copy the simple_chatbot.py file.
3. Open a terminal and run:

   python simple_chatbot.py

Example Conversation
--------------------
Hello! I'm a chatbot 🤖. Type 'bye' to end the conversation.
You: how are you
Chatbot: I'm doing great, thank you! 😊
You: what's your name
Chatbot: I'm Chatbot, nice to meet you! 😄
You: bye
Chatbot: Goodbye! 👋

Extension Ideas
---------------
- Add more phrases (e.g. "Tell me a joke")
- Use .strip() and .capitalize() to clean up user inputs
- Add a GUI using Tkinter

License
-------
This project is open source and available under the MIT License.


Intermediate Chatbot
====================

An upgraded Python chatbot that uses dictionaries, personalizes responses with the user's name,
gives time-based greetings, and saves chat history to a file.

Project Objective
-----------------
Build a more sophisticated chatbot with:
- Organized responses using dictionaries
- Personalized interaction with user-provided names
- Time-based greetings (Good morning / afternoon / evening)
- Conversation logging to chat_log.txt

Skills Practiced
----------------
- Dictionaries for keyword–response mapping
- String parsing and data extraction
- datetime module (working with system time)
- File I/O for saving chat history
- Function-based code organization

How to Run
----------
1. Make sure you have Python installed (version 3.6 or higher).
2. Download or copy the intermediate_chatbot.py file.
3. Open a terminal and run:

   python intermediate_chatbot.py

The chatbot will generate or update a file called chat_log.txt to store your conversation history.

Example Features
----------------
User input: "my name is Sam"
→ Chatbot replies: "Nice to meet you, Sam!"

User input: "joke"
→ Chatbot replies: "Why did the math book look sad? Because it had too many problems!"

User input: "bye"
→ Chatbot replies: "Goodbye! 👋 Have a nice day!"

Files Included
--------------
- intermediate_chatbot.py : Main chatbot code
- chat_log.txt : Automatically generated log file of your chat

Extension Ideas
---------------
- Add fuzzy keyword matching with difflib or regex
- Use a GUI library (e.g., Tkinter or PyQt)
- Create a Flask web version for use in browsers

License
-------
This project is licensed under the MIT License. Contributions welcome!
