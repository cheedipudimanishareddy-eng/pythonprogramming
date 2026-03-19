# Stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "GOOGL": 140,
    "TSLA": 250,
    "AMZN": 130
}

portfolio = {}
total_value = 0

print("Stock Portfolio Tracker")
print("Available stocks:", stock_prices.keys())

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock] = quantity
    else:
        print("Stock not available.")

# Calculate portfolio value
print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value

    print(stock, "-", quantity, "shares ×", price, "=", value)

print("\nTotal Portfolio Value:", total_value)
