from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def idk():
    return {"Poopy": "bumbum"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    """
    Write get script and specify data structure to expect
    
    :param item_id: Description
    :type item_id: int
    :param q: Description
    :type q: Union[str, None]
    """

    return {"item_id": item_id, "q": q}

@app.post("/items/")
def write_item(item_id: int, q: Union[str, None] = None):
    """
    Just write post script here and specify data structure to expect
    
    :param item_id: Description
    :type item_id: int
    :param q: Description
    :type q: Union[str, None]
    """

    return None