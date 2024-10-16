from pydantic import BaseModel, EmailStr

class Response(BaseModel):
    name: str
    email: EmailStr
    description: str

