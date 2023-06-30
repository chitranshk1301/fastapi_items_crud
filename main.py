from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# In-memory storage for items
items = []


# Model for item data
class Item(BaseModel):
    id: int
    name: str
    price: float
    quantity: int


# Routes for item manipulation
@app.get("/items")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}


@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for i, existing_item in enumerate(items):
        if existing_item.id == item_id:
            items[i] = item
            return item
    return {"error": "Item not found"}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, item in enumerate(items):
        if item.id == item_id:
            deleted_item = items.pop(i)
            return deleted_item
    return {"error": "Item not found"}


# API to manage inventory
@app.post("/inventory")
def manage_inventory(items_data: dict):
    for item_id, quantity in items_data.items():
        for item in items:
            if item.id == int(item_id):
                item.quantity += quantity
    return {"message": "Inventory updated successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
