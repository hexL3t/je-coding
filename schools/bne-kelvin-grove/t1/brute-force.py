# Brute-Force
# A brute-force attack is a hacking method that tries every possible combination
# to unlock a password or system. Like trying every letter, number and symbol.

import time # Import time to track the duration of the cracking process

def bruteForce(password):
        startTime = time.time() # Record the start time to measure how long it takes

        # Define the dictionary of all possible characters for the password
        dictionary = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  # lowercase letters
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',  # uppercase letters
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',  # digits
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', 
        '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '{', 
        '|', '}', '~'  # special characters    
        ]

        letter = [] # Initialise an empty list to store matched characters progressively
        pWord = password  # Store the input password for comparison

        # Loop over each character in the password
        for x in range(0, len(pWord)):
                # Loop through the dictionary to find a matching character for the password position
                for y in range(0, len(dictionary)):
                        if pWord[x] == dictionary[y]:        # If a match is found
                                letter.append(dictionary[y]) # Append the matched character to the 'letter'
                                print(f"Current Match: {''.join(letter)}") # Print current matched password
                                break # Break out of the inner loop once a match is found, moving on....
        
        # After completing the loop, print the fully matched password
        print(f"\nPassword: {''.join(letter)}")

        # Calculate and print the elaspsed time for the password cracking process
        endTime = time.time() # Records the end of the time
        elapsedTime = endTime - startTime  # Calculate the elapsed time
        print(f"That took {elapsedTime:.3f} seconds to crack") # Print the time with 3 decimal places

# Call the password cracker function with a password
bruteForce("L3arn2c0D3!!@@..")  # Add your own password into the " "
