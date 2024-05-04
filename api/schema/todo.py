from pydantic import BaseModel, Field
from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator
from api.model.todo import Todo

#Creating model
GetTodo = pydantic_model_creator(None, name="Todo")


"""
This model defines the structure for creating a new todo item. Here's what each part does:

Post/Put-Todo: This is the name of the Pydantic model.
BaseModel: This indicates that PostTodo & PutTodo inherits from Pydantic's BaseModel, making it a Pydantic model.
task: str: This defines a field named task of type str. It's required for creating a new todo item.
    - Optional[str] : optional for updating the todo item
done: bool: This defines a field named done of type bool. It indicates whether the todo item is completed or not.
    - Optional[bool] : optional for updating the todo item-
Field(..., max_length=100): This defines additional validation constraints for the task field. The max_length parameter 
specifies that the length of the task string cannot exceed 100 characters.
"""
class PostTodo(BaseModel):
    task: str = Field(..., max_length=100)
    done: bool


class PutTodo(BaseModel):
    task: Optional[str] = Field(None, max_length=100)
    done: Optional[bool]
