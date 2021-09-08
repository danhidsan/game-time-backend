from ariadne import load_schema_from_path, make_executable_schema, QueryType

from .resolvers.user import resolve_user
from .resolvers.game import resolve_games

type_defs = load_schema_from_path('./api/types/')

query = QueryType()
query.set_field('user', resolve_user)
query.set_field('games', resolve_games)

schema = make_executable_schema(type_defs, [query])
