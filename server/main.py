from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/test")
async def idk():
    return {"Poopy": "bumbum"}

@app.get("/count")
async def return_count():
    return {"count" : 5}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    """
    Write get script and specify data structure to expect
    
    :param item_id: Description
    :type item_id: int
    :param q: Description
    :type q: Union[str, None]
    """

    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def write_item(item_id: int, q: Union[str, None] = None):
    """
    Just write post script here and specify data structure to expect
    
    :param item_id: Description
    :type item_id: int
    :param q: Description
    :type q: Union[str, None]
    """

    return None