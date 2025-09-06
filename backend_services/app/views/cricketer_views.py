from sqlalchemy.orm import Session
from app.models.cricketer import Cricketer
from app.schema.cricketer_schema import CricketerGet,CricketerCreate
def get_cricketers(db:Session):
    data=db.query(Cricketer).all()
    return data

def create_cricketer(db:Session,schema:CricketerCreate):
    cric=Cricketer(**schema.dict())
    print('crick is',cric.name)
    db.add(cric)
    db.commit()
    db.refresh(cric)
    return cric

def update_cricketer(db:Session,schema:CricketerCreate,cr_id:int):
    update_cric=db.query(Cricketer).filter(Cricketer.id==cr_id).first()
    print('update is',update_cric)
    if update_cric:
        update_cric.name=schema.name
        update_cric.role=schema.role
        update_cric.is_retired=schema.is_retired
        db.commit()
        return update_cric
    
def delete_cricketer(db:Session,cric_id:int):
    delete_cric=db.query(Cricketer).filter(Cricketer.id==cric_id).first()
    if delete_cric:
        db.delete(delete_cric)
        db.commit()
        return delete_cric
