from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine
from schema.schema import Response
from models.models import Base
from crud.crud import create_item, view
from fastapi.middleware.cors import CORSMiddleware


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [

    "https://hashith.info",
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"Server up"}

@app.post("/contacts/")
def addRespone(item: Response, db: Session = Depends(get_db)):

    return create_item(db=db, item=item)


@app.get("/contacts_details/")
def addRespone(db: Session = Depends(get_db)):
    return view(db=db)





