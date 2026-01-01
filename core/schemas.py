from pydantic import BaseModel, Field, field_validator



class CustomerSchema(BaseModel):
    full_name : str
    phone_number : str = Field(pattern=r"^\d{11}$")