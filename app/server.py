
from fastapi import FastAPI
from lifespan import lifespan
from dependency import SessionDependency
import crud
import schema
import models

app = FastAPI(
    title='Advertisement',
    version='0.1',
    description='Сервис объявлений',
    lifespan=lifespan
)


@app.post('/v1/adv', response_model=schema.CreateAdvertisementResponse)
async def create_adv(session: SessionDependency,
                      create_adv_request: schema.CreateAdvertisementRequest):
    create_adv_dict = create_adv_request.dict()
    adv = models.Advertisement(**create_adv_dict)
    await crud.add_item(session, adv)
    return adv.id_dict


@app.get('/v1/adv/{adv_id}', response_model=schema.GetAdvertisementResponse)
async def get_adv(adv_id: int, session: SessionDependency):
    adv = await crud.get_item(session, models.Advertisement, adv_id)
    return adv.dict


@app.get('/v1/adv', response_model=schema.GetAdvertisementResponse)
async def get_adv(heading: str, session: SessionDependency):
    qs = heading
    adv = await crud.get_item_qs(session, models.Advertisement, qs)
    return adv.dict



@app.patch('/v1/adv/{adv_id}', response_model=schema.UpdateAdvertisementResponse)
async def update_adv(update_adv_request: schema.UpdateAdvertisementRequest,
                      adv_id: int, session: SessionDependency):
    adv = await crud.get_item(session, models.Advertisement, adv_id)
    adv_dict = update_adv_request.dict(exclude_none=True)
    for field, value in adv_dict.items():
        setattr(adv, field, value)
    await crud.add_item(session, adv)
    return adv.dict


@app.delete('/v1/adv/{adv_id}', response_model=schema.DeleteAdvertisementResponse)
async def delete_adv(adv_id: int, session: SessionDependency):
    await crud.delete_item(session, models.Advertisement, adv_id)
    return {'status': 'success'}


@app.post('/v1/user', response_model=schema.CreateUserResponse)
async def create_user(session: SessionDependency,
                      create_user_request: schema.CreateUserRequest):
    print(create_user_request)
    create_user_dict = create_user_request.dict()
    user = models.User(**create_user_dict)
    await crud.add_item(session, user)
    print(user.dict)
    return user.dict















