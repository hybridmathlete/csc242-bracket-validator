"""
Author: 9G7WRQ
Date: 10/6/2026
Purpose: Stores and displays the history of bracket checks 
during a session.
Input: Check labels, source-code lines, and CheckResult objects.
Output: History entries, check counts, summaries, and formatted details.
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
        """
        Purpose: Creates an empty session history.
        Precondition: None.
        Postcondition: The history is empty and the next check number
        is set to 1.
        """
        self._entries = MyLinkedList()
        self._next_number = 1

    def add_check(self, label, lines, result):
        """
        Purpose: Adds a bracket check to the end of the session history.
        Precondition: label is a string, lines is a MyArrayList of
        strings, and result is a CheckResult.
        Postcondition: A new HistoryEntry is added to the end of the
        history with the next check number. The lines are saved as a
        deep copy, the next check number is increased by 1, and the
        new HistoryEntry is returned.
        """
        saved_lines = MyArrayList()
        saved_lines.copy_list(lines)

        entry = HistoryEntry(
            self._next_number,
            label,
            saved_lines,
            result
        )

        self._entries.add_last(entry)
        self._next_number += 1

        return entry

    def get_count(self):
        """
        Purpose: Gets the number of checks stored in the session history.
        Precondition: None.
        Postcondition: Returns the number of checks currently stored.
        """
        return self._entries.get_count()

    def is_empty(self):
        """
        Purpose: Determines whether the session history is empty.
        Precondition: None.
        Postcondition: Returns True if no checks are stored; otherwise,
        returns False.
        """
        return self._entries.is_empty()

    def get_entry(self, check_number):
        """
        Purpose: Finds a history entry using its check number.
        Precondition: check_number is an integer.
        Postcondition: Returns the HistoryEntry with the matching check
        number, or None if no matching entry exists.
        """
        for index in range(self._entries.get_count()):
            entry = self._entries.get_at(index)

            if entry.check_number == check_number:
                return entry

        return None

    def get_summary(self):
        """
        Purpose: Creates a summary of all checks in the session history.
        Precondition: None.
        Postcondition: Returns one summary row for each check in
        oldest-to-newest order, separated by newline characters. If the
        history is empty, returns "No checks yet.".
        """
        if self.is_empty():
            return "No checks yet."

        rows = []

        for index in range(self._entries.get_count()):
            entry = self._entries.get_at(index)

            row = (
                f"#{entry.check_number}  "
                f"{entry.label} ({entry.lines.get_count()} lines)  "
                f"{entry.result}"
            )

            rows.append(row)

        return "\n".join(rows)

    def format_detail(self, check_number):
        """
        Purpose: Formats one saved check with its source lines and result.
        Precondition: check_number is an integer.
        Postcondition: Returns a multi-line string containing the selected
        check's number, label, saved lines, and result. A caret is included
        under the problem column when the check failed. If the check does
        not exist, returns "No check #<n>.".
        """
        entry = self.get_entry(check_number)

        if entry is None:
            return f"No check #{check_number}."

        rows = [f"Check #{entry.check_number}: {entry.label}"]

        for index in range(entry.lines.get_count()):
            line_number = index + 1
            line = entry.lines.get(index)

            rows.append(f"{line_number:>3} | {line}")

            if (
                not entry.result.is_balanced
                and line_number == entry.result.line_number
            ):
                spaces = 6 + entry.result.column - 1
                rows.append(" " * spaces + "^")

        rows.append(str(entry.result))

        return "\n".join(rows)

    def clear(self):
        """
        Purpose: Removes all checks from the session history.
        Precondition: None.
        Postcondition: The history is empty and the next check number
        is reset to 1.
        """
        self._entries.clear()
        self._next_number = 1