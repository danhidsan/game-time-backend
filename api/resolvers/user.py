""" Query resolvers """

def resolve_user(obj, info, id=None):
    return {
        "email": "email 1",
        "username": "username 1",
    }

""" Mutation resolvers """

def resolve_login(*_, input):
    return {
        "error": "",
        "status": "OK",
        "token": "",
        "user": {
            "email": "",
            "username": "",
        }
    }

def resolve_logout(obj, info):
    return {
        "error": "",
        "status": ""
    }

def resolve_signup(*_, input):
    return {
        "error": "",
        "status": "OK",
        "token": "",
        "user": {
            "email": "",
            "username": "",
        }
    }

def resolve_update_user(*_, input):
    return {
        "error": "",
        "status": "OK",
        "user": {
            "email": "",
            "username": "",
        }
    }

def resolve_update_password(*_, input):
    return {
        "error": "",
        "status": ""
    }
