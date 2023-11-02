import json

def test_all_books(client):
    response = client.get("/api/books/")
    assert response.status_code == 200

def test_popular_books(client):
    response = client.get("/api/books/recommended")
    books = json.loads(response.data)
    for book in books:
        assert book['average_rating'] > 4.5
        assert book['ratings_count'] > 10000