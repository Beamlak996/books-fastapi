from fastapi import FastAPI
from src.books.routes import book_router

version = 'v1'

app = FastAPI(
    title = "Books",
    description = 'A REST_API for book reviews.',
    version = version,
)


app.include_router(book_router, prefix=f"/api/{version}/books")