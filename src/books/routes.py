from fastapi import APIRouter, status, HTTPException
from typing import List
from src.books.book_data import books
from src.books.schemas import BookUpdateModel, Book

book_router = APIRouter()

@book_router.get("/", response_model=List[Book])
def get_all_books():
    return books

@book_router.post("/", status_code=status.HTTP_201_CREATED)
def create_a_book(book_data: Book) -> dict:
    new_book = book_data.dict()  # Using dict() for Pydantic models
    books.append(new_book)
    return new_book

@book_router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")

@book_router.patch("/{book_id}", response_model=Book)
def update_book(book_id: int, book_update_data: BookUpdateModel):
    for book in books:
        if book['id'] == book_id:
            book.update(book_update_data.dict(exclude_unset=True))  # Update only fields that are provided
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")

@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")
