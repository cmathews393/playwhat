import bs4 as bs
from bs4 import BeautifulSoup
import requests
import json

catalogURL = "https://catalog.gamepass.com/sigls/v2?id=fdd9e2a7-0fee-49f6-ad69-4354098401ff&language=en-us&market=US"


gamepassRequest = requests.get(catalogURL)

gamepassPCGames = gamepassRequest.json()

gameIDs = [item['id'] for item in gamepassPCGames if 'id' in item]

IDsForRequest = ','.join(gameIDs)

gameInfoURL = f"https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds=9PJ06TZX4NMH&market=US&languages=en-us&MS-CV=DGU1mcuYo0WMMp+F.1"

gameInfoRequest = requests.get(gameInfoURL)

gameInfo = gameInfoRequest.json()

print(gameInfo)


json_object = json.dumps(gameInfoRequest.json(), indent=4, sort_keys=True)


with open("sample.json", "w") as outfile:
    outfile.write(json_object)