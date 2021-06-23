import os
import base64
import requests

# Server-to-server authentication
# 1.APPLICATION - Request access token (->client_id,client_secret,grant_type)
# 2.SPOTIFY ACCOUNTS SERVICE -> Returns access token (<- access_token)
# 3.APPLICATION -> User access token in requests to Web API (-> access_token)
# 4.SPOTIFY WEB API -> Return requested (unscoped) data (<-{JSON object})

# client_ID and client_Secret are ENVIROMENT VARIABLES!
client_ID = os.environ.get('SPOTIFY_CLIENT_ID')
client_Secret = os.environ.get('CLIENT_SECRET')

def getAccessToken(clientID, clientSecret):
    client_credentials = f'{client_ID}:{client_Secret}'
    client_credentials_b64 = base64.b64encode(client_credentials.encode())

    token_url = "https://accounts.spotify.com/api/token"
    token_data = {
        "grant_type": "client_credentials"
    }
    token_headers = {
        "Authorization": f"Basic {client_credentials_b64.decode()}" # <base64 encoded client_id:client_secret>
    }

    r = requests.post(token_url, data=token_data, headers=token_headers)
    response = r.json()
    # print(json.dumps(response, indent=2))

    access_token = response["access_token"]
    return access_token

# Response example:
# {
#     "access_token": "BQDZ19fpCYjoQ_sqS2GR50fUZEKzfROG5GJ18u0Tq2V_pYmMM5RpowYHmnYGdgRya0xh7_Td2k8ygSoocNU",
#     "token_type": "Bearer",
#     "expires_in": 3600
# }