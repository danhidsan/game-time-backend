from domain.games import search_games

def resolve_explore_games(obj, info):
    return [
        { "popular": [], "newness": [], "anticipated": [] },
    ]

def resolve_search_games(*_, name):
    games = search_games(name)
    print(games[0])
    return map(lambda x: {"id": x.id, "igdbId": x.id, "title": x.name, "image": x.cover.url if x.cover is not None else ""}, games)

def resolve_user_games(*_, userId=None, status=None):
    return [
        { "playing": [{ "title": status }], "forPlay": [], "finished": [] }
    ]