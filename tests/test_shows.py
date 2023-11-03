import json
import database


def test_all_shows(client):
    response = client.get("/api/shows/")
    shows = json.loads(response.data)
    assert shows == database.shows.to_dict(orient="records")
