import bs4 as bs
from bs4 import BeautifulSoup
import requests
import json

# catalogURL = "https://catalog.gamepass.com/sigls/v2?id=fdd9e2a7-0fee-49f6-ad69-4354098401ff&language=en-us&market=US"


# gamepassRequest = requests.get(catalogURL)

# gamepassPCGames = gamepassRequest.json()

# gameIDs = [item['id'] for item in gamepassPCGames if 'id' in item]

# IDsForRequest = ','.join(gameIDs)

# gameInfoURL = f"https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds=9PJ06TZX4NMH&market=US&languages=en-us&MS-CV=DGU1mcuYo0WMMp+F.1"

# gameInfoRequest = requests.get(gameInfoURL)

# gameInfo = gameInfoRequest.json()

# print(gameInfo)


# json_object = json.dumps(gameInfoRequest.json(), indent=4, sort_keys=True)


# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)


# attributes_xbl_online_coop = []

# for product in json_object["Products"]:
#     for attribute in product.get("Properties", {}).get("Attributes", []):
#         if attribute.get("Name") == "XblOnlineCoop":
#             attributes_xbl_online_coop.append(attribute)

# print(attributes_xbl_online_coop)
def mainfunc():

    catalogURL = "https://catalog.gamepass.com/sigls/v2?id=fdd9e2a7-0fee-49f6-ad69-4354098401ff&language=en-us&market=US"


    # Request for GamePass PC Games
    gamepassRequest = requests.get(catalogURL)
    gamepassPCGames = gamepassRequest.json()

    # Extracting game IDs
    gameIDs = [item['id'] for item in gamepassPCGames if 'id' in item]
    IDsForRequest = ','.join(gameIDs)
    print(IDsForRequest)
    # IDsForRequest = "9NG07QJNK38J"
    gameInfoURL = f"https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds={IDsForRequest}&market=US&languages=en-us&MS-CV=DGU1mcuYo0WMMp+F.1"
    # Request for Game Info
    gameInfoRequest = requests.get(gameInfoURL)
    gameInfo = gameInfoRequest.json()
    print(gameInfo)
    # Extracting Attributes where Name is "XblOnlineCoop"
    minRequestedPlayers = 4
    product_info = []

    for product in gameInfo.get("Products", []):
        info = {}
        # Check for XblOnlineCoop attribute
        for attribute in product.get("Properties", {}).get("Attributes", []):
            if attribute.get("Name") == "XblOnlineCoop":
                maxPlayers = attribute.get("Maximum")
                if maxPlayers and maxPlayers >= minRequestedPlayers:
                    for availability in product["DisplaySkuAvailabilities"]:
                        for localized_property in availability["Sku"]["LocalizedProperties"]:
                            sku_title = localized_property.get("SkuTitle")
                            if sku_title:
                                info["sku_title"] = sku_title
                                break  # Break after finding the SKU title
                        if "sku_title" in info:
                            break  # Break if SKU title is found

        # Get URI from LocalizedProperties
        if "sku_title" in info:
            for localized_property in product.get("LocalizedProperties", []):
                for image in localized_property.get("Images", []):
                    if image.get("ImagePurpose") == "BoxArt":
                        uri = image.get("Uri")
                        if uri:
                            info["uri"] = uri
                            break  # Break after finding the URI
                    if "uri" in info:
                        break  # Break if URI is found

        if "sku_title" in info and "uri" in info:
            product_info.append(info)
    print(product_info)
    return product_info
