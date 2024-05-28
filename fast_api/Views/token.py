from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def create_access_token(data: dict):
    return "fake_access_token"

# Dummy function to hash passwords
def hash_password(password: str):
    return pwd_context.hash(password)
