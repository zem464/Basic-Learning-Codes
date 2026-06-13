# Import class
from class_fan import Fan

# Create a defining function for the objects
def TestFan():
    fan1 = Fan(Fan.fast, 10, "Yellow", True)
    fan2 = Fan(Fan.medium, 5, "Blue", False)

    # Display fan1
    print("\n[\033[35;40m\033[1m    First Fan   \033[0m]")
    print("\n\033[31;40m\033[1mSpeed: \033[31m\033[0m", fan1.get_speed())
    print("\033[31;40m\033[1mRadius: \033[31m\033[0m", fan1.get_radius())
    print("\033[31;40m\033[1mColor: \033[31m\033[0m", fan1.get_color())
    print("\033[31;40m\033[1mOn: \033[31m\033[0m", fan1.get_fan_on())

    # Display fan2
    print("\n[\033[35;40m\033[1m    Second Fan  \033[0m]")
    print("\n\033[31;40m\033[1mSpeed: \033[31m\033[0m", fan2.get_speed())
    print("\033[31;40m\033[1mRadius: \033[31m\033[0m", fan2.get_radius())
    print("\033[31;40m\033[1mColor: \033[31m\033[0m", fan2.get_color())
    print("\033[31;40m\033[1mOn: \033[31m\033[0m", fan2.get_fan_on())

# Call the main function
TestFan()