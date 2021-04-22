from fastapi import APIRouter, Depends, status, HTTPException
from blog import database, schemas, models
from sqlalchemy.orm import Session
from blog.repository import user

router = APIRouter(
    tags = ['Users']
)
get_db = database.get_db



@router.post('/user', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/user/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
   return user.show(id, db)