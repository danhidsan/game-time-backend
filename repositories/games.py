from integration.igdb.games import search_games_igdb

def search_games(search: str) -> list:
    games = search_games_igdb(search)
    return games