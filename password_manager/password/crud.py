from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import update
from fastapi import Depends, FastAPI, HTTPException
from password_manager.password import models, schemas
from password_manager.database.database import engine, SessionLocal



def get_passwords(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Password).offset(skip).limit(limit).all()



def get_password(db: Session, title: str):
    results = db.query(models.Password).filter(models.Password.title == title).first()
    return results


def get_password_by_id(db: Session, password_id: int) -> models.Password:
    return db.query(models.Password).filter(models.Password.id == password_id).first()


def get_passwords_by_title(db: Session, password_title: str):
    return db.query(models.Password).filter(models.Password.title.contains(password_title)).all()


def update_password(db: Session, password_id: int, password_update: dict) -> models.Password:
    statement = update(models.Password).where(models.Password.id == password_id).values(**password_update)
    db.execute(statement)
    db.commit()
    return db.query(models.Password).filter(models.Password.id == password_id).first()


def create_password_entry(db: Session, password: schemas.PasswordCreate):
    db_password = models.Password(title=password.title,
                                  username=password.username,
                                  email=password.email,
                                  password=password.password,
                                  notes=password.notes,
                                  last_modified=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    db.add(db_password)
    db.commit()
    db.refresh(db_password)
    return db_password

# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()
#
#
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()

# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
