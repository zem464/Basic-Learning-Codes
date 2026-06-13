# Import class
from class_car import Car

# Create the object
car = Car(2013, 'Hyundai', 0)

# Print the accelerating information 
print("\n[\033[35;40m\033[1m    ACCELERATION    \033[31m\033[0m]")
print("\n\033[34;40m\033[1mCar year model: \033[31m\033[0m", car.get_year_model())
print("\033[34;40m\033[1mCar made of: \033[31m\033[0m", car.get_make())
print("\n\033[37;40m\033[1m<<<  SPEED   >>>\033[0m")
for _ in range(5):
    car.accelerate()
    print("\n\033[33;40m\033[1mCurrent speed: \033[31m\033[0m", car.get_speed())

# Print the braking information
print("\n[\033[35;40m\033[1m     BRAKE     \033[31m\033[0m]")
print("\n\033[34;40m\033[1mCar year model: \033[31m\033[0m", car.get_year_model())
print("\033[34;40m\033[1mCar made of: \033[31m\033[0m", car.get_make())
print("\n\033[37;40m\033[1m<<<  SPEED   >>>\033[0m")
for _ in range(5):
    car.brake()
    print("\n\033[31;40m\033[1mCurrent speed: \033[31m\033[0m", car.get_speed())