from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import update
from password_manager.password import models, schemas


def get_passwords(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Password).offset(skip).limit(limit).all()


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

