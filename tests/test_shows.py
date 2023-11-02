import json
import database

def test_all_shows(client):
    response = client.get("/api/shows/")
    shows = json.loads(response.data)
    print(database.shows.to_dict(orient="records")[35])
    assert shows == database.shows.to_dict(orient="records")