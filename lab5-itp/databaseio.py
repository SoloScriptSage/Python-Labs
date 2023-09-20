#Vladyslav Hirchuk
#Final Project 4

from ast import Try
from multiprocessing import Value
from queue import Empty
from re import I

def display_menu():
        display_logo()
        print("\t\tMENU")
        print("1. Add a new player to the database")
        print("2. Delete a player from the database")
        print("3. Display the current database")
        print("4. Exit")

def read_data():

    # --------------- Reading the name --------------- #

    while True:
        pN = input("\nChess player first and last name: ")
        if len(pN.split()) == 2 and checkGrammar(pN) and checkForNumbers(pN):
            break
        else:
            print("Invalid input. Please enter first and last name.")
            continue

    # ---------- Reading the favourite piece --------- #

    pieces = ["R", "B", "KN", "KG", "P", "Q"]

    while True:
        legalPieces()
        fP = input("Favorite piece: ")
        if fP not in pieces:
            continue
        else:
            break

    # ---------------- Checking the age --------------- #

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

    # ------------------ Checking ELO ----------------- #
     
    while True:
        ra = input("Rating: ")
        try:
            ra = float(ra)
            break
        except ValueError:
            print("USE ONLY NUMBERS!!!")

        # Finally, we add player to our database

    return pN, ag, ra, fP     

# Not necesserily neeeded method but required in the assignment
def print_data(r1, r2, r3, r4):
    print(f"Name: {r1}")
    print(f"Age: {r2}")
    print(f"Rating: {r3}")
    print(f"Favorite piece: {r4}")

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

def legalPieces():
    print("\n____________________________________________\n")
    print("\tLEGAL VALUES FOR PIECES")
    print("Pawn\t-\tP")
    print("Knight\t-\tKN")
    print("Bishop\t-\tB")
    print("King\t-\tKG")
    print("Queen\t-\tQ")
    print("\n____________________________________________\n")

def checkGrammar(PN):
    if PN[0].isupper() and PN[PN.find(" ") + 1].isupper():
        return True
    else:
        return False

def checkForNumbers(word):
    for ch in word:
        if ch.isdigit():
            return False
    return True
