from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.views.cricketer_views import (
    get_cricketers,
    create_cricketer,
    update_cricketer,
    delete_cricketer
)
from app.schema.cricketer_schema import (
    CricketerGet, 
    CricketerCreate
)
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


routes = APIRouter()


@routes.get('/get', response_model=list[CricketerGet])
def get_cricketer(db: Session = Depends(get_db)):
    return get_cricketers(db)


@routes.post('/create', response_model=CricketerGet)
def create(schema: CricketerCreate, db: Session = Depends(get_db)):
    data = create_cricketer(db, schema)
    if not data:
        return HTTPException(detail='no found', status_code=400)
    return data


@routes.put('/update/{cric_id}', response_model=CricketerGet)
def update(cric_id: int, schema: CricketerCreate, db: Session = Depends(get_db)):
    res = update_cricketer(db, schema, cric_id)
    if not res:
        return HTTPException('id is not exist', detail=404)
    return res


@routes.delete('/delete/{cric_id}')
def delete(cric_id: int, db: Session = Depends(get_db)):
    res = delete_cricketer(db, cric_id)
    if not res:
        return HTTPException('id is not exist', detail=404)
    return res
