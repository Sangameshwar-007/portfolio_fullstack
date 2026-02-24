from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/about", tags=["About"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.AboutResponse)
def create_about(data: schemas.AboutBase, db: Session = Depends(get_db)):
    about = models.About(**data.dict())
    db.add(about)
    db.commit()
    db.refresh(about)
    return about

@router.get("/", response_model=list[schemas.AboutResponse])
def get_about(db: Session = Depends(get_db)):
    return db.query(models.About).all()

@router.put("/{id}", response_model=schemas.AboutResponse)
def update_about(id: int, data: schemas.AboutBase, db: Session = Depends(get_db)):
    about = db.query(models.About).filter(models.About.id == id).first()
    if not about:
        raise HTTPException(status_code=404, detail="About not found")
    
    for key, value in data.dict().items():
        setattr(about, key, value)
    
    db.commit()
    db.refresh(about)
    return about

@router.delete("/{id}")
def delete_about(id: int, db: Session = Depends(get_db)):
    about = db.query(models.About).filter(models.About.id == id).first()
    if not about:
        raise HTTPException(status_code=404, detail="About not found")
    
    db.delete(about)
    db.commit()
    return {"message": "Deleted"}