"""
Author: [Your Name]
Date: [Today's Date]

Purpose: [Describe what this program does]

Input: [Describe expected input]

Output: [Describe expected output]
"""

# =====================================================================
# ASSIGNED TO: Benjamin Clark (bclark2799)
# BRANCH:      feature-bracket-checker
# REVIEWER:    Andrew Gause (approves the PR)
# DUE:         PR opened by Sat 10/3
# TEST WITH:   python3 test_bracket_checker.py
#              (compare to expected_output/test_bracket_checker.txt)
# NEEDS:       check_result.py finished (Andrew, merged by Wed 9/30)
#
# This is the MyArrayStack part of the project -- the core algorithm.
# It checks that every (, [, { is closed by the matching ), ], } in the
# right order, and reports the line and column of the FIRST problem.
#
# Why a stack? Brackets nest: the most recently OPENED bracket must be
# the first one CLOSED. That is last-in, first-out.
#
# There are exactly four possible outcomes. Your messages must match
# these formats EXACTLY (the tests compare the text):
#   1. Balanced:   "All brackets are balanced"
#   2. Mismatch:   "Mismatch at line L, col C: expected 'X' but found 'Y'"
#                  (a closer that does not match the latest opener)
#   3. Unexpected: "Unexpected 'Y' at line L, col C: no bracket is open"
#                  (a closer when the stack is empty)
#   4. Unclosed:   "Unclosed 'X' opened at line L, col C"
#                  (text ends while an opener is still on the stack --
#                   report the one on TOP, at the position it OPENED)
# Line and column numbers are 1-BASED.
# =====================================================================

from my_array_stack import MyArrayStack
from check_result import CheckResult


# ================= GIVEN: DO NOT MODIFY =================
#
# OPENERS[i] is matched by CLOSERS[i]: ( with ), [ with ], { with }.
OPENERS = "([{"
CLOSERS = ")]}"


# ================= YOUR IMPLEMENTATION =================


def _is_opener(ch):
    # ASSIGNED TO: Benjamin
    #
    # Precondition: ch is a single character.
    # Postcondition: Returns True if ch is (, [, or {; False otherwise.
    #
    # HINT: The "in" operator works on strings.

    # TODO (Benjamin): Replace this comment block with your own
    # docstring, then implement the function below.
    return False


def _is_closer(ch):
    # ASSIGNED TO: Benjamin
    #
    # Precondition: ch is a single character.
    # Postcondition: Returns True if ch is ), ], or }; False otherwise.

    # TODO (Benjamin): Replace this comment block with your own
    # docstring, then implement the function below.
    return False


def _matching_closer(opener):
    # ASSIGNED TO: Benjamin
    #
    # Precondition: opener is one of (, [, {.
    # Postcondition: Returns the closer that matches opener.
    #
    # HINT: Find opener's position in OPENERS (str.index), then return
    # the character at the SAME position in CLOSERS.

    # TODO (Benjamin): Replace this comment block with your own
    # docstring, then implement the function below.
    return ""


def check_brackets(lines):
    # ASSIGNED TO: Benjamin
    #
    # Precondition: lines is a MyArrayList of strings (one per line).
    # Postcondition: Returns a CheckResult. Scans every character of
    # every line in order and STOPS at the first problem. For a failed
    # check, line_number and column are where the problem is (for an
    # unclosed opener: where that opener was opened). For a balanced
    # check, line_number and column are both 0.
    #
    # HINT:
    # - Create one MyArrayStack.
    # - Outer loop over line indexes 0 .. lines.get_count() - 1
    #   (lines.get(index) gives the string). Inner loop over the
    #   character positions of that line. Convert BOTH to 1-based
    #   numbers before you store or report them.
    # - Opener: push a TUPLE (ch, line_number, column) -- you need the
    #   position later if this opener is never closed.
    # - Closer:
    #     - Stack empty?  -> return the "Unexpected" CheckResult.
    #     - Otherwise read the top tuple, e.g.
    #           open_ch, open_line, open_col = stack.get_top()
    #       If ch is not _matching_closer(open_ch) -> return the
    #       "Mismatch" CheckResult. Otherwise pop() -- that pair is
    #       done.
    # - Any other character: ignore it.
    # - After both loops: if the stack is not empty, return the
    #   "Unclosed" CheckResult using the TOP tuple. Otherwise return
    #   CheckResult(True, 0, 0, "All brackets are balanced").
    #
    # WATCH OUT:
    # - pop() does NOT return a value in our MyArrayStack. Always call
    #   get_top() FIRST, then pop().
    # - get_top() on an EMPTY stack crashes -- check is_empty_stack()
    #   before calling it.

    # TODO (Benjamin): Replace this comment block with your own
    # docstring, then implement the function below.
    return CheckResult(True, 0, 0, "")
