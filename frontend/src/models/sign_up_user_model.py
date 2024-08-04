from pydantic import BaseModel, EmailStr, Field

class SignUpModel(BaseModel):
    username: str = Field(..., min_length=1)
    email: EmailStr
    password: str