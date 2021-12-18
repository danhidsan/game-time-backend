from extensions import db
from utils.hash import check_password
from utils.auth import generate_token
from models.user import User


def create_user(user_input: dict) -> User:
    try:
        user = User(username=user_input['username'], email=user_input['email'])
        user.set_password(user_input['password'].encode('utf-8'))

        db.session.add(user)
        db.session.commit()

        return user
    except Exception as e:
        print('An exception ocurrend on create_user')
        print(e)

def update_user(user_id: int, user_input: dict) -> User:
    try:
        user = User.query.get(user_id)

        if 'username' in user_input:
            user.username = user_input['username']
        if 'email' in user_input:
            user.email = user_input['email']
        
        db.session.add(user)
        db.session.commit()

        return user
    except Exception as e:
        print('An exception ocurred on update_user')
        print(e)

def login(login_input: dict):
    try:
        user = User.query.filter_by(email=login_input['email']).first()
        if not user:
            return None, None

        user_hash = user.password
        is_match = check_password(login_input['password'].encode('utf-8'), user_hash.encode('utf-8'))

        if is_match:
            token = generate_token()
            return token, user
        
        return None, None
    except Exception as e:
        print('An exception ocurrend on create_user')
        print(e)
        return None, None
