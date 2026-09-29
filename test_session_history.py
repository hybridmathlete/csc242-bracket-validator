"""
Author: Provided Test Driver -- do not modify
Date: Fall 2026

Purpose: Test driver for SessionHistory (session_history.py --
Ramina). Tests adding checks, numbering, lookup by check number, the
deep copy of saved lines, the summary, the detail view with its ^
marker, and clear. Builds CheckResults directly, so it does NOT depend
on the bracket checker or TextBuffer.

Input: none (all test data is defined in this file)

Output: printed test results -- compare line-by-line against
expected_output/test_session_history.txt
"""

from my_array_list import MyArrayList
from check_result import CheckResult
from session_history import SessionHistory


def print_header(title):
    print("\n==============================")
    print(title)
    print("==============================")


def label_of(entry):
    if entry is None:
        return None
    return entry.label


def main():
    print("CSC 242 Group 2 - Session History Test Driver")

    passed = CheckResult(True, 0, 0, "All brackets are balanced")
    failed = CheckResult(False, 2, 23,
                         "Mismatch at line 2, col 23: expected ')' but found ']'")

    print_header("New history")
    history = SessionHistory()
    print(f"Expected count: 0 | Actual: {history.get_count()}")
    print(f"Expected is_empty: True | Actual: {history.is_empty()}")
    print(f"Expected summary: No checks yet. | Actual: {history.get_summary()}")
    print(f"Expected detail(1): No check #1. | Actual: {history.format_detail(1)}")

    print_header("add_check")
    lines_one = MyArrayList.from_array(["(ok)"])
    lines_two = MyArrayList.from_array(["def f(x):", "    return [x * (2 + 3]"])
    entry = history.add_check("typed text", lines_one, passed)
    print(f"Expected returned entry number: 1 | Actual: {entry.check_number if entry else None}")
    entry = history.add_check("samples/mismatch.py", lines_two, failed)
    print(f"Expected returned entry number: 2 | Actual: {entry.check_number if entry else None}")
    print(f"Expected count: 2 | Actual: {history.get_count()}")
    print(f"Expected is_empty: False | Actual: {history.is_empty()}")

    print_header("get_entry")
    print(f"Expected get_entry(1) label: typed text | Actual: {label_of(history.get_entry(1))}")
    print(f"Expected get_entry(2) label: samples/mismatch.py | Actual: {label_of(history.get_entry(2))}")
    print(f"Expected get_entry(3): None | Actual: {label_of(history.get_entry(3))}")
    print(f"Expected get_entry(0): None | Actual: {label_of(history.get_entry(0))}")

    print_header("Saved lines are a deep copy")
    lines_one.set_at(0, "CHANGED")
    entry = history.get_entry(1)
    saved = entry.lines.get(0) if entry else None
    print(f"Expected saved line of #1: (ok) | Actual: {saved}")

    print_header("get_summary")
    print("Expected:")
    print("#1  typed text (1 lines)  PASS - All brackets are balanced")
    print("#2  samples/mismatch.py (2 lines)  FAIL - Mismatch at line 2, col 23: expected ')' but found ']'")
    print("Actual:")
    print(history.get_summary())

    print_header("format_detail (failed check)")
    print("Expected:")
    print("Check #2: samples/mismatch.py")
    print("  1 | def f(x):")
    print("  2 |     return [x * (2 + 3]")
    print("                            ^")
    print("FAIL - Mismatch at line 2, col 23: expected ')' but found ']'")
    print("Actual:")
    print(history.format_detail(2))

    print_header("format_detail (passed check -- no ^ marker)")
    print("Expected:")
    print("Check #1: typed text")
    print("  1 | (ok)")
    print("PASS - All brackets are balanced")
    print("Actual:")
    print(history.format_detail(1))

    print_header("clear")
    history.clear()
    print(f"Expected count: 0 | Actual: {history.get_count()}")
    entry = history.add_check("after clear", MyArrayList.from_array(["()"]), passed)
    print(f"Numbering restarts -- Expected entry number: 1 | Actual: {entry.check_number if entry else None}")


if __name__ == "__main__":
    main()
