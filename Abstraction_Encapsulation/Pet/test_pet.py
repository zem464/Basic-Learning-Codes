# Import class
from class_pet import Pet

# Create the object
pet = Pet()

# Ask for inputs
print("\n[\033[35;40m\033[1m     About your pet...     \033[31m\033[0m]")
pet.set_name(input("\n\033[32;40m\033[1mWhat is the name of your pet?: \033[31m\033[0m"))
pet.set_animal_type(input("\033[32;40m\033[1mWhat type of animal is your pet?: \033[31m\033[0m"))
pet.set_age(input("\033[32;40m\033[1mHow old is your pet?(in months): \033[31m\033[0m"))

# Print the information
print("\n[\033[35;40m\033[1m     Pet's Information     \033[31m\033[0m]")
print("\n\033[31;40m\033[1mName: \033[31m\033[0m", pet.get_name())
print("\033[31;40m\033[1mAnimal Type: \033[31m\033[0m", pet.get_animal_type())
print("\033[31;40m\033[1mAge: \033[31m\033[0m", pet.get_age(), "- month old")