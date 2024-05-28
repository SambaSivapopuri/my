from pydantic import BaseModel, EmailStr
from fastapi import HTTPException
from passlib.context import CryptContext
from db.db import db
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    password: str

# class UserLogin(BaseModel):
#     username: str
#     password: str

# class User(BaseModel):
#     username: str
#     email: EmailStr
# class UserModel:
    
#     @classmethod
#     def save(cls, user_data):
#         db.user.insert_one(user_data)
    
#     @classmethod
#     def find_by_username(cls, username):
#         return db.user.find_one({"username": username})

#     @classmethod
#     def find_by_email(cls, email):
#         return db.user.find_one({"email": email})

#     @classmethod
#     def verify_password(cls, plain_password, hashed_password):
#         return pwd_context.verify(plain_password, hashed_password)


class User:
    def __init__(self, **kwargs) :
        self.data=kwargs
    def save(self):
        db.user.insert_one(self.data)
    @classmethod
    def findall(self):
        return db.user.find()
    @classmethod
    def data_filter(self,**data):
        if data:
            return db.user.find_one(data)
        return {"data":" Check Input value or validations"}
    @classmethod
    def register_user(cls, username, email, password):
        # Check if user already exists
        if cls.data_filter(username=username):
            raise HTTPException(status_code=400, detail="Username already exists")

        # Check if email already exists
        if cls.data_filter(email=email):
            raise HTTPException(status_code=400, detail="Email already exists")

        # Create a new user object
        new_user = cls(username=username, email=email, password=password)

        # Save the new user to the database
        new_user.save()

        return {"message": "User registered successfully"}