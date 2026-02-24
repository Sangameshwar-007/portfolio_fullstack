from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(500))
    image_url = Column(String(255))

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    skill_name = Column(String(100), index=True)
    percentage = Column(Integer)

class About(Base):
    __tablename__ = "about"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text)
    email = Column(String(255))

class ContactMessage(Base):
    __tablename__ = "contact_messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    subject = Column(String(255))
    message = Column(Text)
