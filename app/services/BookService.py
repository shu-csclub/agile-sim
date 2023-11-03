import database


class BookService:
    def __init__(self) -> None:
        pass

    def getAll(self):
        return database.books.to_dict(orient="records")

    def getRecommended(self):
        return (
            database.books[
                (database.books.average_rating > 4.5)
                & (database.books.text_reviews_count > 10000)
            ]
            .sort_values(by=["average_rating"], ascending=False)
            .to_dict(orient="records")
        )
