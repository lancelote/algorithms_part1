"""
Quick Find algorithm
"""

import argparse


class QuickFind:
    """
    Object sequence represented as a list of items,
    items with the same value represent the connected objects
    """

    def __init__(self, length):
        """
        :param length: number of objects (0 to n - 1)
        """
        self.data = list(range(length))

    def union(self, obj1, obj2):
        """
        Add connection between obj1 and obj2

        :param obj1: int
        :param obj2: int
        :return: None
        """
        root_obj1 = self.data[obj1]
        root_obj2 = self.data[obj2]
        for i in range(len(self.data)):
            if self.data[i] == root_obj1:
                self.data[i] = root_obj2

    def connected(self, obj1, obj2):
        """
        Are obj1 and obj2 in the same component?
        :param obj1: int
        :param obj2: int
        :return: True or False
        """
        return self.data[obj1] == self.data[obj2]

    def find(self, obj):
        """
        Component identifier for obj

        :param obj: int
        :return: int
        """
        return self.data[obj]

    def count(self):
        """
        Number of components

        :return: int
        """
        return len(set(self.data))

    def __repr__(self):
        return ' '.join(map(str, self.data))

    __str__ = __repr__


def arg_parse():  # pragma: no cover
    """
    Parse console arguments
    """
    parser = argparse.ArgumentParser(description="Quick find algorithm")
    parser.add_argument("task", action="store")
    args = parser.parse_args()
    task = args.task
    return task


def main():  # pragma: no cover
    """
    Prints the result to a console
    """
    task = arg_parse().split(' ')
    legth, unions = task[0], task[1:]

    # Run algorithm
    lst = QuickFind(int(legth))
    for union_operation in unions:
        obj1, obj2 = map(int, union_operation.split('-'))
        lst.union(obj1, obj2)
    print(lst)

if __name__ == '__main__':  # pragma: no cover
    main()
