#Vladyslav Hirchuk
#Final Project 6

from ast import Try
from multiprocessing import Value
from queue import Empty
from re import I

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Read chess player info
def read_data():

    # Reading name

    while True:
        pN = input("\nChess player first and last name: ")
        if len(pN.split()) == 2 and checkGrammar(pN) and checkForNumbers(pN):
            break
        else:
            print("Invalid input. Please enter first and last name.")
            continue

    # Reading piece

    pieces = ["R", "B", "KN", "KG", "P", "Q"]

    while True:
        legalPieces()
        fP = input("Favorite piece: ")
        if fP not in pieces:
            continue
        else:
            break

    # Reading age

    while True:
        ag = input("Age: ")
        try:
            ag = int(ag)
            if ag <= 0:
                print("Invalid input. Age cannot be less than 0. Please enter player age.")
                continue
            break
        except ValueError:
            print("Invalid input. You cannot use letters. Please enter player age.")

    # Reading ELO
     
    while True:
        ra = input("Rating: ")
        try:
            ra = float(ra)
            break
        except ValueError:
            print("USE ONLY NUMBERS!!!")

        # Add player to database

    return pN, ag, ra, fP     

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Print menu
def display_menu():
        display_logo()
        print("\t\tMENU")
        print("1. Add a new player to the database")
        print("2. Delete a player from the database")
        print("3. Display the current database")
        print("4. Save to file current database")
        print("5. Load the current database from file")
        print("6. Clear database")
        print("7. Exit")
# Print name age rating piece
def print_data(r1, r2, r3, r4):
    print(f"Name: {r1}")
    print(f"Age: {r2}")
    print(f"Rating: {r3}")
    print(f"Favorite piece: {r4}")
# Print Logo
def display_logo():
    print("\n____________________________________________\n")
    print("""
    ░█████╗░██╗░░██╗███████╗░██████╗░██████╗
    ██╔══██╗██║░░██║██╔════╝██╔════╝██╔════╝
    ██║░░╚═╝███████║█████╗░░╚█████╗░╚█████╗░
    ██║░░██╗██╔══██║██╔══╝░░░╚═══██╗░╚═══██╗
    ╚█████╔╝██║░░██║███████╗██████╔╝██████╔╝
    ░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")
    print("\n____________________________________________\n")
# Print legal pieces
def legalPieces():
    print("\n____________________________________________\n")
    print("\tLEGAL VALUES FOR PIECES")
    print("Pawn\t-\tP")
    print("Knight\t-\tKN")
    print("Bishop\t-\tB")
    print("King\t-\tKG")
    print("Queen\t-\tQ")
    print("\n____________________________________________\n")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Check for uppercase in name
def checkGrammar(PN):
    if PN[0].isupper() and PN[PN.find(" ") + 1].isupper():
        return True
    else:
        return False

# Check for numbers in name
def checkForNumbers(word):
    for ch in word:
        if ch.isdigit():
            return False
    return True
