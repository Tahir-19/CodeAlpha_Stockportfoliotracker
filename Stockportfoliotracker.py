
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300,
    "MSFT": 300
}

portfolio = {}
total_investment = 0

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Please choose from the available stocks.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + quantity

for stock, quantity in portfolio.items():
    total_investment += stock_prices[stock] * quantity

print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    print(f"{stock}: {quantity} shares at ${stock_prices[stock]} each")

print(f"Total Investment Value: ${total_investment}")

save = input("Save portfolio to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio:\n")
        for stock, quantity in portfolio.items():
            f.write(f"{stock}: {quantity} shares at ${stock_prices[stock]} each\n")
        f.write(f"Total Investment Value: ${total_investment}\n")
    print("Portfolio saved to portfolio.txt")