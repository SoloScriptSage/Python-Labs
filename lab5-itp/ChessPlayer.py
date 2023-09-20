import databaseio

class ChessPlayer:
    def __init__(self, Name, Age, Rating, FavoritePiece):
        self.name = Name
        self.age = Age
        self.rating = Rating
        self.favoritePiece = FavoritePiece

    def display(self):
        databaseio.print_data(self.name, self.age, self.rating, self.favoritePiece)
