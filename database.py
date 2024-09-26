import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

from models import Users

engine = create_async_engine("sqlite+aiosqlite:///async_db_test.db", echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    pass

async def create_table(engine) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()


async def insert_objects(async_session: async_sessionmaker[AsyncSession], name, surname) -> None:
    async with async_session() as session:
        async with session.begin():
            session.add_all(
                [
                    Users(name=name, surname=surname)
                ]
            )


async def select_objects(async_session: async_sessionmaker[AsyncSession]) -> str:
    async with async_session() as session:
        stmt = select(Users)
        result = await session.execute(stmt)
        return_result = ""

        for user in result.scalars():
            return_result = return_result + f"{user.id}. {user.name} {user.surname}\n"
            print(user.id, user.name, user.surname)
        return return_result
