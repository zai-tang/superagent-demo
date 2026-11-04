# textstats

A tiny, dependency-free Python library for counting things in text.

It exists so that `dsh-superagent` has a small but real project to work on:
a change here is a few lines of code plus a few lines of test, which makes
it easy to see whether the agent produced a reviewable result.

## Usage

```python
from textstats import char_count, word_count, unique_words, top_words

char_count("hello world")           # 10
word_count("hello hello world")     # 3
unique_words("Hello hello world")   # {"hello", "world"}
top_words("a b a c a", 2)           # [("a", 3), ("b", 1)]
```

## Development

No dependencies. Python 3.9 or later.

```sh
python -m unittest discover -s tests -v
```

## Layout

```
textstats/__init__.py   the library
textstats/core.py       the implementation
tests/test_textstats.py the tests
```
