from typing import List
from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models
from config.database import engine, get_db
from schemas import TodoRequest, TodoResponse

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.get("/todos", response_model=List[TodoResponse])
async def all(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()


@app.post('/todos', status_code=status.HTTP_201_CREATED, response_model=TodoResponse)
async def create(request: TodoRequest, db: Session = Depends(get_db)):
    new_todo = models.Todo(title=request.title, completed=request.completed)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@app.get('/todos/{id}', status_code=status.HTTP_200_OK, response_model=TodoResponse)
async def show(id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"todo with id {id} not found.")

    return todo


@app.put('/todos/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=TodoResponse)
def update(id: int, request: TodoRequest, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id)
    if not todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"todo with id {id} not found.")
    todo.update(dict(request), synchronize_session=False)
    db.commit()
    return todo.first()


@app.delete('/todos/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id)
    if not todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"todo with id {id} not found.")

    todo.delete(synchronize_session=False)
    db.commit()
    return 'done'
