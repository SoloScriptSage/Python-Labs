import ChessPlayer
import csv
import os # for deleting the file and hope to clear the console but it doesn't work

# Class chessplayer
class ChessPlayerDatabase:
    # Array and len_num
    def __init__(self):
        self.database = []
        self.num_data = 0

    # Add item to array
    def addItem(self, item = ChessPlayer.ChessPlayer):
        self.database.append(item)
        self.num_data += 1

    # Delete item[by index]
    def deleteItem(self, index):                            
        if 0 <= index < len(self.database):             
            self.database.pop(index)
            self.num_data -= 1                      # Counter
        else:
            print("Invalid index. The player does not exist in the database.")  

    # Return item[by index]
    def getItem(self, index):
        return self.database[index]

    # Display self array
    def displayAll(self):
        c = 0
        for player in self.database:
            print(f"---------{c}-----------")
            player.display()
            print(f"---------------------\n")
            c += 1

    def clear_database(self):
        self.database.clear()

    def save(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
        with open(filename, mode = 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(["Name","Age","Rating","Favouite piece"])
            for player in self.database:
                writer.writerow([player.name, player.age, player.rating, player.favoritePiece])

    def load(self, filename):
        self.database.clear()
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader) # skipping the line with ["name","age","rating","favouite piece"]
            for row in reader:
                name, age, rating, favorite_piece = row
                age = int(age)
                rating = float(rating)
                player = ChessPlayer.ChessPlayer(name, age, rating, favorite_piece)
                self.addItem(player)
