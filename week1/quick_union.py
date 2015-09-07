"""
Quick Union algorithm (weighted)
"""

import argparse


class QuickUnion:
    """
    Object sequence represented as a list of items,
    item value corresponds to a root of object
    """

    def __init__(self, n):
        """
        :param n: number of objects (0 to n - 1)
        """
        self.data = list(range(n))
        self.size = [1]*n  # Objects height in the tree

    def union(self, obj1, obj2):
        """
        Add connection between obj1 and obj2 objects
        Weight algorithm (avoiding too height trees)

        :param obj1: int
        :param obj2: int
        :return: None
        """
        root_obj1 = self.root(obj1)
        root_obj2 = self.root(obj2)
        if root_obj1 != root_obj2:
            if self.size[root_obj1] < self.size[root_obj2]:
                self.data[root_obj1] = root_obj2
                self.size[root_obj2] += self.size[root_obj1]
            else:
                self.data[root_obj2] = root_obj1
                self.size[root_obj1] += self.size[root_obj2]

    def connected(self, obj1, obj2):
        """
        Are obj1 and obj2 in the same component?
        :param obj1: int
        :param obj2: int
        :return: True or False
        """
        return self.root(obj1) == self.root(obj2)

    def root(self, obj):
        """
        Root of obj

        :param obj: int
        :return: int
        """
        while obj != self.data[obj]:
            # Uncomment to enable simple path compression
            # self.data[obj] = self.data[self.data[obj]]
            obj = self.data[obj]
        return obj

    def __repr__(self):
        return ' '.join(map(str, self.data))

    __str__ = __repr__


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
    length, unions = task[0], task[1:]

    # Run algorithm
    lst = QuickUnion(int(length))
    for union_operation in unions:
        obj1, obj2 = map(int, union_operation.split('-'))
        lst.union(obj1, obj2)
    print(lst)

if __name__ == '__main__':  # pragma: no cover
    main()
