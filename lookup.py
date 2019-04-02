import matplotlib.pyplot as plt
from tkinter import *
import requests
import json
import os
os.system('cls')

def red_green(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"

root = Tk()


# root.title("Crypto Currency Portfolio")
# root.iconbitmap(r'c:\codemy.ico')

            # header_names = ["Name", "Rank", "Current Price", "Price Paid", "P/L Per Coin", "1 Hour Change", "24 Hour Change",
            #                 "7 Day Change", "Current Value", "P/L Total"]
            #
            # colour_change = ["white", "silver"]
            #
            # column = range(10)
            #
            # header = Label(root, text=header_names, bg=colour_change, font = "Verdana 8 bold")
            # header.grid(row=0, column=column, sticky=N+S+E+W)
            #
            # for i in range(len(header_names)):
            #     print(header[i])




# ********** Create Header **********

name = Label(root, text="Name", bg="white", font="Verdana 8 bold")
name.grid(row=0, column=0, sticky=N + S + E + W)

rank = Label(root, text="Rank", bg="silver", font="Verdana 8 bold")
rank.grid(row=0, column=1, sticky=N + S + E + W)

current_price = Label(root, text="Current Price", bg="white", font="Verdana 8 bold")
current_price.grid(row=0, column=2, sticky=N + S + E + W)

price_paid = Label(root, text="Price Paid", bg="silver", font="Verdana 8 bold")
price_paid.grid(row=0, column=3, sticky=N + S + E + W)

PL_per_coin = Label(root, text="P/L Per Coin", bg="white", font="Verdana 8 bold")
PL_per_coin.grid(row=0, column=4, sticky=N + S + E + W)

hour_change = Label(root, text="1 Hour Change", bg="silver", font="Verdana 8 bold")
hour_change.grid(row=0, column=5, sticky=N + S + E + W)

tf_hour_change = Label(root, text="24 Hour Change", bg="white", font="Verdana 8 bold")
tf_hour_change.grid(row=0, column=6, sticky=N + S + E + W)

seven_day_change = Label(root, text="7 Day Change", bg="silver", font="Verdana 8 bold")
seven_day_change.grid(row=0, column=7, sticky=N + S + E + W)

current_value = Label(root, text="Current Value", bg="white", font="Verdana 8 bold")
current_value.grid(row=0, column=8, sticky=N + S + E + W)

PL_total = Label(root, text="P/L Total", bg="silver", font="Verdana 8 bold")
PL_total.grid(row=0, column=9, sticky=N + S + E + W)

# ********** End of Header **********

coin_names = ["", "xtrabytes", "vestchain", "dash"]

# api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/" + str(coin_names))
# api = json.loads(api_request.content)

# xby_request = requests.get("https://api.coinmarketcap.com/v1/ticker/xtrabytes")
# xby = json.loads(xby_request.content)


print("----------------------------------")

# for i in coin_names:
#     for coin_names in api_request:
#         print(i)



def lookup():
    api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
    api = json.loads(api_request.content)

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
            "amount_owned": 100,
            "price_paid_per": 10
            },
        {
            "sym": "XRP",
            "amount_owned": 100,
            "price_paid_per": 0.1
        },
        {
            "sym": "TRON",
            "amount_owned": 1000,
            "price_paid_per": 0.01
        },
        {
            "sym": "STEEM",
            "amount_owned": 100,
            "price_paid_per": 0.2
        }
        ]

    portfolio_profit_loss = 0
    total_current_value = 0
    row_count = 1
    # column_count = 0
    pie = []
    pie_size = []
    for x in api:
        for coin in my_portfolio:
            if coin["sym"] == x["symbol"]:

                # Do some math
                total_paid = float(coin["amount_owned"]) * float(coin["price_paid_per"])
                current_value = float(coin["amount_owned"]) * float(x["price_usd"])
                profit_loss = float(current_value) - float(total_paid)
                portfolio_profit_loss += profit_loss
                profit_loss_per_coin = float(x["price_usd"]) - float(coin["price_paid_per"])
                total_current_value += current_value

                pie.append(x["name"])
                pie_size.append(coin["amount_owned"])

                # print(x["name"])
                # print(" Current Price: ${0:.2f}".format(float(x["price_usd"])))
                # print(" Profit / Loss Per Coin: ${0:.2f}".format(float(profit_loss_per_coin)))
                # print(" Rank: {0:.0f}".format(float(x["rank"])))
                # print(" Total Paid: ${0:.2f}".format(float(total_paid)))
                # print(" Current Value: ${0:.2f}".format(current_value))
                # print(" Profit / Loss: ${0:.2f}".format(profit_loss))
                # print("----------------------------------")

                name = Label(root, text=x["name"], bg="white")
                name.grid(row=row_count, column=0, sticky=N + S + E + W)

                rank = Label(root, text=x["rank"], bg="silver")
                rank.grid(row=row_count, column=1, sticky=N + S + E + W)

                current_price = Label(root, text="${0:.2f}".format(float(x["price_usd"]), bg="white"))
                current_price.grid(row=row_count, column=2, sticky=N + S + E + W)

                price_paid = Label(root, text="${0:.2f}".format(float(total_paid)), bg="silver")
                price_paid.grid(row=row_count, column=3, sticky=N + S + E + W)

                PL_per_coin = Label(root, text="${0:.2f}".format(float(profit_loss_per_coin)), bg="white",
                                    fg=red_green(float(profit_loss_per_coin)))
                PL_per_coin.grid(row=row_count, column=4, sticky=N + S + E + W)

                hour_change = Label(root, text="{0:.2f}%".format(float(x["percent_change_1h"])), bg="silver")
                hour_change.grid(row=row_count, column=5, sticky=N + S + E + W)

                tf_hour_change = Label(root, text="{0:.2f}%".format(float(x["percent_change_24h"])), bg="white",
                                       fg=red_green((float(x["percent_change_24h"]))))
                tf_hour_change.grid(row=row_count, column=6, sticky=N + S + E + W)

                seven_day_change = Label(root, text="{0:.2f}%".format(float(x["percent_change_7d"])),
                                         bg="silver", fg=red_green((float(x["percent_change_7d"]))))
                seven_day_change.grid(row=row_count, column=7, sticky=N + S + E + W)

                current_value = Label(root, text="${0:.2f}".format(float(current_value)), bg="white")
                current_value.grid(row=row_count, column=8, sticky=N + S + E + W)

                PL_total = Label(root, text="${0:.2f}".format(float(profit_loss)), bg="silver", fg=red_green((float(
                    profit_loss))))
                PL_total.grid(row=row_count, column=9, sticky=N + S + E + W)

                row_count += 1


    portfolio_profits = Label(root, text="Profit/Loss: ${0:.2f}".format(float(portfolio_profit_loss)), font="Verdana 8 "
                                                                                                        "bold",
                              fg=red_green(float(portfolio_profit_loss)))
    portfolio_profits.grid(row=row_count, column=0, sticky=W, padx=10, pady=10)

    root.title("Cryotp Currency Porfolio - Portolio Value: ${0:.2f}".format(float(total_current_value)))
    # total_current_value_output = Label(root, text="Total Value: ${0:.2f}".format(float(total_current_value)),
    #                                    font="Verdana 8 "
    #                                                                                                     "bold",
    #                           fg=red_green(float(total_current_value)))
    #
    # total_current_value_output.grid(row=row_count+1, column=0, sticky=W, padx=10, pady=10)

    # print("GAINZ = ${0:.2f}".format(float(portfolio_profit_loss)))

    api = ""
    update_button = Button(root, text="Update Prices", command=lookup)
    update_button.grid(row=row_count, column=4)


    def graph(pie, pie_sizes):
        labels = pie
        sizes = pie_size
        colors = ["yellowgreen", 'gold', 'lightskyblue', 'lightcoral', 'red']
        patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    graph_button = Button(root, text="Pie Chart", command=graph(pie, pie_size))
    graph_button.grid(row=row_count, column=5)

lookup()

root.mainloop()


# currency = input("Insert Crypto Coin Symbol: ")
#
# for y in api:
#     for symbol in currency:
#         if symbol == y["symbol"]:
#             print(y["symbol"])

