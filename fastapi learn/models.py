from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    name : str =  Field(min_length = 3)
    price : float = Field(gt = 0)
    is_offer : bool 
    description : Optional[str] = None