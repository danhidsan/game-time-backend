import requests
import json

def igdb_client(route: str, payload: str):
    url = f"https://api.igdb.com/v4/{route}"
    headers = {
        "Client-ID": "cm6isi8noymd5tjq8ycrkkjwasqxy9",
        "Authorization": "Bearer w0xffpjv3aefqb9n4gfymca12ayrox",
        "Accept": "application/json",
        "Content-Type": "text/plain",
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    
    return response_json
