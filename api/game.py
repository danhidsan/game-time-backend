import graphene

class Game(graphene.ObjectType):
    title = graphene.String()
    image = graphene.String()

class GameStatus(graphene.Enum):
    PLAYING = 0
    FOR_PLAYING = 1
    FINISHED = 2
    ALL = 3

class Query(graphene.ObjectType):
    games = graphene.List(Game, search=graphene.String(required=False))
    user_games = graphene.List(Game, )
    game = graphene.Field(Game, user_id=graphene.ID, status=GameStatus())

    def resolve_games(root, info, search=None):
        return [
            {"title": "Title 1", "image": "Image 1"},
            {"title": "Title 2", "image": "Image 2"}
        ]
    def resolve_game(root, info):
        return { "title": "Title 1", "image": "Image 1" }
    
    def resolve_user_games(root, info, user_id, status = GameStatus.ALL):
        return [
            {"title": "Title 1", "image": "Image 1"},
            {"title": "Title 2", "image": "Image 2"}
        ]
