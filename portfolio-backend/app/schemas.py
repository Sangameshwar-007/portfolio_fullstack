from pydantic import BaseModel
from typing import Optional

# Project Schemas
class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    image_url: Optional[str] = None

class ProjectResponse(ProjectBase):
    id: int
    class Config:
        from_attributes = True

# Skill Schemas
class SkillBase(BaseModel):
    skill_name: str
    percentage: int

class SkillResponse(SkillBase):
    id: int
    class Config:
        from_attributes = True

# About Schemas
class AboutBase(BaseModel):
    description: str
    email: str

class AboutResponse(AboutBase):
    id: int
    class Config:
        from_attributes = True

# Contact Schemas
class ContactBase(BaseModel):
    name: str
    email: str
    subject: str
    message: str

class ContactResponse(ContactBase):
    id: int
    class Config:
        from_attributes = True
