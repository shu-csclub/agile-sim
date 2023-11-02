import database


class ShowService:
    def __init__(self) -> None:
        pass

    def getAll(self):
        return database.shows.to_dict(orient="records")
