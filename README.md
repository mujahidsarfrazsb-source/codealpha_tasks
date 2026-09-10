# CodeAlpha Python Programming Internship Projects

This repository contains two completed projects for the **CodeAlpha Python Programming Internship**.

Each task is kept in a separate folder with its own source code, sample files, output files, and detailed documentation. Both projects use core Python concepts and can be run directly with Python 3 without installing any third-party packages.

## Completed Tasks

| Task | Project | Main Focus | Status |
|---|---|---|---|
| Task 2 | Stock Portfolio Tracker | Dictionaries, input handling, calculations, CSV file handling | Completed |
| Task 3 | Email Extractor Automation | Regular expressions, file handling, automation | Completed |

---

## Task 2: Stock Portfolio Tracker

The **Stock Portfolio Tracker** is a console-based Python program that calculates the value of a user's stock investments using manually defined stock prices.

The user can enter a stock symbol and quantity, add multiple stocks to the portfolio, view the calculated investment value for each stock, and see the total portfolio value. The result can also be saved to a CSV file.

### Key Features

- Uses a predefined dictionary of stock prices
- Accepts stock symbols and quantities from the user
- Validates unsupported stock symbols
- Validates invalid, zero, and negative quantities
- Calculates individual investment values
- Calculates the total portfolio value
- Displays a clear portfolio summary
- Optionally saves the result to `portfolio_summary.csv`

### Main Python Concepts

`dictionary` · `functions` · `loops` · `if/else` · `input/output` · `arithmetic` · `exception handling` · `CSV file handling`

### Project Location

```text
Task_2_StockPortfolioTracker/
```

Main program:

```text
stock_portfolio_tracker.py
```

### Run Task 2

Open the task folder and run:

```bash
python stock_portfolio_tracker.py
```

If your system uses `python3`:

```bash
python3 stock_portfolio_tracker.py
```

### Example

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

---

## Task 3: Email Extractor Automation

The **Email Extractor Automation** project automates the process of finding email addresses inside a text file.

The program reads a `.txt` file, extracts email addresses using a regular expression, removes duplicates, displays the final list, and saves the results to another text file.

### Key Features

- Reads email addresses from a `.txt` file
- Uses Python regular expressions for extraction
- Removes duplicate email addresses
- Preserves the order in which addresses first appear
- Displays extracted emails in a numbered list
- Supports custom input and output filenames
- Handles missing or unreadable files
- Rejects non-`.txt` input files
- Saves results to `extracted_emails.txt`

### Main Python Concepts

`re` · `regular expressions` · `functions` · `lists` · `sets` · `loops` · `file handling` · `exception handling` · `pathlib`

### Project Location

```text
Task_3_EmailExtractorAutomation/
```

Main program:

```text
email_extractor.py
```

### Run Task 3

Open the task folder and run:

```bash
python email_extractor.py
```

If your system uses `python3`:

```bash
python3 email_extractor.py
```

For the included sample test, press **Enter** when the program asks for the input filename to use:

```text
sample_input.txt
```

Press **Enter** again for the default output file:

```text
extracted_emails.txt
```

### Example

```text
Extracted Email Addresses
----------------------------------------
1. services@codealpha.tech
2. services.codealpha@gmail.com
3. hr@example.com
4. support@example.org
5. developer.team+python@example.co.uk
6. training.department@example.net
----------------------------------------

Success: 6 unique email address(es) saved to 'extracted_emails.txt'.
```

---

## Repository Structure

```text
CodeAlpha_Tasks/
├── README.md
│
├── Task_2_StockPortfolioTracker/
│   ├── README.md
│   ├── stock_portfolio_tracker.py
│   └── portfolio_summary.csv
│
└── Task_3_EmailExtractorAutomation/
    ├── README.md
    ├── email_extractor.py
    ├── sample_input.txt
    ├── expected_output.txt
    └── extracted_emails.txt
```

Each task also contains its own `README.md` with more detailed information about that individual project.

---

## Requirements

- Python 3.x
- Windows, macOS, or Linux
- A terminal or command prompt
- No third-party Python packages are required

You can use any editor, such as **Visual Studio Code**, **PyCharm**, or **IDLE**.

---

## Skills Practiced

Through these two projects, I practiced:

- Breaking a problem into small reusable functions
- Working with dictionaries, lists, and sets
- Validating user input
- Performing basic calculations
- Reading and writing text files
- Creating and reading CSV output
- Using regular expressions for text processing
- Handling common runtime errors
- Organizing Python projects into clear folders
- Writing project documentation for GitHub

---

## Internship Task Coverage

This repository includes two completed tasks from the CodeAlpha Python Programming task list:

### Task 2: Stock Portfolio Tracker

Completed requirements include:

- User enters stock names and quantities
- Stock prices are stored in a hardcoded dictionary
- Investment values are calculated
- Total investment value is displayed
- Results can be saved to a CSV file

### Task 3: Task Automation with Python Scripts

Selected automation:

**Extract email addresses from a text file and save them to another file.**

Completed requirements include:

- Reads a text file
- Extracts email addresses
- Uses the `re` module
- Uses file handling
- Saves extracted results to another file

---

## Project Notes

- The stock prices used in Task 2 are manually defined for demonstration purposes and are not live market prices.
- The email extraction pattern in Task 3 is intended for common email formats used in this internship project.
- Both projects are intentionally built with Python's standard library so they remain easy to run and review.

---

## Author

**Mujahid Sarfraz**  
Python Programming Intern  
CodeAlpha

---

## Acknowledgment

These projects were completed as part of the **CodeAlpha Python Programming Internship** to practice Python fundamentals through small, working applications.
