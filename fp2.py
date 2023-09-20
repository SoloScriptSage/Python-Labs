#Final Project 2
#Vladyslav Hichuk

print(f"____________________________________________\n")
print("""
    ░█████╗░██╗░░██╗███████╗░██████╗░██████╗
    ██╔══██╗██║░░██║██╔════╝██╔════╝██╔════╝
    ██║░░╚═╝███████║█████╗░░╚█████╗░╚█████╗░
    ██║░░██╗██╔══██║██╔══╝░░░╚═══██╗░╚═══██╗
    ╚█████╔╝██║░░██║███████╗██████╔╝██████╔╝
    ░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")
print(f"____________________________________________\n")

print("\tCHESS PLAYER DATABASE")

#Checking for grammar is name and surname w uppercase

def checkGrammar(PN):
    if PN[0].isupper() and PN[PN.find(" ") + 1].isupper():
        return True
    else:
        return False

#Checking for numbers in name

def checkForNumbers(word):
    for ch in word:
        if ch.isdigit():
            return False
    return True
#Legal input for pieces

def legalPieces():
    print(f"\n____________________________________________\n")
    print("\tLEGAL VALUES FOR PIECES")
    print("Pawn\t-\tP")
    print("Knight\t-\tKN")
    print("Bishop\t-\tB")
    print("King\t-\tKG")
    print("Queen\t-\tQ")
    print(f"\n____________________________________________\n")

#Checking the name

while True:
    playerName = str(input("\nChess player first and last name: "))
    if checkGrammar(playerName) and checkForNumbers(playerName):
        break
    else: 
        print("WRITE FIRST AND LAST NAME WITH FIRST UPPERCASE LETTERS!!!")
        continue

# Checking the favorite piece

pieces = ["R", "B", "KN", "KG", "P", "Q"]

while True:
    legalPieces()
    favoritePiece = str(input("Favorite piece: "))
    if favoritePiece not in pieces:
        continue
    else: 
        break

#Checking Age

while True:
    age = input("Age: ")
    try:
        age = int(age)
        if age <= 0 and age <= 150:
            print("Use only numbers greater 0 and less than 150!!!")
            continue
        break
    except ValueError:
        print("USE ONLY NUMBERS!!!")

# Checking ELO

while True:
    rating = input("Rating: ")
    try:
        rating = float(rating)
        break
    except ValueError:
        print("USE ONLY NUMBERS!!!")



print(f"\n____________________________________________\n")
print(f"Player Name\t-\t{playerName}")
print(f"Age\t\t-\t{age}")
print(f"Favorite piece\t-\t{favoritePiece}")
print(f"Rating\t\t-\t{rating}")
print(f"\n____________________________________________\n")
