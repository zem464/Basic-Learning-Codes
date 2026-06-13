# import the functions of tv class
from class_tv import TV

# Create a program for testing
def TestTV():
    tv1 = TV("", "")
    tv2 = TV("", "")    

    # Assign the values for TV1
    tv1.channel_setting(30)
    tv1.volume_setting(3)
    tv1.TV_off()

    # Assign the values for TV2
    tv2.channel_setting(3)
    tv2.volume_setting(2)
    tv2.TV_off()

    # Print the values
    print("\n\033[31m\033[1mTwo TV from the UML: \033[31m\033[0m\n")
    print("=========================================================\n")
    print("\033[31m>>","\033[37mTV1's channel is", tv1.get_channel(), "and the volume level is", tv1.get_volume())
    print("\033[31m>>", "\033[37mTV2's channel is", tv2.get_channel(), "and the volume level is", tv2.get_volume(), '\n')

# End the program
TestTV()