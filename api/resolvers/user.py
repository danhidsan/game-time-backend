from domain.user import create_user, update_user, login

""" Query resolvers """

def resolve_user(obj, info, id=None):
    return {
        "email": "email 1",
        "username": "username 1",
    }

""" Mutation resolvers """

def resolve_login(*_, input):
    token, user = login(login_input=input)
    if not user and not token:
        return {}
    return {
        "token": token,
        "user": {
            "email": user.email,
            "username": user.username,
        }
    }

def resolve_logout(obj, info):
    return {
        "error": "",
        "status": ""
    }

def resolve_signup(*_, input):
    user = create_user(user_input=input)
    return {
        "token": "token",
        "user": {
            "id": user.id,
            "email": user.email,
            "username": user.username,
        }
    }

def resolve_update_user(*_, user_id, input):
    user = update_user(user_id, input)
    if not user:
        return {}
    return {
        "user": {
            "email": user.email,
            "username": user.username,
        }
    }

def resolve_update_password(*_, input):
    return {
        "error": "",
        "status": ""
    }
