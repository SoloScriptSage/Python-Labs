
# Lab 5
# Vladyslav Hirchuk

# Method that asks for ID
def getID():
    global _ID
    validIDs = [101, 102, 103]
    while True:
        _ID = int(input("Please enter the object id: "))
        if _ID in validIDs:
            break
        else:
            print("Invalid object id!")
            
# Method that prompts the user for the mass in kilograms
def getMass():
    # Global variable "mass" for formula
    global mass

    while True:
        mass = int(input("Enter the mass (kg) of the object: "))
        if mass > 0:
            break
        else:
            print("ERROR: Mass must be greater than 0")

# Method that prompts the user for the velocity in meters per second
def getVelocity():
    # Global variable "velocity" for formula
    global velocity

    while True:
        velocity = int(input("Enter the velocity (m/s) of the object: "))
        if velocity > 0 and velocity <= 100:
            break
        else:
            print("ERROR: Velocity must be greater than 0 and less than or equal to 100")

# Method that receives the mass and velocity from the main module and calculates and returns the kinetic energy for velocity = 0 to the entered velocity
def calcKE(_velo, _mass):
    KE = 0.5 * _mass * pow(_velo, 2)
    return KE

# Main method that starts the program
def main():
    getID()
    getMass()
    getVelocity()

    for velo in range(velocity + 1):
        print(f"{velo}\t\t{calcKE(velo, mass)}")

main()
