"""
Author: Benjamin Clark
Date: October 4, 2026

Purpose: Stores a block of text as a MyArrayList of lines, one string
per line with no newline characters. Text can be loaded from a string
or a file, or built up one line at a time. Lines are looked up by
1-based line number, as the user sees them.

Input: A string, a file name, or individual lines to add.

Output: Individual lines, the line count, the MyArrayList of lines, and
a numbered listing of the text.
"""

from my_array_list import MyArrayList


class TextBuffer:

    def __init__(self):
        """
        Precondition: none.
        Postcondition: Creates an empty TextBuffer (0 lines).
        """
        self._lines = MyArrayList()

    def load_text(self, text):
        """
        Precondition: text is a string whose lines are separated by "\n".
        Postcondition: Replaces the buffer's contents with the lines of
        text, in order. An empty string gives 0 lines, and a single
        trailing "\n" does not create an extra empty line.
        """
        self._lines.clear()
        if text == "":
            return
        if text.endswith("\n"):
            text = text[:-1]
        for line in text.split("\n"):
            self._lines.append(line)

    def load_file(self, file_name):
        """
        Precondition: file_name is a string path to a text file.
        Postcondition: If the file can be read, replaces the buffer's
        contents with its lines and returns True. If it cannot be read,
        the buffer is left unchanged and returns False.
        """
        try:
            with open(file_name, 'r') as in_file:
                text = in_file.read()
        except OSError:
            return False
        self.load_text(text)
        return True

    def add_line(self, line):
        """
        Precondition: line is a string with no newline character.
        Postcondition: line is added as the new last line.
        """
        self._lines.append(line)

    def get_line(self, line_number):
        """
        Precondition: line_number is an integer (1-based).
        Postcondition: Returns the text of that line, or None if
        line_number is out of range (including 0 and negatives).
        """
        return self._lines.get(line_number - 1)

    def get_line_count(self):
        """
        Precondition: none.
        Postcondition: Returns the number of lines stored.
        """
        return self._lines.get_count()

    def get_lines(self):
        """
        Precondition: none.
        Postcondition: Returns the MyArrayList of lines itself, not a
        copy.
        """
        return self._lines

    def __str__(self):
        """
        Precondition: none.
        Postcondition: Returns each line prefixed by its 1-based line
        number (right-aligned in 3 spaces) and " | ", rows separated by
        "\n" with no trailing newline. Returns "(empty)" when there are
        no lines.
        """
        count = self._lines.get_count()
        if count == 0:
            return "(empty)"
        result = ""
        for index in range(count):
            if index > 0:
                result += "\n"
            result += f"{index + 1:>3} | {self._lines.get(index)}"
        return result