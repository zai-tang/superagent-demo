# AGENTS.md

Instructions for coding agents working in this repository.

## What this is

`textstats` is a small, dependency-free Python library. Keep it that way: no
third-party runtime dependencies, Python 3.9 or later.

## Before you change anything

Run the tests and make sure they pass:

```sh
python -m unittest discover -s tests -v
```

## While you change things

- Add a test for every behaviour you add or change.
- Keep the public surface in `textstats/__init__.py` in step with `core.py`:
  a new function needs an import and an entry in `__all__`.
- Match the existing style: type hints on public functions, a short docstring
  that says what the function returns, no comments that restate the code.
- Do not add a dependency, a CLI, a config file, or a build step.

## Before you open a pull request

Run the tests again. Your pull request description states what changed, why,
and how you verified it. Mention anything you left out.
