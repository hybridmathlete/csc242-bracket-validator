"""
Author: 9G7WRQ
Date: 10/7/2026

Purpose: Tests the complete bracket validator pipeline using sample files.
Input: Sample source-code files containing different bracket cases.
Output: Expected and actual bracket-check results, followed by the
session history created by the tests.
"""

# =====================================================================
# ASSIGNED TO: Ramina Daood (rdaood8933)
# BRANCH:      test-end-to-end
# REVIEWER:    Benjamin Clark (approves the PR)
# DUE:         PR opened by Sat 10/3; RUN IT TOGETHER in Session 2
#              (Mon 10/5) once every branch is merged
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
    pipeline and stores the result in session history.
    Precondition: file_name is a path to a sample file, expected is
    the exact expected result string, and history is a SessionHistory.
    Postcondition: The file is loaded, checked, and added to the
    session history. The expected and actual results are printed.
    """

    buffer = TextBuffer()

    print(file_name)

    if not buffer.load_file(file_name):
        print(f"  Could not load {file_name}")
        return

    result = check_brackets(buffer.get_lines())

    history.add_check(
        file_name,
        buffer.get_lines(),
        result
    )

    print(f"  Expected: {expected}")
    print(f"  Actual:   {result}")


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
        "samples/deep_nested.py",
        "PASS - All brackets are balanced",
        history
    )

    run_file_case(
        "samples/empty.py",
        "PASS - All brackets are balanced",
        history
    )

    run_file_case(
        "samples/long_last_line.py",
        "FAIL - Mismatch at line 8, col 18: expected ']' but found ')'",
        history
    )

    run_file_case(
        "samples/string_bracket.py",
        "FAIL - Unclosed '(' opened at line 2, col 10",
        history
    )

    print_header("History after all cases")

    expected_count = 8

    print(
        f"Expected history count: {expected_count} | "
        f"Actual: {history.get_count()}"
    )

    print(history.get_summary())

    print("\nDetail for check #7:")
    print(history.format_detail(7))


if __name__ == "__main__":
    main()