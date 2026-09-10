# CodeAlpha Email Extractor Automation

A Python automation project created for the **CodeAlpha Python Programming Internship**.

This project fulfills **Task 3: Task Automation with Python Scripts**. The selected automation task extracts email addresses from a `.txt` file and saves the unique results to another text file.

## Project Objective

The goal is to automate a repetitive text-processing task. Instead of manually searching a text file for email addresses, the program reads the file, detects email addresses, removes duplicates, displays the results, and saves them automatically.

## Features

- Reads a `.txt` file
- Extracts email addresses using regular expressions
- Removes duplicate email addresses
- Preserves the order in which addresses first appear
- Displays extracted emails in a numbered list
- Saves results to a new `.txt` file
- Accepts custom input and output filenames
- Provides default filenames for quick testing
- Handles missing and unreadable files
- Rejects non-`.txt` input files
- Uses only Python's standard library

## Python Concepts Used

- `re` module
- Regular expressions
- File handling
- Functions
- Lists
- Sets
- Loops
- Conditional statements
- Exception handling
- User input and output
- `pathlib`

## Project Files

```text
CodeAlpha_EmailExtractorAutomation/
├── email_extractor.py
├── sample_input.txt
├── expected_output.txt
├── extracted_emails.txt
└── README.md
```

### File Description

- `email_extractor.py` - Main Python automation script
- `sample_input.txt` - Sample text used for testing
- `expected_output.txt` - Expected result for the sample input
- `extracted_emails.txt` - Example generated output
- `README.md` - Project documentation

## Requirements

- Python 3.x
- No third-party packages are required

## How to Run

1. Download or clone this repository.
2. Open the project folder.
3. Open a terminal or command prompt in the folder.
4. Run:

```bash
python email_extractor.py
```

On systems that use `python3`, run:

```bash
python3 email_extractor.py
```

## Quick Test

The repository includes `sample_input.txt`.

When the program asks:

```text
Enter input file name [sample_input.txt]:
```

press **Enter** to use the sample file.

When it asks:

```text
Enter output file name [extracted_emails.txt]:
```

press **Enter** again.

The program will create `extracted_emails.txt`.

## Example Run

```text
==================================================
          EMAIL EXTRACTOR AUTOMATION
==================================================

Enter input file name [sample_input.txt]:

Extracted Email Addresses
----------------------------------------
1. services@codealpha.tech
2. services.codealpha@gmail.com
3. hr@example.com
4. support@example.org
5. developer.team+python@example.co.uk
6. training.department@example.net
----------------------------------------

Enter output file name [extracted_emails.txt]:

Success: 6 unique email address(es) saved to 'extracted_emails.txt'.
```

## How It Works

1. The user provides the name of a `.txt` file.
2. The program reads its contents.
3. A regular expression searches for email addresses.
4. Duplicate addresses are removed.
5. The unique addresses are displayed.
6. The user chooses an output filename.
7. The final list is saved, one address per line.

## Regular Expression

The program uses:

```python
r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
```

For this internship project, this pattern is intended for common email address formats in normal text files.

## Error Handling

The program handles:

- Missing input files
- Non-`.txt` input files
- Invalid UTF-8 text files
- Files containing no email addresses
- Problems writing the output file

## Example Output

```text
services@codealpha.tech
services.codealpha@gmail.com
hr@example.com
support@example.org
developer.team+python@example.co.uk
training.department@example.net
```

## Internship Task Coverage

This project directly covers the selected **CodeAlpha Task 3** automation idea:

- Reads a text file
- Extracts email addresses
- Uses Python's `re` module
- Uses file handling
- Saves the extracted addresses to another file
- Automates a real-life repetitive task

## Author

**Mujahid Sarfraz**  
Python Programming Intern  
CodeAlpha

## Acknowledgment

This project was completed as part of the **CodeAlpha Python Programming Internship**.
