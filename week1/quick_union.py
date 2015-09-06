"""
Quick Union algorithm
"""


class QuickUnion:
    """
    Object sequence represented as a list of items,
    items with the same value represent the connected objects
    """

    def __init__(self, n):
        """
        :param n: number of objects (0 to n - 1)
        """
        self.id = list(range(n))

    def union(self, p, q):
        """
        Add connection between p and q objects

        :param p: int
        :param q: int
        :return: None
        """
        for i in range(len(self.id)):
            if self.id[i] == self.id[p]:
                self.id[i] = self.id[q]

    def connected(self, p, q):
        """
        Are p and q in the same component?
        :param p: int
        :param q: int
        :return: True or False
        """
        return self.id[p] == self.id[q]

    def find(self, p):
        """
        Component identifier for p

        :param p: int
        :return: int
        """
        return self.id[p]

    def count(self):
        """
        Number of components

        :return: int
        """
        return len(set(self.id))
