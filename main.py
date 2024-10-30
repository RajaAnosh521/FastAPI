from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI() 

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {}              


@app.get("/get-item/{item_id}") 
def get_item(item_id: int = Path(..., description="The id of the item you like to give..")): 
    return inventory[item_id] 


@app.get("/get-by-name/{item_id}") 
def get_item(*, name: Optional[str] = None, test = None, item_id: int):   
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id] 
    return {"data": "Not found"} 


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item): 
    if item_id in inventory:
        return {"Error": "Item already exists."} 
    inventory[item_id] = item             
    return inventory[item_id] 


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if not item_id in inventory:
        return {"Error": "Item does not already exists..."} 

    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand 
    
    return inventory[item_id] 


@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        return {"Error": "id does not exist..."} 
    
    del inventory[item_id] 
    return {"msg": "Deleted successfully..."} 