from typing import List
from marshmallow import Schema, fields, post_load
from integration.igdb.client import igdb_client
from integration.igdb.models import IGDBCover, IGDBGame

API_ROUTE = 'games'
class IGDBCoverSchema(Schema):
    id = fields.Integer()
    url = fields.String()

    @post_load
    def make_igdb_cover(self, data, **kargs):
        return IGDBCover(**data)
class IGDBGameSchema(Schema):
    id = fields.Integer()
    cover = fields.Nested(IGDBCoverSchema)
    name = fields.String()

    @post_load
    def make_igdb_game(self, data, **kargs):
        return IGDBGame(**data)

def search_games_igdb(search: str) -> List[IGDBGame]:
    payload = f"fields name,cover.url; search \"{search}\"; limit 30;"
    games: list = igdb_client(API_ROUTE, payload, "i1wbq2wwiuh0vkv36te51t3o79gh28")
    schema = IGDBGameSchema(many=True)
    games_deserialized = schema.load(games)
    return games_deserialized
