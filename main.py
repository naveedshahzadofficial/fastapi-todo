from typing import List
from fastapi import FastAPI
import schemas
app = FastAPI()

@app.get("/todos", response_model=List[schemas.TodoResponse])
async def list():
  return [
        {'id': 1, 'user_id': 1, 'completed': False, 'title': 'This is title 1'},
        {'id': 2, 'user_id': 1, 'completed': False, 'title': 'This is title 2'}
    ]

@app.post('/todos')
async def create(request: schemas.TodoRequest):
  return request

@app.get('/todos/{id}', response_model = schemas.TodoResponse)
async def show(id: int):
  return {'id': 1, 'user_id': 1, 'completed': False, 'title': 'This is title 1'}

@app.put('/todos/{id}')
async def update(id: int, request: schemas.TodoRequest):
  return request

@app.delete('/todos/{id}')
async def delete(id: int):
  return id