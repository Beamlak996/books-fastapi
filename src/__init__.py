from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_sapn(app: FastAPI):
    print("Server is starting...")
    await init_db()
    yield
    print("Server has been stopped")

version = 'v1'

app = FastAPI(
    title = "Books",
    description = 'A REST_API for book reviews.',
    version = version,
    lifespan=life_sapn
)


app.include_router(book_router, prefix=f"/api/{version}/books")