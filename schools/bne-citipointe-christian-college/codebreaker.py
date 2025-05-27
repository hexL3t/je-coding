# Encrypts a given message  using Caeser Cipher
def caeser_encrypt(message, shift):
    result = "" # Initialise an empty string to store the encrypted message
    for char in message: # Go through each character in the input message
        if char.isalpha(): # Check if the character is an alphabet letter (a-z or A-Z)
            base = ord('A') if char.isupper() else ord('a') 
            # Determine the base ASCII value for either Uppercase or lowercase letters
            result += chr((ord(char) - base + shift) % 26 + base) # Apply the Caeser Cipher
            """
            1. Get Numerical Value of the current character (e.g. A = 65)
            2. Subtract the base value and get it's position in the alphabet (eg. A = 0)
            3. Add the shift value
            4. Use the modulus operator (%) 26 to wrap around the alphabet, 
                    if the shift goes beyond Z or z.
            5. Add the base value back to get the new ASCII value of the shifted letter
            6. Convert the ASCII value back to a character using chr().
            7. Saves result as variable 'result'
            """
        else:
            result += char # if the character is not a letter (space, number, punctuation), keep as is.
    return result # return the final encrypted message

# Decrypts the Message
def caesar_decrypt(message, shift):
    return caeser_encrypt(message, 26 - shift) # Reuse the encryption function with the reverse shift

# Brute-Force Function
def caeser_brute_force(cipher_text):
    print("\n Brute Force Possibilities: ") # Inform the user that we are going to try 'ALL' possible decryptions
    for shift in range(1,26):  # Looping through all possible shift values from 1 to 25 (0, 26 = original message)
        print(f"Shift {shift}: {caesar_decrypt(cipher_text, shift)}")
        # For each shift value, decrypt the cipher_text and print the result along with the shift value used
        # This allows the user to read through the possibilities and see if any of them look like the message.

# User Input
message  = input("Enter a message: ") # Ask the user to type in a message and store it in the 'message' variable
shift = int(input("Enter a shift amount: ")) # As the user for the shift value (how many letters to shift) 
                                            # Convert String into a Integer

# Encryption Process
encrypted = caeser_encrypt(message, shift) # Call the function with the user's message and shift value, store as 'encrypted'
print("Encrypted Message:", encrypted)  # Display the encrypted message

# Decryption Process
print("Decrypted Message: ", caesar_decrypt(encrypted, shift)) # Call the caeser_decrypt function to reverse the encryption

# Brute-Force Process
# caeser_brute_force(encrypted) #Uncomment the line to test.