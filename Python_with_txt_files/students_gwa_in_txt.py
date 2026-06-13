# Write a Python program that read a file containing the name of 20 students together with their GWA. 
# The program will output the name of the student who got the highest GWA (including the GWA).

# Create and open the file with students and gwa
with open("students_gwa.txt") as student_file:
    # Initialize lowest possible gwa and student name
    gwa_equivalent = 5.0
    gwa_student = ""
    
    for line in student_file:       # Read the file line by line
        name, gwa_str = line.strip().split(" : ")       # Split the name and gwa
        gwa = float(gwa_str)    # Check if the gwa is lower than the current lowest gwa, if yes, update the lowest gwa and student name
        if gwa < gwa_equivalent:
            gwa_equivalent = gwa
            gwa_student = name
            
# Print the name with highest gwa
print("\033[31m\033[1mHighest GWA awardee: \033[35m\033[0m", gwa_student)
print("\033[31m\033[1mGWA: \033[35m\033[0m", gwa_equivalent)