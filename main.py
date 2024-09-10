from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publisher": "J.B. Lippincott & Co.",
        "published_date": "1960-07-11",
        "page_count": 281,
        "language": "English"
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "publisher": "Secker & Warburg",
        "published_date": "1949-06-08",
        "page_count": 328,
        "language": "English"
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Charles Scribner's Sons",
        "published_date": "1925-04-10",
        "page_count": 180,
        "language": "English"
    },
    {
        "id": 4,
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel García Márquez",
        "publisher": "Harper & Row",
        "published_date": "1970-06-05",
        "page_count": 417,
        "language": "Spanish"
    },
    {
        "id": 5,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "publisher": "Little, Brown and Company",
        "published_date": "1951-07-16",
        "page_count": 234,
        "language": "English"
    },
    {
        "id": 6,
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "publisher": "The Russian Messenger",
        "published_date": "1866-01-01",
        "page_count": 430,
        "language": "Russian"
    },
    {
        "id": 7,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publisher": "T. Egerton, Whitehall",
        "published_date": "1813-01-28",
        "page_count": 279,
        "language": "English"
    },
    {
        "id": 8,
        "title": "The Brothers Karamazov",
        "author": "Fyodor Dostoevsky",
        "publisher": "The Russian Messenger",
        "published_date": "1880-11-01",
        "page_count": 796,
        "language": "Russian"
    },
    {
        "id": 9,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "publisher": "HarperOne",
        "published_date": "1988-05-01",
        "page_count": 208,
        "language": "Portuguese"
    },
    {
        "id": 10,
        "title": "Moby Dick",
        "author": "Herman Melville",
        "publisher": "Richard Bentley",
        "published_date": "1851-10-18",
        "page_count": 585,
        "language": "English"
    }
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

@app.get("/books", response_model=List[Book])
def get_all_books():
    return books

@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()

    books.append(new_book)

    return new_book


@app.get("/book/{book_id}")
def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")


@app.patch("/book/{book_id}")
def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language

            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")


@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)

            return None
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")