"""
Author: Benjamin Clark
Date: October 4, 2026

Purpose: Checks that every (, [ and { in a block of text is closed by
the matching ), ] or } in the right order. A MyArrayStack holds the
brackets that are open but not yet closed, so the most recently opened
bracket must be the first one closed. The check stops at the first
problem and reports its 1-based line and column.

Input: A MyArrayList of strings, one per line of text.

Output: A CheckResult for one of four outcomes: balanced, mismatch,
unexpected closer, or unclosed opener.
"""

from my_array_stack import MyArrayStack
from check_result import CheckResult


# OPENERS[i] is matched by CLOSERS[i]: ( with ), [ with ], { with }.
OPENERS = "([{"
CLOSERS = ")]}"


def _is_opener(ch):
    """
    Precondition: ch is a single character.
    Postcondition: Returns True if ch is (, [, or {; False otherwise.
    """
    return ch in OPENERS


def _is_closer(ch):
    """
    Precondition: ch is a single character.
    Postcondition: Returns True if ch is ), ], or }; False otherwise.
    """
    return ch in CLOSERS


def _matching_closer(opener):
    """
    Precondition: opener is one of (, [, {.
    Postcondition: Returns the closer that matches opener.
    """
    return CLOSERS[OPENERS.index(opener)]


def check_brackets(lines):
    """
    Precondition: lines is a MyArrayList of strings (one per line).
    Postcondition: Returns a CheckResult. Scans every character in order
    and stops at the first problem. For a failed check, line_number and
    column are where the problem is (for an unclosed opener, where it
    was opened). For a balanced check, both are 0.
    """
    stack = MyArrayStack()

    for line_index in range(lines.get_count()):
        line = lines.get(line_index)
        line_number = line_index + 1
        for char_index in range(len(line)):
            ch = line[char_index]
            column = char_index + 1
            if _is_opener(ch):
                stack.push((ch, line_number, column))
            elif _is_closer(ch):
                if stack.is_empty_stack():
                    return CheckResult(
                        False, line_number, column,
                        f"Unexpected '{ch}' at line {line_number}, "
                        f"col {column}: no bracket is open")
                open_ch, open_line, open_col = stack.get_top()
                expected = _matching_closer(open_ch)
                if ch != expected:
                    return CheckResult(
                        False, line_number, column,
                        f"Mismatch at line {line_number}, col {column}: "
                        f"expected '{expected}' but found '{ch}'")
                stack.pop()

    if not stack.is_empty_stack():
        open_ch, open_line, open_col = stack.get_top()
        return CheckResult(
            False, open_line, open_col,
            f"Unclosed '{open_ch}' opened at line {open_line}, "
            f"col {open_col}")
    return CheckResult(True, 0, 0, "All brackets are balanced")