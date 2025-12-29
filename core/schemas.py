from pydantic import BaseModel, Field, field_validator



class PriceCreateSchema(BaseModel):
    page : str = Field(max_length=20)
    price : float

    @field_validator("price")
    def validate_price(price):
        if price < 0:
            raise ValueError("Price can't be negative.")
        return price
    

class PriceUpdateSchema(BaseModel):
    id : int
    price : float

    @field_validator("price")
    def validate_price(price):
        if price < 0:
            raise ValueError("Price can't be negative.")
        return price


class PriceResponseSchema(BaseModel):
    id : int
    page : str
    price : float