from fastapi import APIRouter, Depends, HTTPException, status, Request
from Models.user import User,UserRegistration
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from db.db import db
app=APIRouter(prefix="/user")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "PPA@CHRUN"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

@app.post("/register/", response_model=User)
async def register_user(user:User):
    # Check if username or email already exists
    # if db["user"].find_by_username(user.username):
    #     raise HTTPException(status_code=400, detail="Username already registered")
    # if UserModel.find_by_email(user.email):
    #     raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
    # hashed_password = pwd_context.hash(user.password)
    data=db["user"].find_one({"username":user.username})
    for i in await data:
        print(i.name)
    # Save the user to the database
    UserModel.save({
        "username": user.username,
        "email": user.email,
        # "password": hashed_password
    })

    return {"username": user.username, "email": user.email}

# Route to generate JWT token
# @app.post("/token")
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = UserModel.find_by_username(form_data.username)
#     if not user or not UserModel.verify_password(form_data.password, user["password"]):
#         raise HTTPException(status_code=401, detail="Incorrect username or password")

#     # Generate JWT token
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = jwt.encode({"sub": user["username"], "exp": datetime.utcnow() + access_token_expires}, SECRET_KEY, algorithm=ALGORITHM)
#     return {"access_token": access_token, "token_type": "bearer"}

# # Protected route
# @app.get("/protected_route/")
# async def protected_route(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username = payload.get("sub")
#         if not username:
#             raise HTTPException(status_code=401, detail="Invalid token")
#         return {"username": username}
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=401, detail="Token has expired")
#     except jwt.JWTError:
#         raise HTTPException(status_code=401, detail="Could not validate token")
