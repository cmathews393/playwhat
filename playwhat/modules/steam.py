import requests
import os
from dotenv import load_dotenv

load_dotenv()

steamAPIkey = os.getenv("Steam__ApplicationKey")

print(steamAPIkey)

response = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steamAPIkey}&steamid=76561198066299732&include_played_free_games=true&format=json")

print(response.json())