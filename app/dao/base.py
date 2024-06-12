from sqlalchemy import insert, select
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker
from app.logger import logger


class BaseDAO:
    model = None

    @classmethod
    async def get_user_by_id(cls, model_id: int):
        try:
            async with async_session_maker() as session:
                query = select(cls.model.__table__.columns).filter_by(user_id=model_id)
                result = await session.execute(query)
                return result.first()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = 'Database Exception'
            elif isinstance(e, Exception):
                msg = 'Unknown Exception'
            msg += ': Cannot get user by id'
            extra = {'model_id': model_id}
            logger.error(msg, extra=extra, exc_info=True)

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        try:
            async with async_session_maker() as session:
                query = select(cls.model.__table__.columns).filter_by(**filter_by)
                result = await session.execute(query)
                return result.scalar_one_or_none()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = 'Database Exception'
            elif isinstance(e, Exception):
                msg = 'Unknown Exception'
            msg += ': Cannot find user'
            extra = {'filter_by': filter_by}
            logger.error(msg, extra=extra, exc_info=True)

    @classmethod
    async def get_all_users(cls):
        try:
            async with async_session_maker() as session:
                query = select(cls.model.__table__.columns)
                result = await session.execute(query)
                return result.mappings().all()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = 'Database Exception'
            elif isinstance(e, Exception):
                msg = 'Unknown Exception'
            msg += ': Cannot get all users'
            logger.error(msg, exc_info=True)

    @classmethod
    async def add_user(cls, **data):
        try:
            async with async_session_maker() as session:
                query = insert(cls.model).values(**data)
                await session.execute(query)
                await session.commit()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = 'Database Exception'
            elif isinstance(e, Exception):
                msg = 'Unknown Exception'
            msg += ': Cannot add user'
            extra = {'data': data}
            logger.error(msg, extra=extra, exc_info=True)
