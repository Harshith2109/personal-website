from sqlalchemy import Column, Integer, String
from database.database import Base

class Responses(Base):
    __tablename__ = "Responses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, nullable=False, index=True)
    description = Column(String)
