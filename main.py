from fastapi import FastAPI
from model import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

#Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

#Get one todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"todo": "No todos found"}

#Create a Todo
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo Added"}

#Update a Todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, data: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = data.id
            todo.item = data.item
            return {"Updated todo": todo}
    return {"todo": "No todo found"}

#Delete a Todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"todo": "Todo Deleted"}
    return {"todo": "No todo found"}
