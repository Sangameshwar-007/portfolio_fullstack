from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/skills", tags=["Skills"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.SkillResponse)
def create_skill(data: schemas.SkillBase, db: Session = Depends(get_db)):
    skill = models.Skill(**data.dict())
    db.add(skill)
    db.commit()
    db.refresh(skill)
    return skill

@router.get("/", response_model=list[schemas.SkillResponse])
def get_skills(db: Session = Depends(get_db)):
    return db.query(models.Skill).all()

@router.put("/{id}", response_model=schemas.SkillResponse)
def update_skill(id: int, data: schemas.SkillBase, db: Session = Depends(get_db)):
    skill = db.query(models.Skill).filter(models.Skill.id == id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    
    for key, value in data.dict().items():
        setattr(skill, key, value)
    
    db.commit()
    db.refresh(skill)
    return skill

@router.delete("/{id}")
def delete_skill(id: int, db: Session = Depends(get_db)):
    skill = db.query(models.Skill).filter(models.Skill.id == id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    
    db.delete(skill)
    db.commit()
    return {"message": "Deleted"}