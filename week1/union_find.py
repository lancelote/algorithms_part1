"""
Union Find algorithm
"""


class UnionFind:
    """
    Object sequence represented as a list of items,
    item value corresponds to a root of object
    """

    def __init__(self, n):
        """
        :param n: number of objects (0 to n - 1)
        """
        self.id = list(range(n))
        self.size = [0]*n  # Objects height in the tree

    def union(self, p, q):
        """
        Add connection between p and q objects
        Weight algorithm (avoiding too height trees)

        :param p: int
        :param q: int
        :return: None
        """
        root_p = self.root(p)
        root_q = self.root(q)
        if root_p != root_q:
            if self.size[root_p] < self.size[root_q]:
                self.id[root_p] = root_q
                self.size[root_q] += self.size[root_p]
            else:
                self.id[root_q] = root_p
                self.size[root_p] += self.size[root_q]

    def connected(self, p, q):
        """
        Are p and q in the same component?
        :param p: int
        :param q: int
        :return: True or False
        """
        return self.root(p) == self.root(q)

    def root(self, p):
        """
        Root of p

        :param p: int
        :return: int
        """
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]  # Simple path compression
            p = self.id[p]
        return p
