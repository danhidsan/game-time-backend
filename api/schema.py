from ariadne import load_schema_from_path, make_executable_schema, QueryType

from .resolvers.user import resolve_user
from .resolvers.game import resolve_explore_games, resolve_search_games, resolve_user_games

type_defs = load_schema_from_path('./api/types/')

query = QueryType()

# User
query.set_field('user', resolve_user)

#Game
query.set_field('exploreGames', resolve_explore_games)
query.set_field('searchGames', resolve_search_games)
query.set_field('userGames', resolve_user_games)

schema = make_executable_schema(type_defs, [query])
