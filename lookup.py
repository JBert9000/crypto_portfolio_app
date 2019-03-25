import requests
import json
import os
os.system('cls')

coin_names = ["", "xtrabytes", "vestchain", "dash"]

api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
api = json.loads(api_request.content)

# api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/" + str(coin_names))
# api = json.loads(api_request.content)

# xby_request = requests.get("https://api.coinmarketcap.com/v1/ticker/xtrabytes")
# xby = json.loads(xby_request.content)



# My portfolio
my_portfolio = [
    {
        "sym": "ETH",
        "amount_owned": 0.8,
        "price_paid_per": 500
    },
    {
        "sym": "XBY",
        "amount_owned": 2500,
        "price_paid_per": 0.23
    },
    {
        "sym": "VEST",
        "amount_owned": 500,
        "price_paid_per": 0.004
    },
    {
        "sym": "DASH",
        "amount_owned": 1000,
        "price_paid_per": 10
    }
]

print("---------------------")

# for i in coin_names:
#     for coin_names in api_request:
#         print(i)

portfolio_profit_loss = 0

for x in api:
    for coin in my_portfolio:
        if coin["sym"] == x["symbol"]:

            # Do some math
            total_paid = coin["amount_owned"] * coin["price_paid_per"]
            current_value = float(coin["amount_owned"]) * float(x["price_usd"])
            profit_loss = current_value - total_paid
            portfolio_profit_loss += profit_loss

            print(x["name"])
            print("${0:.2f}".format(float(x["price_usd"])))
            print("Rank: {0:.0f}".format(float(x["rank"])))
            print("Total Paid: ${0:.2f}".format(float(total_paid)))
            print("Current Value: ${0:.2f}".format(current_value))
            print("Profit / Loss: ${0:.2f}".format(profit_loss))
            print("---------------------")

print("GAINZ = ${0:.2f}".format(float(portfolio_profit_loss)))

# currency = input("Insert Crypto Coin Symbol: ")
#
# for y in api:
#     for symbol in currency:
#         if symbol == y["symbol"]:
#             print(y["symbol"])

