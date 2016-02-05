[![Build Status](https://travis-ci.org/lancelote/algorithms_part1.svg)](https://travis-ci.org/lancelote/algorithms_part1)
[![Requirements Status](https://requires.io/github/lancelote/algorithms_part1/requirements.svg?branch=master)](https://requires.io/github/lancelote/algorithms_part1/requirements/?branch=master)

# Algorithms, Part 1

## Description

Code for the coursera Algorithms Part I course

### Week 1

Quick Find:
```bash
python3 launcher.py "quick_find 10 1-2 3-4 5-6 7-8"
# Where:
#   10 - number of objects
#   1-2 ... - union operations
```

Quick Union:
```bash
python3 launcher.py "quick_union 10 1-2 3-4 5-6 7-8"
# Where:
#   10 - number of objects
#   1-2 ... - union operations
```

## Requirements

Install:
```bash
pip install -r requirements.txt
```

Update/change:

1. Fix `requirements.in`
2. Make sure `pip-tools` are installed
3. Run `pip-compile requirements.in`
4. New `requirements.txt` are ready, run `pip-sync` to update your virtual
environment (do not do this without active venv!)

## Tests

```bash
paver        # Everything
paver week1  # Concrete (week1, week2, ..., weekn)
```

## ToDo List

- [x] Tests
- [x] CI
- [x] Extend description
- [x] Refactor algorithm call API
- [x] Project infrastructure
