"""
Author: [Your Name]
Date: [Today's Date]

Purpose: [Describe what this program does]

Input: [Describe expected input]

Output: [Describe expected output]
"""

# =====================================================================
# ASSIGNED TO: Ramina Daood (rdaood8933)
# BRANCH:      feature-session-history
# REVIEWER:    Benjamin Clark (approves the PR)
# DUE:         PR opened by Sat 10/3
# TEST WITH:   python3 test_session_history.py
#              (compare to expected_output/test_session_history.txt)
# NEEDS:       check_result.py finished (Andrew, merged by Wed 9/30)
#
# SessionHistory is the MyLinkedList part of the project: a log of
# every bracket check run during one session. Each check is stored as
# a HistoryEntry (GIVEN below) at the END of a MyLinkedList, so the log
# reads oldest-to-newest. Check numbers start at 1.
#
# A linked list fits this job: the log only grows at the end
# (add_last is O(1) because MyLinkedList keeps a reference to its last
# node), it is always read in order, and it never needs a fixed
# capacity.
# =====================================================================

from my_linked_list import MyLinkedList
from my_array_list import MyArrayList


# ================= GIVEN: DO NOT MODIFY =================
#
# HistoryEntry bundles everything needed to re-display one past check:
# its number, a label (a file name or "typed text"), the lines that
# were checked (a MyArrayList of strings), and the CheckResult.
class HistoryEntry:
    """Bundles one past check. GIVEN -- do not modify."""

    def __init__(self, check_number, label, lines, result):
        self.check_number = check_number
        self.label = label
        self.lines = lines
        self.result = result


# ================= YOUR IMPLEMENTATION =================


class SessionHistory:

    def __init__(self):
        # ASSIGNED TO: Ramina
        #
        # Precondition: none.
        # Postcondition: Creates an empty history. The first check
        # added will be check #1.
        #
        # HINT: Two attributes: self._entries (a new MyLinkedList) and
        # self._next_number (the number the NEXT check will get).

        # TODO (Ramina): Replace this comment block with your own
        # docstring, then implement the method below.
        pass

    def add_check(self, label, lines, result):
        # ASSIGNED TO: Ramina
        #
        # Precondition: label is a string; lines is a MyArrayList of
        # strings; result is a CheckResult.
        # Postcondition: Adds a new HistoryEntry to the END of the log,
        # numbered with the next check number, and RETURNS that entry.
        # The lines must be saved as a DEEP COPY, so that if the caller
        # changes its own MyArrayList later, the saved history does not
        # change.
        #
        # HINT:
        # - Deep copy: create a new MyArrayList and call its copy_list()
        #   with the caller's list (see my_array_list.py).
        # - Build the HistoryEntry, add_last() it, then move
        #   self._next_number forward.
        #
        # WATCH OUT: copy_list() on an EMPTY list leaves the copy with
        # capacity 0, so never append() to a saved copy afterward.

        # TODO (Ramina): Replace this comment block with your own
        # docstring, then implement the method below.
        return None

    def get_count(self):
        # ASSIGNED TO: Ramina
        #
        # Precondition: none.
        # Postcondition: Returns how many checks are in the log.

        # TODO (Ramina): Replace this comment block with your own
        # docstring, then implement the method below.
        return 0

    def is_empty(self):
        # ASSIGNED TO: Ramina
        #
        # Precondition: none.
        # Postcondition: Returns True if no checks have been logged.

        # TODO (Ramina): Replace this comment block with your own
        # docstring, then implement the method below.
        return True

    def get_entry(self, check_number):
        # ASSIGNED TO: Ramina
        #
        # Precondition: check_number is an integer.
        # Postcondition: Returns the HistoryEntry whose check_number
        # matches, or None if there is no such check.
        #
        # HINT: Walk the list with get_count() + get_at(index) (the same
        # pattern MyHashTable used in Lab 6) and compare
        # entry.check_number. Do not assume check #n is at index n - 1.

        # TODO (Ramina): Replace this comment block with your own
        # docstring, then implement the method below.
        return None

    def get_summary(self):
        # ASSIGNED TO: Ramina
        #
        # Precondition: none.
        # Postcondition: Returns one row per check, oldest first, rows
        # separated by "\n" (no trailing newline). Returns
        # "No checks yet." when the log is empty. Row format:
        #     "#<number>  <label> (<line count> lines)  <result>"
        # Example:
        #     "#2  samples/mismatch.py (2 lines)  FAIL - Mismatch at ..."
        #
        # HINT: <result> is just str(entry.result) -- CheckResult's
        # __str__ already adds "PASS - " / "FAIL - ". Note the TWO
        # spaces after the number and before the result.

        # TODO (Ramina): Replace this comment block with your own
        # docstring, then implement the method below.
        return ""

    def format_detail(self, check_number):
        # ASSIGNED TO: Ramina
        #
        # Precondition: check_number is an integer.
        # Postcondition: Returns a multi-line string that re-displays
        # one past check, or "No check #<n>." if it does not exist.
        # Format:
        #     Check #2: samples/mismatch.py
        #       1 | def f(x):
        #       2 |     return [x * (2 + 3]
        #                                 ^
        #     FAIL - Mismatch at line 2, col 23: expected ')' but found ']'
        # - First row: "Check #<number>: <label>"
        # - Then every saved line as f"{line_number:>3} | {text}"
        # - For a FAILED check only: directly under the problem line,
        #   a row with a "^" under the problem column.
        # - Last row: str(entry.result)
        #
        # HINT: The prefix "  1 | " is 6 characters wide, so the caret
        # row is (6 + column - 1) spaces followed by "^".

        # TODO (Ramina): Replace this comment block with your own
        # docstring, then implement the method below.
        return ""

    def clear(self):
        # ASSIGNED TO: Ramina
        #
        # Precondition: none.
        # Postcondition: Removes every entry. Numbering restarts at 1.

        # TODO (Ramina): Replace this comment block with your own
        # docstring, then implement the method below.
        pass
