import database

class BookService:
    def __init__(self) -> None:
        pass

    def getAll(self):
        return database.books.to_dict(orient='records')

    def getPopularBooks(self):
        return database.books[database.books.average_rating > 4.5].sort_values(by=['average_rating'], ascending=False).to_dict(orient='records')