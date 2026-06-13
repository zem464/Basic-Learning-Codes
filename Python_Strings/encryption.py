# Write a Python Script that will accept a string as a plain text and then the program will encrypt 
# it using the following character substitute:
# 'a' = *, 'e' = &, 'i' = # , 'o' = + 'u' = !

# Get an input from the user
text_input = input("Input a plaintext: ")
text_output = ""

# Check if the input has the variables and change it into corresponding symbols
for i in range(len(text_input)):

    if text_input[i].lower() == 'a':    # If there is 'a', change to '*'
        text_output += '*'

    elif text_input[i].lower() == 'e':  # If there is 'e', change to '&'
        text_output += '&'

    elif text_input[i].lower() == 'i':  # If there is 'i', change to '#'
        text_output += '#'

    elif text_input[i].lower() == 'o':  # If there is 'o', change to '+'
        text_output += '+'

    elif text_input[i].lower() == 'u':  # If there is 'u', change to '!'
        text_output += '!'
    else:
        text_output += text_input[i]
        
# Print the encrypted input
print(text_output)