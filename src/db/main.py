# # Inside src/db/main.py
# from sqlmodel import create_engine, text
# from sqlalchemy.ext.asyncio import AsyncEngine
# from src.config import config
# from sqlmodel import SQLModel
# from src.books.models import Book
# from sqlalchemy.ext.asyncio import create_async_engine

# engine = AsyncEngine(create_engine(
#     url=config.DATABASE_URL,
#     echo=True
# ))

# DATABASE_URL = "postgresql://neon-1_owner:npg_TJj6wacxW2tk@ep-green-sky-a8yjg2ix-pooler.eastus2.azure.neon.tech/neon-1?sslmode=require"

# engine = create_async_engine(
#     DATABASE_URL,
#     echo=True
# )
# async def initdb():
#     """create our database models in the database"""

#     async with engine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.create_all)





# Inside src/db/main.py
from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import config
from sqlmodel import SQLModel
from src.books.models import Book
from sqlalchemy.ext.asyncio import create_async_engine

engine = AsyncEngine(create_engine(
    url=config.DATABASE_URL,
    echo=True
))

DATABASE_URL = "postgresql://neon-1_owner:npg_TJj6wacxW2tk@ep-green-sky-a8yjg2ix-pooler.eastus2.azure.neon.tech/neon-1?sslmode=require"

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)
async def initdb():
    """create our database models in the database"""

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)