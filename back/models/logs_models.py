from pydantic import BaseModel

class logsModel(BaseModel):
    email: str
    table: str
    change: str