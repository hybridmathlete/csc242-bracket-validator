"""
Author: Provided Test Driver -- do not modify
Date: Fall 2026

Purpose: Test driver for TextBuffer (text_buffer.py -- Benjamin).
Tests loading text (including the empty-string and trailing-newline
cases), 1-based line lookup with out-of-range lines, add_line,
load_file on a real and a missing file, and __str__.

Input: none (test data is defined in this file and in samples/)

Output: printed test results -- compare line-by-line against
expected_output/test_text_buffer.txt
"""

from text_buffer import TextBuffer


def print_header(title):
    print("\n==============================")
    print(title)
    print("==============================")


def main():
    print("CSC 242 Group 2 - TextBuffer Test Driver")

    print_header("New buffer")
    buffer = TextBuffer()
    print(f"Expected line count: 0 | Actual: {buffer.get_line_count()}")
    print(f"Expected str: (empty) | Actual: {buffer}")

    print_header("load_text")
    buffer.load_text("first\nsecond\nthird")
    print(f"Expected line count: 3 | Actual: {buffer.get_line_count()}")
    print(f"Expected get_line(1): first | Actual: {buffer.get_line(1)}")
    print(f"Expected get_line(3): third | Actual: {buffer.get_line(3)}")
    print(f"Expected get_line(0): None | Actual: {buffer.get_line(0)}")
    print(f"Expected get_line(4): None | Actual: {buffer.get_line(4)}")
    print(f"Expected get_line(-1): None | Actual: {buffer.get_line(-1)}")

    print_header("load_text replaces old contents")
    buffer.load_text("only line")
    print(f"Expected line count: 1 | Actual: {buffer.get_line_count()}")
    print(f"Expected get_line(1): only line | Actual: {buffer.get_line(1)}")

    print_header("load_text special cases")
    buffer.load_text("a\nb\n")
    print(f"Trailing newline -- Expected line count: 2 | Actual: {buffer.get_line_count()}")
    buffer.load_text("")
    print(f"Empty string -- Expected line count: 0 | Actual: {buffer.get_line_count()}")
    buffer.load_text("a\n\nc")
    print(f"Blank middle line -- Expected line count: 3 | Actual: {buffer.get_line_count()}")
    print(f"Expected get_line(2): '' | Actual: '{buffer.get_line(2)}'")

    print_header("add_line")
    buffer = TextBuffer()
    buffer.add_line("x = (1")
    buffer.add_line("+ 2)")
    print(f"Expected line count: 2 | Actual: {buffer.get_line_count()}")
    print(f"Expected get_line(2): + 2) | Actual: {buffer.get_line(2)}")
    print(f"Expected get_lines().get(0): x = (1 | Actual: {buffer.get_lines().get(0)}")

    print_header("load_file")
    buffer = TextBuffer()
    print(f"Expected load_file(samples/mismatch.py): True | Actual: {buffer.load_file('samples/mismatch.py')}")
    print(f"Expected line count: 2 | Actual: {buffer.get_line_count()}")
    print(f"Expected load_file(no_such_file.txt): False | Actual: {buffer.load_file('no_such_file.txt')}")
    print(f"Buffer unchanged after failed load -- Expected line count: 2 | Actual: {buffer.get_line_count()}")

    print_header("__str__")
    print("Expected:")
    print("  1 | def f(x):")
    print("  2 |     return [x * (2 + 3]")
    print("Actual:")
    print(buffer)


if __name__ == "__main__":
    main()
