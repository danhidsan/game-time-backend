from extensions import db
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
