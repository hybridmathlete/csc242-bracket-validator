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
    '''
    Precondition: history is a SessionHistory.
    Postcondition: Reads lines until END, then checks and logs them.
    Nothing is logged if no lines were entered.
    '''
    print(f"Type your text. Enter {END_MARKER} on its own line "
          "to finish.")
    buffer = TextBuffer()
    line = input()
    while line != END_MARKER:
        buffer.add_line(line)
        line = input()
    if buffer.get_line_count() == 0:
        print("No text entered.")
        return
    run_check(buffer, "typed text", history)


def check_file(history):
    '''
    Precondition: history is a SessionHistory.
    Postcondition: If the file cannot be read it prints an error. Otherwise,
    it reads a file name, loads and checks the file, and logs the result.
    '''
    file_name = input("File name: ").strip()
    buffer = TextBuffer()
    if not buffer.load_file(file_name):
        print(f"Could not read '{file_name}'.")
        return
    run_check(buffer, file_name, history)


def view_detail(history):
    '''
    Precondition: history is a SessionHistory.
    Postcondition: Reads a check number and prints that check in
    detail. Prints an error for input that is not a whole number.
    '''
    if history.is_empty():
        print("No checks yet.")
        return
    choice = input("Check number: ").strip()
    if not choice.isdigit():
        print("Please enter a whole number.")
        return
    print(history.format_detail(int(choice)))


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
