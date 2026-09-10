# CodeAlpha Stock Portfolio Tracker

## Internship Task

This project was created for the CodeAlpha Python Programming Internship.

**Task 2: Stock Portfolio Tracker**

The program lets a user select stocks from a predefined price list, enter the number of shares, and calculate the total investment value. The result can also be saved to a CSV file.

## Features

- Uses a hardcoded dictionary of stock prices
- Accepts stock symbols and quantities from the user
- Validates incorrect stock names and quantities
- Calculates investment value for every selected stock
- Displays a clean portfolio summary
- Calculates the total investment
- Optionally saves the result to `portfolio_summary.csv`

## Python Concepts Used

- Dictionaries
- Functions
- Loops
- `if` / `else`
- User input and output
- Basic arithmetic
- File handling
- CSV module

## Requirements

- Python 3.x
- No third-party package is required

## How to Run

Open a terminal inside the project folder and run:

```bash
python stock_portfolio_tracker.py
```

On some systems, use:

```bash
python3 stock_portfolio_tracker.py
```

## Example

```text
Enter a stock symbol, or type DONE to finish: AAPL
Enter quantity for AAPL: 3
Added: 3 share(s) of AAPL at $180.00 each = $540.00

Enter a stock symbol, or type DONE to finish: TSLA
Enter quantity for TSLA: 2
Added: 2 share(s) of TSLA at $250.00 each = $500.00

Enter a stock symbol, or type DONE to finish: DONE

Total Investment Value: $1040.00
```

## GitHub Repository Name

Create the repository with this exact style:

`CodeAlpha_StockPortfolioTracker`

## Push to GitHub

After creating an empty repository on GitHub, open a terminal in this project folder and run:

```bash
git init
git add .
git commit -m "Complete CodeAlpha Stock Portfolio Tracker"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/CodeAlpha_StockPortfolioTracker.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## Suggested LinkedIn Video Explanation

In your short demo video, explain:

1. This is Task 2 of the CodeAlpha Python Programming Internship.
2. Stock prices are stored in a Python dictionary.
3. The user enters a stock symbol and quantity.
4. The program calculates each stock's investment value.
5. It calculates the total portfolio value.
6. The user can save the summary to a CSV file.
7. Show the GitHub repository at the end.

## Author

Created as part of the CodeAlpha Python Programming Internship.
