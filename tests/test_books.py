import json
import database


def test_all_books(client):
    response = client.get("/api/books/")
    books = json.loads(response.data)
    assert books == database.books.to_dict(orient="records")
