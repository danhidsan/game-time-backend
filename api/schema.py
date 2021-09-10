from ariadne import load_schema_from_path, make_executable_schema, QueryType, MutationType

from .resolvers.user import (
  resolve_user, resolve_login, resolve_logout, resolve_signup, 
  resolve_update_password, resolve_update_user
)
from .resolvers.game import resolve_explore_games, resolve_search_games, resolve_user_games

type_defs = load_schema_from_path('./api/types/')

query = QueryType()
mutation = MutationType()

""" User """
# Queries
query.set_field('user', resolve_user)
# Mutations
mutation.set_field('login', resolve_login)
mutation.set_field('logout', resolve_logout)
mutation.set_field('signUp', resolve_signup)
mutation.set_field('updateUser', resolve_update_user)
mutation.set_field('updatePassword', resolve_update_password)

""" Game """
# Queries
query.set_field('exploreGames', resolve_explore_games)
query.set_field('searchGames', resolve_search_games)
query.set_field('userGames', resolve_user_games)

schema = make_executable_schema(type_defs, [query, mutation])
