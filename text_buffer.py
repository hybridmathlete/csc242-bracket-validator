"""
Author: [Your Name]
Date: [Today's Date]

Purpose: [Describe what this program does]

Input: [Describe expected input]

Output: [Describe expected output]
"""

# =====================================================================
# ASSIGNED TO: Benjamin Clark (bclark2799)
# BRANCH:      feature-text-buffer
# REVIEWER:    Andrew Gause (approves the PR)
# DUE:         PR opened by Sat 10/3
# TEST WITH:   python3 test_text_buffer.py
#              (compare to expected_output/test_text_buffer.txt)
#
# TextBuffer stores a block of text as a MyArrayList of lines -- one
# string per line, with NO newline characters. This is the MyArrayList
# part of the project.
#
# IMPORTANT -- line numbers:
# - The USER sees 1-based line numbers (the first line is line 1).
# - The MyArrayList underneath is 0-based (the first line is index 0).
# - So line n is stored at index n - 1. Every method that takes a
#   line_number must convert it.
# =====================================================================

from my_array_list import MyArrayList


class TextBuffer:

    def __init__(self):
        # ASSIGNED TO: Benjamin
        #
        # Precondition: none.
        # Postcondition: Creates an empty TextBuffer (0 lines).
        #
        # HINT: One attribute is enough: self._lines, a new, empty
        # MyArrayList.

        # TODO (Benjamin): Replace this comment block with your own
        # docstring, then implement the method below.
        pass

    def load_text(self, text):
        # ASSIGNED TO: Benjamin
        #
        # Precondition: text is a string whose lines are separated by
        # "\n".
        # Postcondition: REPLACES the buffer's contents with the lines
        # of text, in order.
        #   - An empty string gives 0 lines (not 1 empty line).
        #   - A single trailing "\n" does NOT create an extra empty
        #     line: "a\nb\n" is 2 lines, not 3.
        #
        # HINT:
        # - Start by clearing the old contents (MyArrayList has clear()).
        # - Handle the two special cases above BEFORE splitting.
        #   text.endswith("\n") and slicing (text[:-1]) help here.
        # - text.split("\n") gives you each line; append() each one to
        #   self._lines. (The temporary Python list from split() is fine
        #   -- the STORED lines must live in the MyArrayList.)

        # TODO (Benjamin): Replace this comment block with your own
        # docstring, then implement the method below.
        pass

    def load_file(self, file_name):
        # ASSIGNED TO: Benjamin
        #
        # Precondition: file_name is a string path to a text file.
        # Postcondition: If the file can be read, replaces the buffer's
        # contents with the file's lines and returns True. If the file
        # cannot be read (missing, no permission, ...), the buffer is
        # left UNCHANGED and returns False -- the program must not crash.
        #
        # HINT:
        # - Read the whole file into a string inside a try / except
        #   OSError block (use "with open(file_name, 'r') as in_file:").
        # - Reuse load_text() -- do not write the splitting logic twice.

        # TODO (Benjamin): Replace this comment block with your own
        # docstring, then implement the method below.
        return False

    def add_line(self, line):
        # ASSIGNED TO: Benjamin
        #
        # Precondition: line is a string with no newline character.
        # Postcondition: line is added as the new LAST line.
        #
        # HINT: The console uses this to build a buffer one typed line
        # at a time. One line of code.

        # TODO (Benjamin): Replace this comment block with your own
        # docstring, then implement the method below.
        pass

    def get_line(self, line_number):
        # ASSIGNED TO: Benjamin
        #
        # Precondition: line_number is an integer (1-BASED).
        # Postcondition: Returns the text of that line, or None if
        # line_number is out of range (including 0 and negatives).
        #
        # HINT: Look at what MyArrayList.get() already returns for an
        # out-of-range index -- you may not need an if statement at all.
        # Remember to convert line_number to an index.

        # TODO (Benjamin): Replace this comment block with your own
        # docstring, then implement the method below.
        return None

    def get_line_count(self):
        # ASSIGNED TO: Benjamin
        #
        # Precondition: none.
        # Postcondition: Returns the number of lines stored.

        # TODO (Benjamin): Replace this comment block with your own
        # docstring, then implement the method below.
        return 0

    def get_lines(self):
        # ASSIGNED TO: Benjamin
        #
        # Precondition: none.
        # Postcondition: Returns the MyArrayList of lines ITSELF (not a
        # copy). The bracket checker and the session history both take
        # this MyArrayList as input.

        # TODO (Benjamin): Replace this comment block with your own
        # docstring, then implement the method below.
        return MyArrayList()

    def __str__(self):
        # ASSIGNED TO: Benjamin
        #
        # Precondition: none.
        # Postcondition: Returns every line prefixed by its 1-based line
        # number, right-aligned in 3 spaces, then " | ", one line per
        # row, rows separated by "\n" (no trailing newline). Returns
        # "(empty)" when there are no lines. Example for 2 lines:
        #     "  1 | def f(x):\n  2 |     return x"
        #
        # HINT: f"{line_number:>3} | {text}" produces one row. Build
        # the result the same way MyArrayStack.__str__ does (start with
        # "" and add "\n" BETWEEN rows).

        # TODO (Benjamin): Replace this comment block with your own
        # docstring, then implement the method below.
        return ""
