# Encryption Function
# Encrypts a given message using the Caesar Cipher
""" The Caesar cipher is a simple substitution cipher where each 
letter in the plaintext is shifted a certain number of places 
down the alphabet.
"""
def caesar_encrypt(message, shift):
    result = "" # Initialise an empty string to store the encrypted message
    for char in message:    # Go through each character in the input message
        if char.isalpha():   # Check if the character is an alphabet letter (A-Z or a-z)
            # Determine the base ASCII value for the letter (uppercase OR lowercase)
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            # Apply the Caeser Cipher shift:
                # 1. Get the Numerical value of the current character (e.g A = 65)
                # 2. Subtract the base value to get current position (e.g. A = 0)
                # 3. Add the shift value
                # 4. Use the modulus operator (%) 26 to wrap around alphabet, if shift 
                # goes beyond Z or z.
                # 5. Add the base value back to get the new ASCII value
                # 6. Convert the new ASCII value back using chr()
                # 7. Save into the 'result' variable
        else:
            #If the character is not a letter (eg. space, punctuation, number), leave as is.
            result += char 
    return result # Return the final encrypted message
    
#Decryption
# Decyrpts a message that was encrypted using Caeser Cipher
"""
To decrypt, we simply apply the Caesar cipher with the opposite shift.
Shifting by 'shift' in one direction is the same as shifting by
26 - 'shift' in the opposite direction (since there are 26 letters in the alphabet).
"""
def caesar_decrypt(message, shift):
    # Reuse the encryption function with the reverse shift
    return caesar_encrypt(message, 26 - shift)  

# User Input
message = input("Enter a message: ") # Ask user to input their message
shift = int(input("Enter the shift amount: ")) # Ask the user for the shift amount

# Encryption Process
encrypted = caesar_encrypt(message,shift) # Call the caeser_encrypt function
print ("Encrypted Message: ", encrypted)  # Display the encrypted message

# Decryption Process
print("Decrypted Message: ", caesar_decrypt(encrypted, shift))
# call the caesar decrypt function reverse the encryption and display original message