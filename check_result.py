"""
Author: AU75ZB
Date: 9/29/2026 

Purpose: Defines CheckResult, the shared result object for the Bracket
& Syntax Validator. The bracket checker (bracket_checker.py) creates a
CheckResult for every check it runs, the session history
(session_history.py) stores each one, and the console
(validator_console.py) prints them. Because all three modules agree on
the same four public fields -- is_balanced, line_number, column, and
message -- each group member can build their module independently and
the pieces still fit together. This file is the agreement that lets three 
people's code connect.

Input: Four values supplied by check_brackets() when a check finishes:
is_balanced (bool), line_number and column (1-based ints giving the
position of the first problem, both 0 when the text is balanced), and
message (a string describing the result). line_number, column, and
message are optional and default to 0, 0, and "". No console input is
read.

Output: A CheckResult object whose four fields can be read directly
(e.g. result.line_number). str(result) returns a one-line summary,
"PASS - <message>" or "FAIL - <message>", for example:
    PASS - All brackets are balanced
    FAIL - Mismatch at line 2, col 23: expected ')' but found ']'
"""

class CheckResult:

    def __init__(self, is_balanced, line_number=0, column=0, message=""):
        '''
        Precondition: is_balanced is a bool. line_number and column are
        the 1-based position of the first problem found (both 0 when the
        text is balanced). message is a string describing the result.
        Postcondition: Creates a CheckResult that stores the four values
        as public attributes (is_balanced, line_number, column, message)
        so the checker, the session history, and the console can all
        read them directly.
        '''
        self.is_balanced = is_balanced
        self.line_number = line_number
        self.column = column
        self.message = message

    def __str__(self):
        '''
        Precondition: none.
        Postcondition: Returns a one-line summary of the result as follows:
        "PASS - " followed by the message when the text is balanced, or
        "FAIL - " followed by the message when it is not. The session
        history and the console both print results this way. Here is an example:
            PASS - All brackets are balanced
            FAIL - Mismatch at line 1, col 2: expected ')' but found ']'
        '''
        if self.is_balanced:
            return "PASS - " + self.message
        return "FAIL - " + self.message
