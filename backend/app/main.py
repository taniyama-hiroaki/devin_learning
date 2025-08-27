from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uuid
from datetime import datetime

app = FastAPI()

# Disable CORS. Do not remove this for full-stack development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

todos_storage: List[dict] = []

class TodoCreate(BaseModel):
    text: str

class Todo(BaseModel):
    id: str
    text: str
    createdAt: str

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/todos", response_model=List[Todo])
async def get_todos():
    return todos_storage

@app.post("/todos", response_model=Todo)
async def create_todo(todo: TodoCreate):
    new_todo = {
        "id": str(uuid.uuid4()),
        "text": todo.text,
        "createdAt": datetime.now().isoformat()
    }
    todos_storage.append(new_todo)
    return new_todo
