from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine

from handlers import user_handler, post_handler

DB_URL = "postgresql+psycopg2://postgres:password@db/postgres"

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_engine(DB_URL)
    app.state.db = engine
    try:
        yield
    finally:
        engine.dispose()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_handler.router)
app.include_router(post_handler.router)

@app.get("/")
def read_root():
    """
    Returns the API version
    """
    return {"API Version": "1.2.0"}
