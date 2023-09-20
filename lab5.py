# Lab 5
# Vladyslav Hirchuk

# Method that prompts the user for the mass in kilograms
def getMass():
    # Global variable "mass" for formula
    global mass
    mass = float(input("Enter the mass (kg) of the object: "))

# Method that prompts the user for the velocity in meters per second
def getVelocity():
    # Global variable "velocity" for formula
    global velocity
    velocity = int(input("Enter the velocity (m/s) of the object: "))

# Method that receives the mass and velocity from the main module and calculates and returns the kinetic energy for velocity = 0 to the entered velocity
def calcKE(_velo, _mass):
    KE = 0.5 * _mass * pow(_velo, 2)
    return KE

# Main method that starts the program
def main():
    getMass()
    getVelocity()

    for velo in range(velocity + 1):
        print(f"{velo}\t\t{calcKE(velo, mass)}")

main()
