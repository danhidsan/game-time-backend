import os
import requests
import json

class AuthorizationError(Exception):
    def __init__(self, message="Authorization Failure") -> None:
        self.message = message
        super().__init__(self.message)

class IGDBServerError(Exception):
    def __init__(self, message="IGDB Internal server error") -> None:
        self.message = message
        super().__init__(self.message)

def igdb_client(route: str, payload: str, token: str):
    url = f"{os.environ.get('IGDB_URL')}{route}"
    headers = {
        "Client-ID": os.environ.get('IGDB_CLIENT_ID'),
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Content-Type": "text/plain",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 401:
        raise AuthorizationError
    elif response.status_code == 500:
        raise IGDBServerError

    response_json = json.loads(response.text)
    
    return response_json
