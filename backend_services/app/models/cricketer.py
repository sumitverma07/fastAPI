from sqlalchemy import Column,String,Integer,Boolean
from app.database import Base

class Cricketer(Base):
    __tablename__='cricketer'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    role=Column(Integer)
    is_retired=Column(Boolean,default=False)