"""
CodeAlpha Python Programming Internship
Task 3: Task Automation with Python Scripts

Email Extractor Automation:
Read a text file, extract email addresses, remove duplicates,
and save the results to another text file.
"""

import re
from pathlib import Path

EMAIL_PATTERN = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)


def extract_emails(text):
    """Return unique email addresses in the order they first appear."""
    emails = EMAIL_PATTERN.findall(text)
    unique_emails = []
    seen = set()

    for email in emails:
        key = email.lower()
        if key not in seen:
            seen.add(key)
            unique_emails.append(email)

    return unique_emails


def read_text_file(file_path):
    """Read UTF-8 text from a file."""
    try:
        return file_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"\nError: '{file_path.name}' was not found.")
    except UnicodeDecodeError:
        print(f"\nError: '{file_path.name}' is not a valid UTF-8 text file.")
    except OSError as error:
        print(f"\nError while reading the file: {error}")

    return None


def save_emails(emails, output_path):
    """Save one email address per line."""
    try:
        output_path.write_text("\n".join(emails) + "\n", encoding="utf-8")
        return True
    except OSError as error:
        print(f"\nError while saving the output file: {error}")
        return False


def main():
    print("=" * 50)
    print("          EMAIL EXTRACTOR AUTOMATION")
    print("=" * 50)

    default_input = "sample_input.txt"
    default_output = "extracted_emails.txt"

    input_name = input(
        f"\nEnter input file name [{default_input}]: "
    ).strip() or default_input

    input_path = Path(input_name)

    if input_path.suffix.lower() != ".txt":
        print("\nPlease provide a .txt file.")
        return

    text = read_text_file(input_path)
    if text is None:
        return

    emails = extract_emails(text)

    if not emails:
        print("\nNo email addresses were found in the file.")
        return

    print("\nExtracted Email Addresses")
    print("-" * 40)
    for number, email in enumerate(emails, start=1):
        print(f"{number}. {email}")
    print("-" * 40)

    output_name = input(
        f"\nEnter output file name [{default_output}]: "
    ).strip() or default_output

    if not output_name.lower().endswith(".txt"):
        output_name += ".txt"

    output_path = Path(output_name)

    if save_emails(emails, output_path):
        print(
            f"\nSuccess: {len(emails)} unique email address(es) "
            f"saved to '{output_path.name}'."
        )


if __name__ == "__main__":
    main()
