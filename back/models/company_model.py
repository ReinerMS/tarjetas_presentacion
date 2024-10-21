from pydantic import BaseModel

class Company(BaseModel):
    img: str
    name: str