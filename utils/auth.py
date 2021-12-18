import jwt
import os

def generate_token() -> str:
    secret = os.environ.get('JWT_SECRET')
    token = jwt.encode({"exp": 1371720939}, secret, algorithm='HS256')
    return token