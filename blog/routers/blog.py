from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from blog import schemas, database, models, oauth
from sqlalchemy.orm import Session
from blog.repository import blog

router = APIRouter(
    tags = ['Blogs']

)
get_db = database.get_db

@router.get('/blog', response_model = List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth.get_current_user)):
    return blog.get_all(db)

@router.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth.get_current_user)):
    return blog.create(request, db)

@router.delete('/blog/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth.get_current_user)):
    return destroy(id, db)

@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth.get_current_user)):
    return blog.update(id, request, db)

@router.get('/blog/{id}', status_code=200, response_model = schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth.get_current_user)):
    return blog.show(id, db)