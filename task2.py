def stock_tracker():
    # Predefined prices as per instructions
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 150, "MSFT": 400}
    portfolio = {}
    
    print("--- Stock Portfolio Tracker ---")
    
    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").upper()
        if symbol == 'DONE':
            break
        
        if symbol in stock_prices:
            quantity = int(input(f"How many shares of {symbol} do you own? "))
            portfolio[symbol] = quantity
        else:
            print("Stock not found in our database.")

    print("\n--- Your Portfolio Summary ---")
    total_value = 0
    for symbol, qty in portfolio.items():
        value = qty * stock_prices[symbol]
        total_value += value
        print(f"{symbol}: {qty} shares | Value: ${value}")

    print(f"\nTotal Investment Value: ${total_value}")

stock_tracker()