from typing import List
from integration.igdb.games import search_games_igdb
from integration.igdb.models import IGDBGame

def search_games(search: str) -> List[IGDBGame]:
    games = search_games_igdb(search)
    return games