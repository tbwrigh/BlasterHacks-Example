from contextlib import asynccontextmanager

from fastapi import FastAPI

from sqlalchemy import create_engine

DB_URL = "sqlite:///./app.db"

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_engine(DB_URL)
    app.state.db = engine
    try:
        yield
    finally:
        engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    """
    Returns the API version
    """
    return {"API Version": "1.2.0"}
