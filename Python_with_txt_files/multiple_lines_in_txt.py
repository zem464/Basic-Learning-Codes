# Write a method in python to write multiple line of text contents into a text file ``mylife.txt``. 

# Create  a file and open it
with open("mylife.txt", "a") as contents:
    while True:     # Use a while loop to ask the user for lines
        line_ask = input("\033[33m\033[1mEnter line: \033[35m\033[0m")  # Ask the user to input lines
        contents.write(str(line_ask) + "\n")                            # Write the lines in the text file
        line_more = input("\033[32m\033[1mMore lines? \033[31myes/no: \033[35m\033[0m") # Ask for another line
        
        if line_more == "yes":      # if yes, continue
            continue
        elif line_more == "no":     # elif no, break
            break
        else:                       # else, put "invalid input"
            print("\033[31mThis is an invalid answer. Enter another input.")
            line_ask = input("\033[32m\033[1mMore lines? \033[31myes/no: \033[35m\033[0m")  # Ask the user for a valid answer
            
            if line_ask == "n":     # If user input no, break
                break