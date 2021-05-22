from graphene import Schema, ObjectType, String

class Hello(ObjectType):
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    def resolve_hello(root, info, name):
        return f'Hello {name}'

    def resolve_goodbye(root, info):
        return 'See ya!'

schema = Schema(query=Hello)