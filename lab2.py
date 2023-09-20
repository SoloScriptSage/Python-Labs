player_name = str(input("Enter a player name: "))
try:
    if player_name.isnumeric or player_name.isdigit:
        print("It's not a name!")
        player_name = str(input("Enter a player name: "))
except:
    pass

age = int(input("Enter a player age: "))
try:
    # to check is this number less than 0
    if age < 0:
        print("Age cannnot be less than 0")
        age = int(input("Enter a player age: "))
except:
    pass
