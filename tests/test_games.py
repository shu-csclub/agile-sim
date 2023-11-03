import json
import database


def test_all_games(client):
    response = client.get("/api/games/")
    games = json.loads(response.data)
    assert games == database.games.to_dict(orient="records")

def test_genres(client):
    response = client.get("/api/games/genres")
    genres = json.loads(response.data)['genres']
    assert genres == list(database.games.genre.unique())
