def resolve_explore_games(obj, info):
    return [
        { "popular": [], "newness": [], "anticipated": [] },
    ]

def resolve_search_games(*_, name):
    return [
        { "igdbId": "", "title": "", "image": "" }
    ]

def resolve_user_games(*_, userId=None, status=None):
    return [
        { "playing": [{ "title": status }], "forPlay": [], "finished": [] }
    ]