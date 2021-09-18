from integration.igdb.client import igdb_client

API_ROUTE = 'games'

def search_games(search: str) -> list:
    payload = f"fields name,cover.url; search \"{search}\"; limit 30;"
    games: list = igdb_client(API_ROUTE, payload, "kr5qqk4ro88ubzvcfqzr1q1kwjxfbl")
    return games