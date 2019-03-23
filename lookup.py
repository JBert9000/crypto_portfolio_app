import requests
import json
import os
os.system('cls')

api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
api = json.loads(api_request.content)

currencies = ["BTC", "ETH", "XBY"]

print("---------------------")
for x in api:
    for coin in currencies:
        if coin == x["symbol"]:
            print(x["name"])
            print("${0:.2f}".format(float(x["price_usd"])))
            print("Rank: {0:.0f}".format(float(x["rank"])))
            print("---------------------")

currency = input("Insert Crypto Coin Symbol: ")

for y in api:
    for symbol in currency:
        if symbol == y["symbol"]:
            print(y["symbol"])