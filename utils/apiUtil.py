import requests, json

def getAPI(url):
    response = requests.get(url)
    return response