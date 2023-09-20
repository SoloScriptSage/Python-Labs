

import ChessPlayerDatabase
import ChessPlayer
import databaseio
import os
import subprocess

CPD = ChessPlayerDatabase.ChessPlayerDatabase()

# Delete a player from the database
def delete_item():
    while True:
        if len(CPD.database) != 0:  # Check if the database is not empty
            try:
                delete_index = int(input("Enter the index of an item to delete or enter -1 to leave: "))
                if delete_index < -1 or delete_index >= len(CPD.database):
                    print(f"Invalid index. Please enter an index from 0 to {len(CPD.database) - 1}, or -1 to leave.")
                    continue
                elif delete_index == -1:
                    break
                else:
                    CPD.deleteItem(delete_index)
                    print("Successfully deleted!")
            except ValueError:
                print("Invalid input. You cannot use letters. Please enter the index of the existing player.")
        else:
            print("Database is empty.")
            break

# STARTS FROM HERE

while True:
    databaseio.display_menu()

    choice = input("\nEnter the number: ")

    match choice:
        case "1":
            player_data = databaseio.read_data()
            player = ChessPlayer.ChessPlayer(player_data[0], player_data[1], player_data[2], player_data[3])
            CPD.addItem(player)
        case "2":
            delete_item()
        case "3":
            CPD.displayAll()
        case "4":
            CPD.save("cpd.csv")
        case "5":
            CPD.load("cpd.csv")
        case "6":
            CPD.clear_database()
            print("Done! Database is empty.")
        case "7":
            quit()
        case _:
            print("Invalid input. Please enter a number.")



