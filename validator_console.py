"""
Author: [Your Name]
Date: [Today's Date]

Purpose: [Describe what this program does]

Input: [Describe expected input]

Output: [Describe expected output]
"""

# =====================================================================
# ASSIGNED TO: Andrew Gause (agause7975)
# BRANCH:      feature-console-menu
# REVIEWER:    Ramina Daood (approves the PR)
# DUE:         PR opened by Sat 10/3 (you can write and test it
#              against teammates' branches as they land)
# RUN WITH:    python3 validator_console.py
#
# This is the MAIN PROGRAM. It is where the three structures become one
# program -- the part the rubric's "correct integration" (12 pts) looks
# at hardest. The data flows through all three:
#
#   TextBuffer          -> check_brackets        -> SessionHistory
#   (MyArrayList of        (MyArrayStack of         (MyLinkedList of
#    lines)                 open brackets)           past checks)
#
# The console itself should contain NO bracket logic and NO list
# logic -- it only calls the other modules' public methods.
# =====================================================================

from text_buffer import TextBuffer
from bracket_checker import check_brackets
from session_history import SessionHistory


# ================= GIVEN: DO NOT MODIFY =================
END_MARKER = "END"

MENU = """
==== Bracket & Syntax Validator ====
1) Check typed or pasted text
2) Check a file
3) View session history
4) View a past check in detail
5) Clear history
6) Quit"""


# ================= YOUR IMPLEMENTATION =================


def run_check(buffer, label, history):
    '''
    Precondition: buffer is a loaded TextBuffer; label is a string;
    history is a SessionHistory.
    Postcondition: Checks the buffer's lines, logs the result in
    history, and prints the result with its check number.
    '''
    result = check_brackets(buffer.get_lines())
    entry = history.add_check(label, buffer.get_lines(), result)
    print(f"Check #{entry.check_number}: {result}")


def check_typed_text(history):
    # ASSIGNED TO: Andrew
    #
    # Precondition: history is a SessionHistory.
    # Postcondition: Prints instructions, reads lines with input()
    # until a line equal to END_MARKER, then checks and logs them with
    # the label "typed text". If no lines were entered, prints
    # "No text entered." and logs nothing.
    #
    # HINT: Build a new TextBuffer and add_line() each typed line.
    # A while loop that reads one line before the loop and one at the
    # bottom of the loop avoids adding "END" itself.

    # TODO (Andrew): Replace this comment block with your own
    # docstring, then implement the function below.
    pass


def check_file(history):
    # ASSIGNED TO: Andrew
    #
    # Precondition: history is a SessionHistory.
    # Postcondition: Asks for a file name, loads and checks the file,
    # and logs it with the file name as its label. If the file cannot
    # be read, prints "Could not read '<file name>'." and logs nothing.
    #
    # HINT: TextBuffer.load_file() returns False on failure -- use
    # that instead of your own try / except.

    # TODO (Andrew): Replace this comment block with your own
    # docstring, then implement the function below.
    pass


def view_detail(history):
    # ASSIGNED TO: Andrew
    #
    # Precondition: history is a SessionHistory.
    # Postcondition: If the history is empty, prints "No checks yet.".
    # Otherwise asks for a check number and prints
    # history.format_detail(number). Input that is not a whole number
    # prints "Please enter a whole number." -- the program must never
    # crash on bad input.
    #
    # HINT: str.isdigit() tells you whether int() is safe to call.

    # TODO (Andrew): Replace this comment block with your own
    # docstring, then implement the function below.
    pass


def main():
    # ASSIGNED TO: Andrew
    #
    # Precondition: none.
    # Postcondition: Creates ONE SessionHistory for the whole session
    # and runs the menu loop until the user chooses 6. Choices:
    #   1 -> check_typed_text     2 -> check_file
    #   3 -> print history.get_summary()
    #   4 -> view_detail          5 -> history.clear(), then print
    #                                  "History cleared."
    #   6 -> leave the loop, then print "Goodbye!"
    #   anything else -> print "Invalid choice."
    #
    # HINT: print(MENU), then input("Choose 1-6: ").strip(). Keep the
    # history OUTSIDE the loop, or it will be emptied every time.

    # TODO (Andrew): Replace this comment block with your own
    # docstring, then implement the function below.
    pass


if __name__ == "__main__":
    main()
