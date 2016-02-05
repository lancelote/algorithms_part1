"""Quick Union algorithm (weighted)"""


class QuickUnion:
    """Object sequence represented as a list of items

    Item value corresponds to a root of object
    """

    def __init__(self, n):
        """
        Args:
            n (int): Number of objects
        """
        self.data = list(range(n))
        self.size = [1]*n  # Objects height in the tree

    def union(self, obj1, obj2):
        """Add connection between obj1 and obj2 objects

        Weighted algorithm (avoiding too height trees)

        Args:
            obj1 (int): First object
            obj2 (int): Second object

        Returns:
            None
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
        """Are obj1 and obj2 in the same component?

        Args:
            obj1 (int): First object
            obj2 (int): Second object

        Returns:
            bool: True or False
        """
        return self.root(obj1) == self.root(obj2)

    def root(self, obj):
        """Find root of obj

        Args:
            obj (int): Object to find root

        Returns:
            int: Object root
        """
        while obj != self.data[obj]:
            # Uncomment to enable simple path compression
            # self.data[obj] = self.data[self.data[obj]]
            obj = self.data[obj]
        return obj

    def __repr__(self):
        return ' '.join(map(str, self.data))

    __str__ = __repr__
