import graphene

from api.game import Query as GameQuery
from api.user import Query as UserQuery

class Query(GameQuery, UserQuery):
    pass

schema = graphene.Schema(query=Query)
