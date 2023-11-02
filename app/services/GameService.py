import database


class GameService:
    def __init__(self) -> None:
        pass

    def getAll(self):
        return database.games.to_dict(orient="records")
