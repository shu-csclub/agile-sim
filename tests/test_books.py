import json
import database

def test_all_books(client):
    response = client.get("/api/books/")
    books = json.loads(response.data)
    assert books == database.books.to_dict(orient='records')


def test_recommended_books(client):
    response = client.get("/api/books/recommended")
    books = json.loads(response.data)
    for book in books:
        assert book['average_rating'] > 3.75
        assert book['text_reviews_count'] > 10000
