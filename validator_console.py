"""
Author: AU75ZB
Date: 10/2/2026

Purpose: This is the main program. It is where the three structures
become one program. This program ties the three modules together into one
interactive console:
  TextBuffer (MyArrayList of lines)
    -> check_brackets (MyArrayStack of open brackets)
    -> SessionHistory (MyLinkedList of past checks)
Every check the user runs is stored in the history, and any past check
can be re-displayed with a ^ marker under the problem.

Input: Menu choices typed at the console; text typed or pasted line by
line (finished with a line containing only END); or a file name.

Output: The result of each check, the session history, and detailed
views of past checks, printed to the console.
"""

from text_buffer import TextBuffer
from bracket_checker import check_brackets
from session_history import SessionHistory


END_MARKER = "END"

MENU = """
==== Bracket & Syntax Validator ====
1) Check typed or pasted text
2) Check a file
3) View session history
4) View a past check in detail
5) Clear history
6) Quit"""


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
    Postcondition: It reads a file name, loads and checks the file,
    and logs the result. If the file cannot be read it prints an error.
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
    '''
    Precondition: none.
    Postcondition: Creates one history for the whole session and
    runs each menu option on it until the user quits.
    '''
    history = SessionHistory()
    choice = ""
    while choice != "6":
        print(MENU)
        choice = input("Choose 1-6: ").strip()
        if choice == "1":
            check_typed_text(history)
        elif choice == "2":
            check_file(history)
        elif choice == "3":
            print(history.get_summary())
        elif choice == "4":
            view_detail(history)
        elif choice == "5":
            history.clear()
            print("History cleared.")
        elif choice != "6":
            print("Invalid choice.")
    print("Goodbye!")


if __name__ == "__main__":
    main()
