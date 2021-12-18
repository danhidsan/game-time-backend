import bcrypt

def generate_password(password: str):
    password_hash = bcrypt.hashpw(password, bcrypt.gensalt(12))
    return password_hash

def check_password(password: str, hash: str):
    is_match = bcrypt.checkpw(password, hash)
    return is_match