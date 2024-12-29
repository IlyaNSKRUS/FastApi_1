import datetime
from typing import Literal
from pydantic import BaseModel


class IdResponse(BaseModel):
    id: int


class Status(BaseModel):
    status: Literal['success']


class CreateAdvertisementRequest(BaseModel):
    heading: str
    description: str
    price: float
    creator: int



class CreateAdvertisementResponse(IdResponse):
    pass


class GetAdvertisementResponse(BaseModel):
    id: int
    heading: str
    description: str
    price: float
    creator: int
    date_creation: datetime.date


class UpdateAdvertisementRequest(BaseModel):
    heading: str | None = None
    description: str | None = None
    price: float | None = None


class UpdateAdvertisementResponse(IdResponse):
    id: int
    heading: str
    description: str
    price: float
    creator: int
    date_creation: datetime.date

class DeleteAdvertisementResponse(Status):
    pass


class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str

class CreateUserResponse(BaseModel):
    id: int
    name: str
    email: str
    password: str






