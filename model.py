from pydantic import BaseModel

class body(BaseModel):
    price: float
    vat: float
    amount: int