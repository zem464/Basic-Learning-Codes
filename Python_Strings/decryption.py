# Write a Python Script that will accept a string as encrypted text and then the program will 
# decrypt it using the following character substitute:
# 'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !

# Get an encrypted input from the user
encrypted_input = input("Input the encrypted text: ").lower()
decrypted_output = ""

# Check for the corresponding symbol to substitute
for i in range(len(encrypted_input)):

    if encrypted_input[i] == '*':   # If there is '*', change to 'a'
        decrypted_output += 'a'

    elif encrypted_input[i] == '&': # If there is '&', change to 'e'
        decrypted_output += 'e'

    elif encrypted_input[i] == '#': # If there is '#', change to 'i'
        decrypted_output += 'i'

    elif encrypted_input[i] == '+': # If there is '+', change to 'o'
        decrypted_output += 'o'

    elif encrypted_input[i] == '!': # If there is '!', change to 'u'
        decrypted_output += 'u'
    else:
        decrypted_output += encrypted_input[i]

# Print the decrypted input
print(decrypted_output)