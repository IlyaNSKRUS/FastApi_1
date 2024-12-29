from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import ORM_OBJECT, ORM_CLS, Advertisement
from sqlalchemy.exc import IntegrityError


async def add_item(session: AsyncSession, item: ORM_OBJECT):
    session.add(item)
    try:
        await session.commit()
    except IntegrityError as err:
        if err.orig.pgcode == '23505':
            raise HTTPException(status_code=409, detail='Item already exist')
        raise err


async def get_item(session: AsyncSession, orm_cls: ORM_CLS, item_id: int) -> ORM_OBJECT:
    orm_obj = await session.get(orm_cls, item_id)
    if orm_obj is None:
        raise HTTPException(status_code=404, detail='item not found')
    return orm_obj

async def get_item_qs(session: AsyncSession, orm_cls: ORM_CLS, item_qs: str) -> ORM_OBJECT:
    result = select(orm_cls).where(orm_cls.heading.ilike(f'%{item_qs}%'))
    user = await session.scalars(result)
    user = user.first()
    return user


async def delete_item(session: AsyncSession, orm_cls: ORM_CLS, item_id: int):
    orm_obj = await get_item(session, orm_cls, item_id)
    await session.delete(orm_obj)
    await session.commit()










