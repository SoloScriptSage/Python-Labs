import os
from subprocess import call
from time import sleep

class ChessPlayer():
    def __init__(self, Name, Age, Rating, FavoritePiece):
        self.name = Name
        self.age = Age
        self.rating = Rating
        self.favoritePiece = FavoritePiece

chessPlayer_database = []

def display_menu():
    while True:
        display_logo()
        print("\t\tMENU")
        print("1. Add a new player to the database")
        print("2. Delete a player from the database")
        print("3. Display the current database")
        print("4. Exit")

        choice = input("Enter the number: ")

        match choice:
            case "1":
                read_data()
            case "2":
                delete_item()
            case "3":
                display_all()
            case "4":
                quit()
            case _:
                print("Invalid input. Please enter a number.")

# ---------------------- ADD ITEMS TO OUR DATABASE ------------------ #

# Add a new player to the database
def read_data():

    # --------------- Checking the name --------------- #

    while True:
        pN = input("\nChess player first and last name: ")
        if checkGrammar(pN) and checkForNumbers(pN):
            break
        else:
            print("Invalid input. Please enter first and last name.")
            continue

    # ---------- Checking the favourite piece --------- #

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
    chessPlayer_database.append(ChessPlayer(pN, ag, ra, fP))                    

    print(f"Players in database now: {len(chessPlayer_database)}")

# ------------------ DELETE ITEMS FROM DATABASE ------------------ #

# Delete a player from the database
def delete_item():
    delete_name = input("Enter the name of a player to delete: ")

    for player in chessPlayer_database:
        if player.name == delete_name:
            chessPlayer_database.remove(player)
            print("Successfully deleted!")
            break
    else:
        print("Player not found.")

# ---------------------- DISPLAY THE DATABASE -------------------- #

# Display the current database
def display_all():
    if len(chessPlayer_database) == 0:
        print("The database is empty.")
    else:
        for player in chessPlayer_database:
            print("\n____________________________________________\n")
            print_data(player.name, player.age, player.rating, player.favoritePiece)

# Not necesserily neeeded method but required in the assignment
def print_data(n, a, r, f):
    print(f"Name: {n}")
    print(f"Age: {a}")
    print(f"Rating: {r}")
    print(f"Favorite piece: {f}")


# ----------------------- ADDITIONAL CODE --------------------- #

# Logo

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

# Legal Pieces

def legalPieces():
    print("\n____________________________________________\n")
    print("\tLEGAL VALUES FOR PIECES")
    print("Pawn\t-\tP")
    print("Knight\t-\tKN")
    print("Bishop\t-\tB")
    print("King\t-\tKG")
    print("Queen\t-\tQ")
    print("\n____________________________________________\n")

# ------------------------- GRAMMARLY ------------------------ #

# Check is name is actually a name :D
def checkGrammar(PN):
    if PN[0].isupper() and PN[PN.find(" ") + 1].isupper():
        return True
    else:
        return False

# Check for numbers in the name
def checkForNumbers(word):
    for ch in word:
        if ch.isdigit():
            return False
    return True

# -------------------------- --------- ----------------------- #

display_menu()
