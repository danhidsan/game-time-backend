import graphene

class User(graphene.ObjectType):
    email = graphene.String()
    name = graphene.String()

class Query(graphene.ObjectType):
    user = graphene.Field(User)

    def resolve_user(root, info):
        return { "email": "email1@example.com", "name": "Name1" }
