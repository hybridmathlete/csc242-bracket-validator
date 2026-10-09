"""
Author: 9G7WRQ
Date: 10/7/2026

Purpose: Tests the file-validation pipeline by checking that TextBuffer,
check_brackets, and SessionHistory work together.
Input: Sample files containing different bracket cases.
Output: Expected and actual results, test status, and session history.
"""

# =====================================================================
# ASSIGNED TO: Ramina Daood (rdaood8933)
# BRANCH:      test-end-to-end
# REVIEWER:    Benjamin Clark (approves the PR)
# RUN WITH:    python3 test_end_to_end.py
# =====================================================================

from text_buffer import TextBuffer
from bracket_checker import check_brackets
from session_history import SessionHistory


def print_header(title):
    print("\n==============================")
    print(title)
    print("==============================")


def run_file_case(file_name, expected, history):
    """
    Purpose: Runs one sample file through the complete validation
    pipeline and saves the result in session history.
    Precondition: file_name is a sample file path, expected is the
    expected result string, and history is a SessionHistory.
    Postcondition: Loads and checks the file, saves the result in
    history, and prints the expected and actual results. If the file
    cannot be loaded, prints an error and does not save a check.
    """

    buffer = TextBuffer()

    print(f"\nFile: {file_name}")

    if not buffer.load_file(file_name):
        print(f"  Could not load {file_name}")
        return

    result = check_brackets(buffer.get_lines())
    actual = str(result)

    history.add_check(
        file_name,
        buffer.get_lines(),
        result
    )

    print(f"  Expected: {expected}")
    print(f"  Actual:   {actual}")

    if actual == expected:
        print("  Test status: PASS")
    else:
        print("  Test status: FAIL")


def main():
    print("CSC 242 Group 2 - End-to-End Test Driver")

    history = SessionHistory()

    print_header("Given cases: one per outcome")

    run_file_case(
        "samples/balanced.py",
        "PASS - All brackets are balanced",
        history
    )

    run_file_case(
        "samples/mismatch.py",
        "FAIL - Mismatch at line 2, col 23: expected ')' but found ']'",
        history
    )

    run_file_case(
        "samples/unclosed.py",
        "FAIL - Unclosed '{' opened at line 2, col 12",
        history
    )

    run_file_case(
        "samples/unexpected.py",
        "FAIL - Unexpected ')' at line 1, col 16: no bracket is open",
        history
    )

    print_header("Ramina's cases")

    run_file_case(
        "samples/deep_nesting.py",
        "PASS - All brackets are balanced",
        history
    )

    run_file_case(
        "samples/empty.py",
        "PASS - All brackets are balanced",
        history
    )

    run_file_case(
        "samples/last_line_error.py",
        "FAIL - Mismatch at line 8, col 18: expected ']' but found ')'",
        history
    )

    run_file_case(
        "samples/bracket_in_string.py",
        "FAIL - Unclosed '(' opened at line 2, col 10",
        history
    )

    print_header("History after all cases")

    expected_count = 8
    actual_count = history.get_count()

    print(
        f"Expected history count: {expected_count} | "
        f"Actual: {actual_count}"
    )

    print(history.get_summary())

    print("\nDetail for check #7:")
    print(history.format_detail(7))


if __name__ == "__main__":
    main()