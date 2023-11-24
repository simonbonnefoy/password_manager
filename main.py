from fastapi import Depends, FastAPI, HTTPException
import uvicorn
from sqlalchemy.orm import Session

from password_manager.password import crud, models, schemas
from password_manager.database.database import get_db
from password_manager.database.database import engine, SessionLocal

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# def get_db() -> SessionLocal:
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@app.post("/passwords/", response_model=schemas.Password)
def create_password_entry(password: schemas.PasswordBase, db: Session = Depends(get_db)):
    db_password = crud.get_password(db, title=password.title)
    if db_password:
        raise HTTPException(status_code=400, detail="Password entry already registered")
    db_password = crud.create_password_entry(db=db, password=password)
    return db_password


@app.put("/passwords/{password_id}", response_model=schemas.Password)
def patch_password_entry(password_id: int, password: schemas.PasswordBase, db: Session = Depends(get_db)):
    update_data = password.model_dump(exclude_unset=True)
    updated_entry = crud.update_password(db, password_id, update_data)
    return updated_entry


@app.get("/passwords/", response_model=list[schemas.Password])
def get_passwords(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    passwords = crud.get_passwords(db, skip=skip, limit=limit)
    return passwords


@app.get("/passwords/ids/{password_id}", response_model=schemas.Password)
def get_password_by_id(password_id: int, db: Session = Depends(get_db)):
    password = crud.get_password_by_id(db, password_id)
    return password


@app.get("/passwords/titles/{password_title}", response_model=list[schemas.Password])
def get_password_by_id(password_title: str, db: Session = Depends(get_db)):
    passwords = crud.get_passwords_by_title(db, password_title)
    return passwords


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
