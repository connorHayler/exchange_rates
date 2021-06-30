import json

with open("exchange_rates.json") as file:
    exchange = json.load(file)
    rates = exchange["rates"]
    while True:
        try:
            print(rates[input("Enter the country code for the exchange rate: ")])
        except KeyError:
            print("Sorry that value doesn't exist.")
