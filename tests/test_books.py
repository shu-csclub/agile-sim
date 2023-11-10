import json
import database


def test_all_books(client):
    response = client.get("/api/books/")
    books = json.loads(response.data)
    assert books == database.books.to_dict(orient="records")


def test_all_publishers(client):
    response = client.get("/api/books/publishers")
    publishers = json.loads(response.data)['publishers']
    assert publishers == list(database.books.publisher.unique())
