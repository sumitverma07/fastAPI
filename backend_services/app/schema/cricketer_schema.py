from pydantic import BaseModel
from typing import Union
class Cricketer(BaseModel):
    name:str
    role:str
    is_retired:Union[bool]

class CricketerCreate(Cricketer):
    pass

class CricketerGet(Cricketer):
    id:int
    class Config:
        from_attributes=True