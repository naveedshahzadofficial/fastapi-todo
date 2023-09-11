from pydantic import BaseModel

class TodoRequest(BaseModel):
   title: str
   completed: bool = False

class TodoResponse(TodoRequest):
  id: int
  user_id: int

  class Config():
        orm_mode = True