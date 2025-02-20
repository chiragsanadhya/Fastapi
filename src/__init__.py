from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)


#the lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):    
    print("Server is starting...")
    await init_db()
    print("server is stopping")



app = FastAPI(
    lifespan=lifespan # add the lifespan event to our application
)

app.include_router(
    book_router,
    prefix="/books",
    tags=['books']
)