import os
import requests
import json

def igdb_client(route: str, payload: str):
    url = f"{os.environ.get('IGDB_URL')}{route}"
    headers = {
        "Client-ID": os.environ.get('IGDB_CLIENT_ID'),
        "Authorization": "Bearer w0xffpjv3aefqb9n4gfymca12ayrox",
        "Accept": "application/json",
        "Content-Type": "text/plain",
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    
    return response_json
