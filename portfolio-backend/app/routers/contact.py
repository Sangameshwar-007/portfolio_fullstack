from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/contact", tags=["Contact"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ContactResponse)
def create_message(data: schemas.ContactBase, db: Session = Depends(get_db)):
    message = models.ContactMessage(**data.dict())
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

@router.get("/", response_model=list[schemas.ContactResponse])
def get_messages(db: Session = Depends(get_db)):
    return db.query(models.ContactMessage).all()

@router.delete("/{id}")
def delete_message(id: int, db: Session = Depends(get_db)):
    message = db.query(models.ContactMessage).filter(models.ContactMessage.id == id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    
    db.delete(message)
    db.commit()
    return {"message": "Deleted"}