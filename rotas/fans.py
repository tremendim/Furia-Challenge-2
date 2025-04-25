from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
import models, schemas

router = APIRouter(prefix="/fans", tags=["Fans"])

@router.post("/", response_model=schemas.Fan)
def create_fan(fan: schemas.FanCreate, db: Session = Depends(get_db)):
    db_fan = models.Fan(**fan.dict())
    db.add(db_fan)
    db.commit()
    db.refresh(db_fan)
    return db_fan

@router.get("/", response_model=List[schemas.Fan])
def read_fans(db: Session = Depends(get_db)):
    return db.query(models.Fan).all()