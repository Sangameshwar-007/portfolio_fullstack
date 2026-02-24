from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import projects, contact, about, skills
from app.database import engine, Base

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Portfolio API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(projects.router)
app.include_router(contact.router)
app.include_router(about.router)
app.include_router(skills.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Portfolio API"}