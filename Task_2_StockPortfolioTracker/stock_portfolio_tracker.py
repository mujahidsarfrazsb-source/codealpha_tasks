"""
CodeAlpha Python Programming Internship
Task 2: Stock Portfolio Tracker

A simple console program that calculates the total value of a stock portfolio
using manually defined stock prices.
"""

import csv
from datetime import datetime


STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 175.00,
    "AMZN": 185.00,
}


def show_available_stocks():
    """Display the stock symbols and their fixed prices."""
    print("\nAvailable stocks:")
    print("-" * 30)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<8} ${price:>8.2f}")
    print("-" * 30)


def get_quantity(symbol):
    """Ask the user for a valid positive quantity."""
    while True:
        value = input(f"Enter quantity for {symbol}: ").strip()

        try:
            quantity = int(value)

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            return quantity

        except ValueError:
            print("Please enter a whole number, for example 2 or 10.")


def save_to_csv(portfolio, total_value):
    """Save the portfolio summary to a CSV file."""
    filename = "portfolio_summary.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Stock", "Quantity", "Price", "Investment Value"])

        for item in portfolio:
            writer.writerow([
                item["symbol"],
                item["quantity"],
                f'{item["price"]:.2f}',
                f'{item["value"]:.2f}',
            ])

        writer.writerow([])
        writer.writerow(["Total Investment", "", "", f"{total_value:.2f}"])
        writer.writerow(["Generated At", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

    print(f"\nPortfolio saved successfully to {filename}")


def main():
    print("=" * 46)
    print("         STOCK PORTFOLIO TRACKER")
    print("=" * 46)

    portfolio = []

    while True:
        show_available_stocks()

        symbol = input(
            "\nEnter a stock symbol, or type DONE to finish: "
        ).strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print("That stock is not in the available stock list.")
            continue

        quantity = get_quantity(symbol)
        price = STOCK_PRICES[symbol]
        investment_value = price * quantity

        portfolio.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "value": investment_value,
        })

        print(
            f"Added: {quantity} share(s) of {symbol} "
            f"at ${price:.2f} each = ${investment_value:.2f}"
        )

    if not portfolio:
        print("\nNo stocks were added. Program ended.")
        return

    total_value = sum(item["value"] for item in portfolio)

    print("\n" + "=" * 58)
    print("PORTFOLIO SUMMARY")
    print("=" * 58)
    print(f'{"Stock":<10}{"Qty":<8}{"Price":<15}{"Value":<15}')
    print("-" * 58)

    for item in portfolio:
        print(
            f'{item["symbol"]:<10}'
            f'{item["quantity"]:<8}'
            f'${item["price"]:<14.2f}'
            f'${item["value"]:<14.2f}'
        )

    print("-" * 58)
    print(f"Total Investment Value: ${total_value:.2f}")

    save_choice = input("\nSave this result to CSV? (y/n): ").strip().lower()

    if save_choice == "y":
        save_to_csv(portfolio, total_value)
    else:
        print("Result was not saved.")

    print("\nThank you for using the Stock Portfolio Tracker.")


if __name__ == "__main__":
    main()
