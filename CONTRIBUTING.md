# Contributing — Group 2 Team Plan

**Members:** Andrew Gause (agause7975) · Benjamin Clark (bclark2799) · Ramina Daood (rdaood8933)
**Target finish:** Wed Oct 7, 2026 · **Due:** Sun Oct 11, 2026

Full directions and the official 75-point rubric are in `Group_Project_Directions.pdf`.

## Who does what

| Member | Files | Branch | Reviewer | Deadline |
|---|---|---|---|---|
| **Andrew** | `check_result.py` | `setup-base-classes` | Ramina | **merged Wed 9/30** (everyone needs it) |
| **Andrew** | `validator_console.py` | `feature-console-menu` | Ramina | PR by Sat 10/3 |
| **Benjamin** | `text_buffer.py` | `feature-text-buffer` | Andrew | PR by Sat 10/3 |
| **Benjamin** | `bracket_checker.py` | `feature-bracket-checker` | Andrew | PR by Sat 10/3 |
| **Ramina** | `session_history.py` | `feature-session-history` | Benjamin | PR by Sat 10/3 |
| **Ramina** | `test_end_to_end.py` + new files in `samples/` | `test-end-to-end` | Benjamin | PR by Sat 10/3 |

Each task also has a **GitHub Issue** assigned to its owner. Link your PR to its issue (write `Closes #<number>` in the PR description) so it closes when merged.

Every file you own has an **ASSIGNED TO** banner at the top, and every method you write has a `TODO (YourName)` marker. Search for your name to find all your work.

For the Session 2 understanding check, you explain the code **you reviewed**: Andrew → Benjamin's checker, Benjamin → Ramina's history, Ramina → Andrew's console.

## What's given (do not modify)

- `my_array_list.py`, `my_linked_list.py`, `my_stack.py`, `my_array_stack.py`: shared base classes
- Blocks marked `GIVEN: DO NOT MODIFY` (the `OPENERS`/`CLOSERS` constants, `HistoryEntry`, the console `MENU`)
- `test_text_buffer.py`, `test_bracket_checker.py`, `test_session_history.py` and `expected_output/`
- `samples/balanced.py`, `mismatch.py`, `unclosed.py`, `unexpected.py`

## How to do your part

1. Get the latest `main` and create your branch:
   ```bash
   git checkout main
   git pull
   git checkout -b <your-branch>
   ```
2. In each method: read the Precondition / Postcondition / HINT, **replace the comment block with your own docstring**, and write the code.
3. Fill in the file header (Author, Date, Purpose, Input, Output) in your own words.
4. Test your part. Your output must match the expected file line for line:
   ```bash
   python3 test_text_buffer.py        # Benjamin
   python3 test_bracket_checker.py    # Benjamin
   python3 test_session_history.py    # Ramina
   python3 test_end_to_end.py         # Ramina (after all branches merge)
   python3 validator_console.py       # Andrew
   ```
5. Commit often with descriptive messages, then push:
   ```bash
   git add <files>
   git commit -m "Add unclosed-opener check to check_brackets"
   git push -u origin <your-branch>
   ```
6. Open a pull request into `main` on GitHub, add `Closes #<issue>`, and request your reviewer. **Never commit directly to `main`.**
7. **Reviewers:** read the whole file, run its test, and leave at least one real comment before approving.

## Team rules

- **Write your own code.** The hints tell you what to do, not the code to type. You'll need to explain your part, and a teammate's part, in your Session 2 log.
- **Don't change the interface alone.** `CheckResult` fields, method names and message formats are shared. If one needs to change, raise it in Discord first.
- **Line and column numbers are 1-based** everywhere the user sees them. MyArrayList indexes are 0-based, so line `n` is index `n - 1`.
- **Our `pop()` does not return a value.** Call `get_top()` first, then `pop()`. Always check `is_empty_stack()` before `get_top()`.
- Style follows the *Computer Science Coding Conventions at Oakton College*: 4-space indent, snake_case, a header docstring, and a Precondition/Postcondition docstring on every method.
- Pull before you start each session, push after every change that works, and reply to PR review requests within 24 hours.

## Schedule

| Date | Milestone |
|---|---|
| Tue 9/29 | **Session 1:** confirm the plan, group AI conversation, everyone writes their Session 1 log |
| Wed 9/30 | `check_result.py` merged; everyone branches from the updated `main` |
| Thu 10/1 – Sat 10/3 | Build and test your part; open PRs |
| Sun 10/4 | Reviews done, branches merged |
| Mon 10/5 | **Session 2:** run end-to-end tests together, fix bugs, everyone writes their Session 2 log |
| Tue 10/6 | Spec doc drafted and reviewed by all |
| Wed 10/7 | **Submit** |
