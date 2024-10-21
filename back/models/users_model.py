from pydantic import BaseModel

class usersModel(BaseModel):
    name: str
    lastName: str 
    email: str
    company: int
    password: str
    status: int
  
class consultModel(BaseModel):
    email: str
    password: str
    