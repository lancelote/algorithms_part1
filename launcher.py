"""
Easy Launcher for algorithms problems
"""

import argparse

from week1.quick_find import QuickFind
from week1.quick_union import QuickUnion


def arg_parse():  # pragma: no cover
    """
    Parse console arguments
    """
    parser = argparse.ArgumentParser(description="Quick union algorithm")
    parser.add_argument("task", action="store")
    args = parser.parse_args()
    task = args.task
    return task


def main():  # pragma: no cover
    """
    Prints the result to a console
    """
    task = arg_parse().split(' ')
    algorithm, length, unions = task[0], task[1], task[2:]

    # Run algorithm
    if algorithm == 'quick_find':
        lst = QuickFind(int(length))
    else:
        lst = QuickUnion(int(length))
    for union_operation in unions:
        obj1, obj2 = map(int, union_operation.split('-'))
        lst.union(obj1, obj2)
    print(lst)

if __name__ == '__main__':  # pragma: no cover
    main()
