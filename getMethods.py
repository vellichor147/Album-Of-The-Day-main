import requests
import json
import pprint
import pandas as pd

""" def getArtistName(token, artist_ID):
    artistEndpoint = f'https://api.spotify.com/v1/artists/{artist_ID}'
    artist_headers = {
        "Authorization": f"Bearer " + token
    }
    r = requests.get(artistEndpoint, headers=artist_headers)
    response = r.json()
    #print(json.dumps(response, indent=2))
    artist_name = response['name']
    return artist_name """

def getArtistInfo(token, artist_ID):
    artistEndpoint = f'https://api.spotify.com/v1/artists/{artist_ID}'
    artist_headers = {
        "Authorization": f"Bearer " + token
    }
    r = requests.get(artistEndpoint, headers=artist_headers)
    response = r.json()
    #print(json.dumps(response, indent=2))
    name = response['name']
    link = response['external_urls']['spotify']
    followers = response['followers']['total']
    genres = response['genres']
    popularity = response['popularity']
    info = [name,link,followers,genres,popularity]
    #print("Artist info: {}".format(info))
    return info

def getAlbumsInfo(token, artist_ID):
    artistEndpoint = f'https://api.spotify.com/v1/artists/{artist_ID}/albums'
    artist_headers = {
        "Authorization": f"Bearer " + token
    }
    r = requests.get(artistEndpoint, headers=artist_headers)
    response = r.json()
    #print(response)
    album_id = response['items'][0]['id']
    album_cover = response['items'][0]['images'][0]['url']
    album_name = response['items'][0]['name']
    album_date = response['items'][0]['release_date']
    album_link = response['items'][0]['external_urls']['spotify']
    info = [album_id,album_cover,album_name,album_date,album_link]
    print("Album info : {}".format(info))
    return info





""" def getArtistsAlbums(token, artist_ID):
    artistEndpoint = f'https://api.spotify.com/v1/artists/{artist_ID}/albums'
    artist_headers = {
    "Authorization": f"Bearer " + token
    }
    r = requests.get(artistEndpoint, headers=artist_headers)
    response = r.json()
    # print(json.dumps(response, indent=2))
    # pprint.pprint(r.json())
    # data = r.json()
    # print(data.keys())
    # print(response.keys())
    # album_link = response['items'][0]['href']
    album_id = response['items'][0]['id']
    album_cover = response['items'][0]['images'][0]['url']
    album_name = response['items'][0]['name']
    album_date = response['items'][0]['release_date']
    # print('album link: {}'.format(album_link))
    info = [album_id,album_cover,album_name,album_date]
    return info """

""" def getAlbum(token, album_ID):
    albumEndpoint = f'https://api.spotify.com/v1/albums/{album_ID}'
    album_headers = {
        "Authorization": f"Bearer " + token
    }
    r = requests.get(albumEndpoint, headers=album_headers)
    response = r.json()
    #print(json.dumps(response, indent=2)) """
""" 
def getAllCategories(token):
    categoriesEndpoint = "https://api.spotify.com/v1/browse/categories"
    categories_headers = {
        "Authorization": f"Bearer " + token
    }
    r = requests.get(categoriesEndpoint, headers=categories_headers)
    response = r.json()
    #print(json.dumps(response, indent=2)) """

