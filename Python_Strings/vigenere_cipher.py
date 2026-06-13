# Write a program that asks the user for the plaintext (all uppercase letters, no spaces) and the 
# keyword (all uppercase letters) and produce the ciphertext using the Vigenère cipher. 
# Give the output of your program for the following message and key:
# Message: THISISTHELASTTASKHOORDAY
# Key: KNIGHTS

# Define function to generate keyword
def Keyword(message, key):
    key = list(key)

    if len(message) == len(key):    # If the length of the message == key, return key
        return key
    else:   # If not, append the key to the end of the key until the length of the key == message
        for i in range (len(message) - len(key)):
            key.append(key[i % len(key)])
        return ("".join(key))

# Define function to encrypt the message
def encryption(message, key):
    encrypt_message = []

    for i in range(len(message)):   # Add modulo 26 to the message and key and convert it to the corresponding character
        x = (ord(message[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypt_message.append(chr(x))
    return ("".join(encrypt_message))
 
if __name__ == "__main__":
# Ask user for the message and keyword all in uppercase letters and no spaces
    message = input("Enter the message in capital letters and no spaces: ")
    message_keyword = input("Enter the keyword in capital letters: ")
    key = Keyword(message, message_keyword)
    encrypt_message = encryption(message, key)
# Print the encrypted ciphertext using the Vigenere cipher
    print ("Encrypted message: ",encrypt_message)