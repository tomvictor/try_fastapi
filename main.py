from enum import Enum

from fastapi import FastAPI, WebSocket
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

from data import html

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    """API for user

    Notes:
        Example API
    Returns:

    """
    return {"user_id": "the current user test"}



@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


#Enumberations

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "alex"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "alex":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

#Query params

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

#Optional query params

@app.get("/items/optional/{item_id}")
async def read_optional_item(
    item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# Multi path params


# example.com/users/1/items/1

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# Required query parameters

@app.get("/items/required/{item_id}")
async def read_required_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/model-item/")
async def create_item(item: Item):
    item_dict = item.dict()
    print(item_dict)
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict



@app.get("/chat")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")