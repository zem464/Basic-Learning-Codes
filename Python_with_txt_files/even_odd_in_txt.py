# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text files; the first text file will be named even.txt that will 
# contain all even numbers extracted from the numbers.txt. The second text file will be named odd.txt 
# that will contain all odd numbers extracted from the numbers.txt.

# Create a method to process the text files
def integers():
    # Create a text file named for the 20 integers, even integers, and odd integers
    with open("numbers.txt") as numbers_input, open("even.txt", "a") as even_num, open("odd.txt", "a") as odd_num:
        for line in numbers_input:  # Read the text line by line
            if line.strip():        # Convert the line to an integer
                int_input = int(line)
                if int_input % 2 == 0:  # Check if line is even, if even, write to even.txt
                    even_num.write(str(int_input) + "\n")
                else:   # if odd, write to odd.txt
                    odd_num.write(str(int_input) + "\n")
# End the Program
integers()