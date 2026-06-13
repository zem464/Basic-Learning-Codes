# This code will ask for the name of a person and their dream job, then print a message with that information.

# Ask the user for their name and dream job
name = input("What is your name?: ")
dream_job = input(f"{name.capitalize()}, what is your dream job?: ")

# Check if the dream job starts with a vowel and print the appropriate message
if dream_job.startswith(("a", "e", "i", "o", "u")):
    print("%s, you will be an %s in the future!" % (name.capitalize(), dream_job))
else:
    print("%s, you will be a %s in the future!" % (name.capitalize(), dream_job))