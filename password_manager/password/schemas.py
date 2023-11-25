from pydantic import BaseModel


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

    class Config:
        orm_mode = True


