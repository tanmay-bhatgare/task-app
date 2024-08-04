from pydantic import BaseModel, EmailStr

class SignInModel(BaseModel):
    username: EmailStr
    password: str