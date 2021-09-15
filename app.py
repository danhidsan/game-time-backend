from ariadne import QueryType, graphql_sync, make_executable_schema
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify

from integration.igdb.client import igdb_client
from api.schema import schema

app = Flask(__name__)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    # On GET request serve GraphQL Playground
    # You don't need to provide Playground if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL Playground app.
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code

@app.route("/health", methods=["GET"])
def health():
    payload = "fields name,cover.url; search \"Horizon Zero Down\"; limit 30;"
    route = "games"
    games = igdb_client(route, payload)
    status_code = 200
    return jsonify(status="OK", games=games), status_code



if __name__ == "__main__":
    app.run(debug=True)