from pydantic import BaseModel
from datetime import datetime


class PasswordBase(BaseModel):
    title: str
    username: str
    email: str
    password: str
    notes: str


class PasswordCreate(PasswordBase):
    last_modified: str
    pass


class Password(PasswordCreate):
    id: int
    # password_id: int

    class Config:
        orm_mode = True


# class UserBase(BaseModel):
#     email: str
#
#
# class UserCreate(UserBase):
#     password: str
#
#
# class User(UserBase):
#     id: int
#     is_active: bool
#
#     class Config:
#         orm_mode = True
