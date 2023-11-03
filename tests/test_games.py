import json
import database


def test_all_games(client):
    response = client.get("/api/games/")
    games = json.loads(response.data)
    assert games == database.games.to_dict(orient="records")
