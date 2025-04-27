# Encrypts a given message using the Caesar cipher.
""" The Caesar cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet.
"""
def caesar_encrypt(message, shift): 
    result = ""	# Initialize an empty string to store the encrypted message
    for char in message: # Go through each character in the input message
        if char.isalpha(): 	# Check if the character is an alphabet letter (a-z or A-Z)
            base = ord('A') if char.isupper() else ord('a')	# Determine the base ASCII value for either uppercase or lowercase letters
            result += chr((ord(char) - base + shift) % 26 + base) # Apply the Caesar cipher shift:
							# 1. Get the numerical value of the current character (e.g., 'A' is 65).
							# 2. Subtract the base value to get its position in the alphabet (e.g., 'A' becomes 0).
							# 3. Add the shift value.
							# 4. Use the modulo operator (%) 26 to wrap around the alphabet if the shift goes beyond Z or z.
							# 5. Add the base value back to get the new ASCII value of the shifted letter.
							# 6. Convert the new ASCII value back to a character using chr().
        else:
            result += char # If the character is not a letter (e.g., space, number, punctuation), keep it as it is	
    return result # Return the final encrypted message'

# Decrypts the Message
"""
Decrypts a message that was encrypted using the Caesar cipher.

To decrypt, we simply apply the Caesar cipher with the opposite shift.
Shifting by 'shift' in one direction is the same as shifting by
26 - 'shift' in the opposite direction (since there are 26 letters in the alphabet).
"""
def caesar_decrypt(message, shift):
	return caesar_encrypt(message, 26 - shift) # Reuse the encryption function with the reverse shift

# User input
message = input("Enter a message: ")		# Ask the user to type in a message and store it in the 'message' variable
shift = int(input("Enter shift amount: "))	# Ask the user for the shift value (how many letters to shift) and convert it to an integer

# Encryption process
encrypted = caesar_encrypt(message, shift)	# Call the caesar_encrypt function with the user's message and shift value, and store the result in the 'encrypted' variable
print("Encrypted message:", encrypted)		# Display the encrypted message to the user

# Optional: Decryption process
print("Decrypted message:", caesar_decrypt(encrypted, shift)) # Call the caesar_decrypt function to reverse the encryption and display the original message