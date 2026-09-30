"""
Author: [Your Name]
Date: [Today's Date]

Purpose: [Describe what this program does]

Input: [Describe expected input]

Output: [Describe expected output]
"""

# =====================================================================
# ASSIGNED TO: Ramina Daood (rdaood8933)
# BRANCH:      test-end-to-end
# REVIEWER:    Benjamin Clark (approves the PR)
# DUE:         PR opened by Sat 10/3; RUN IT TOGETHER in Session 2
#              (Mon 10/5) once every branch is merged.
# RUN WITH:    python3 test_end_to_end.py
#
# The other test drivers test ONE module each. This one tests the
# WHOLE pipeline on real files, the same way the console does:
#     TextBuffer.load_file -> check_brackets -> SessionHistory.add_check
# If a module works alone but the modules disagree about the interface
# (a field name, 0-based vs 1-based numbers, ...), THIS is the test that
# catches it. The four cases in main() are GIVEN; you add the rest.
# =====================================================================

from text_buffer import TextBuffer
from bracket_checker import check_brackets
from session_history import SessionHistory


def print_header(title):
    print("\n==============================")
    print(title)
    print("==============================")


def run_file_case(file_name, expected, history):
    # ASSIGNED TO: Ramina
    #
    # Precondition: file_name is a path to a sample file; expected is
    # the exact string str(result) should produce; history is a
    # SessionHistory.
    # Postcondition: Loads file_name into a new TextBuffer, runs
    # check_brackets on its lines, logs the result in history with the
    # file name as its label, and prints:
    #     <file_name>
    #       Expected: <expected>
    #       Actual:   <str(result)>
    # If the file cannot be loaded, prints
    # "  Could not load <file_name>" instead and logs nothing.
    #
    # HINT: This is the same pipeline as the console's run_check -- one
    # call into each of the three modules.

    # TODO (Ramina): Replace this comment block with your own
    # docstring, then implement the function below.
    pass


def main():
    print("CSC 242 Group 2 - End-to-End Test Driver")
    history = SessionHistory()

    # ================= GIVEN: one case per outcome =================
    print_header("Given cases: one per outcome")
    run_file_case("samples/balanced.py",
                  "PASS - All brackets are balanced", history)
    run_file_case("samples/mismatch.py",
                  "FAIL - Mismatch at line 2, col 23: expected ')' but found ']'",
                  history)
    run_file_case("samples/unclosed.py",
                  "FAIL - Unclosed '{' opened at line 2, col 12", history)
    run_file_case("samples/unexpected.py",
                  "FAIL - Unexpected ')' at line 1, col 16: no bracket is open",
                  history)

    # ================= YOUR TEST CASES =================
    #
    # TODO (Ramina): Create AT LEAST 4 new sample files in samples/
    # and add a run_file_case(...) call for each one below. Work out
    # each expected string BY HAND first (count the columns!), then
    # run the test. Cover at least these:
    #   1. A balanced file with brackets nested 3+ levels deep over
    #      several lines.
    #   2. An EMPTY file (0 lines) -- what should the result be?
    #   3. A longer file (8+ lines) whose only problem is on the LAST
    #      line.
    #   4. Brackets inside a string, e.g.  print("(")  -- our checker
    #      does not understand strings, so it counts that "(".
    #      Write the expected result for what the program ACTUALLY
    #      does, and note it in the spec doc under "future potential".
    # If a test FAILS, do not change the expected value to match --
    # tell the group in Discord which module looks wrong.
    print_header("Ramina's cases")

    # TODO (Ramina): After your cases, check the history the pipeline
    # built up:
    #   - print "Expected history count: <n> | Actual: <count>" where n
    #     is 4 plus however many cases you added
    #   - print history.get_summary()
    #   - print history.format_detail(...) for ONE failing check and
    #     make sure the ^ lands under the right character
    print_header("History after all cases")


if __name__ == "__main__":
    main()
