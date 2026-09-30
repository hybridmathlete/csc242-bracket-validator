"""
Author: Provided Test Driver -- do not modify
Date: Fall 2026

Purpose: Test driver for check_brackets (bracket_checker.py --
Benjamin). Tests all four outcomes (balanced, mismatch, unexpected
closer, unclosed opener), multi-line input, and edge cases. Builds its
input with MyArrayList.from_array, so it does NOT depend on TextBuffer.

Input: none (all test data is defined in this file)

Output: printed test results -- compare line-by-line against
expected_output/test_bracket_checker.txt
"""

from my_array_list import MyArrayList
from bracket_checker import check_brackets


def print_header(title):
    print("\n==============================")
    print(title)
    print("==============================")


def run_case(lines, expected):
    result = check_brackets(MyArrayList.from_array(lines))
    print(f"Input lines: {lines}")
    print(f"  Expected: {expected}")
    print(f"  Actual:   {result}")
    return result


def main():
    print("CSC 242 Group 2 - Bracket Checker Test Driver")

    print_header("Outcome 1: Balanced")
    run_case(["(a[b]{c})"], "PASS - All brackets are balanced")
    run_case(["no brackets here"], "PASS - All brackets are balanced")
    run_case([], "PASS - All brackets are balanced")
    run_case(["def f(x):", "    return [x, {1: (2)}]"], "PASS - All brackets are balanced")
    result = run_case(["()"], "PASS - All brackets are balanced")
    print(f"Balanced result -- Expected line_number, column: 0, 0 | Actual: {result.line_number}, {result.column}")

    print_header("Outcome 2: Mismatch")
    run_case(["(]"], "FAIL - Mismatch at line 1, col 2: expected ')' but found ']'")
    run_case(["{[}]"], "FAIL - Mismatch at line 1, col 3: expected ']' but found '}'")
    run_case(["x = [1, (2", ", 3]"], "FAIL - Mismatch at line 2, col 4: expected ')' but found ']'")
    result = run_case(["def f(x):", "    return [x * (2 + 3]"],
                      "FAIL - Mismatch at line 2, col 23: expected ')' but found ']'")
    print(f"Expected is_balanced: False | Actual: {result.is_balanced}")
    print(f"Expected line_number, column: 2, 23 | Actual: {result.line_number}, {result.column}")

    print_header("Outcome 3: Unexpected closer")
    run_case(["a)"], "FAIL - Unexpected ')' at line 1, col 2: no bracket is open")
    run_case(["()", "]"], "FAIL - Unexpected ']' at line 2, col 1: no bracket is open")
    run_case(["total = (4 + 5))"], "FAIL - Unexpected ')' at line 1, col 16: no bracket is open")

    print_header("Outcome 4: Unclosed opener")
    run_case(["{a", "b"], "FAIL - Unclosed '{' opened at line 1, col 1")
    run_case(["((", ")"], "FAIL - Unclosed '(' opened at line 1, col 1")
    result = run_case(["[ok]", "x = ( [ ]"], "FAIL - Unclosed '(' opened at line 2, col 5")
    print(f"Expected line_number, column: 2, 5 | Actual: {result.line_number}, {result.column}")

    print_header("First problem wins")
    run_case([")", "(]"], "FAIL - Unexpected ')' at line 1, col 1: no bracket is open")


if __name__ == "__main__":
    main()
