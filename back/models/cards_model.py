from pydantic import BaseModel
from typing import Optional


class cardModel(BaseModel):
    name: str
    lastName: str 
    email: str
    company: int
    postName: str
    socialNetwork1: str
    socialNetwork2: str
    socialNetwork3: str
    about: str
    photo: str
    phone: str
    wa: str
    areaCode: str

class deleteModel(BaseModel):
    email: str

class updateModel(BaseModel):
    name: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    company: Optional[str] = None
    postName: Optional[str] = None
    socialNetwork1: Optional[str] = None
    socialNetwork2: Optional[str] = None
    socialNetwork3: Optional[str] = None
    about: Optional[str] = None
    photo: Optional[str] = None
    phone: Optional[str] = None
    wa: Optional[str] = None
    areaCode: Optional[str] = None