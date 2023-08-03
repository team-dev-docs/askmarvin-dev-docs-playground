
python
from datetime import datetime
from pydantic import BaseModel, Field
from marvin import AIApplication
create models to represent the state of our ToDo app
class ToDo(BaseModel):
    title: str
    description: str = None
    due_date: datetime = None
    done: bool = False
class ToDoState(BaseModel):
    todos: list[ToDo] = []
create the app with an initial state and description
todo_app = AIApplication(
    state=ToDoState(),
    description=(
        "A simple todo app. Users will provide instructions for creating and updating"
        " their todo lists."
    ),
)
