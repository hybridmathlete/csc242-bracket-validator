# csc242-bracket-validator
CSC 242 Group 2 — Bracket &amp; Syntax Validator (MyArrayList + MyArrayStack + MyLinkedList)

## What it does

The Bracket & Syntax Validator is a console program that checks whether the brackets in a block of text, usually a snippet of code, are balanced. You type or paste the text, or load it from a file. The program checks that every `(`, `[` and `{` is closed by the matching `)`, `]` or `}` in the right order. If something is wrong, it reports the **line and column of the first problem**. Every check is saved in a session history, so you can list past checks and re-open any of them.

```
Check #1: typed text
  1 | if (x > [1, 2) {
                   ^
FAIL - Mismatch at line 1, col 14: expected ']' but found ')'
```

It recognizes four outcomes:

| Outcome | Example |
|---|---|
| Balanced | `PASS - All brackets are balanced` |
| Mismatch | `FAIL - Mismatch at line 2, col 23: expected ')' but found ']'` |
| Unexpected closer | `FAIL - Unexpected ')' at line 1, col 16: no bracket is open` |
| Unclosed opener | `FAIL - Unclosed '{' opened at line 2, col 12` |

## How the data structures work together

The program combines three of the course's data structures. Every check passes its data through all three:

```
TextBuffer             ->  check_brackets          ->  SessionHistory
MyArrayList of lines       MyArrayStack of open        MyLinkedList of past
                           brackets                    checks
                                  |
                                  v
                            CheckResult
```

| Structure | Job | Why it fits |
|---|---|---|
| **MyArrayList** | Stores the text, one string per line | Lines are looked up by number, and `get(index)` is O(1) on an array |
| **MyArrayStack** | Tracks brackets that are open but not yet closed, with their line and column | Brackets nest: the most recently opened must close first, which is last-in, first-out. `push`, `pop` and `get_top` are O(1) |
| **MyLinkedList** | Logs every check in the order it was run | The log only grows at the end (`add_last` is O(1) with the tail reference) and is always read oldest to newest |

`CheckResult` is the shared object the checker returns: whether the text is balanced, the line, the column and a message.

## Running it

Requires Python 3. From the project folder:

```bash
python3 validator_console.py
```

```
==== Bracket & Syntax Validator ====
1) Check typed or pasted text
2) Check a file
3) View session history
4) View a past check in detail
5) Clear history
6) Quit
```

For option 1, type or paste your text and enter `END` on its own line to finish. For option 2, try one of the files in `samples/`, such as `samples/mismatch.py`.

## Running the tests

```bash
python3 test_text_buffer.py
python3 test_bracket_checker.py
python3 test_session_history.py
python3 test_end_to_end.py
```

Each module test prints `Expected ... | Actual ...` lines. The full expected output for each one is in `expected_output/`. `test_end_to_end.py` runs the whole pipeline (load, check, log) on the files in `samples/`.

## Project structure

| File | Purpose |
|---|---|
| `validator_console.py` | Main program: the menu that runs the full pipeline |
| `check_result.py` | `CheckResult`, the result shared between modules |
| `text_buffer.py` | `TextBuffer`, which loads text or a file into a MyArrayList of lines |
| `bracket_checker.py` | `check_brackets`, the MyArrayStack matching algorithm |
| `session_history.py` | `SessionHistory`, the MyLinkedList log of past checks |
| `my_array_list.py`, `my_linked_list.py`, `my_stack.py`, `my_array_stack.py` | Base data structures from Labs 2–4 |
| `test_*.py`, `expected_output/`, `samples/` | Test drivers, expected results and sample input files |

## Team

- **Andrew Gause**: `CheckResult`, the console and integration
- **Benjamin Clark**: `TextBuffer` and the bracket checker
- **Ramina Daood**: the session history and end-to-end tests

Full individual contributions are in the group's Specifications Document. Team workflow is in [CONTRIBUTING.md](CONTRIBUTING.md).
