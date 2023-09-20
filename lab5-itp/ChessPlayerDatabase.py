import ChessPlayer

class ChessPlayerDatabase:
    def __init__(self):
        self.database = []
        self.num_data = 0

    def addItem(self, item):
        self.database.append(item)
        self.num_data += 1

    def deleteItem(self, index):                            
        if 0 <= index < len(self.database):             
            self.database.pop(index)
            self.num_data -= 1                      # I'm assuming that's like the counter or something
        else:
            print("Invalid index. The player does not exist in the database.")  

    def getItem(self, index):
        return self.database[index]

    def displayAll(self):
        c = 0
        for player in self.database:
            print(f"---------{c}-----------")
            player.display()
            print(f"---------------------\n")
            c += 1
