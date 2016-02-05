"""Quick Find algorithm"""


class QuickFind:
    """Object sequence represented as a list of items

    Items with the same value represent the connected objects
    """

    def __init__(self, length):
        """
        Args:
            length (stR): number of objects (0 to n - 1)
        """
        self.data = list(range(length))

    def union(self, obj1, obj2):
        """Add connection between obj1 and obj2

        Args:
            obj1 (int): First object
            obj2 (int): Second object

        Returns:
            None
        """
        root_obj1 = self.data[obj1]
        root_obj2 = self.data[obj2]
        for i in range(len(self.data)):
            if self.data[i] == root_obj1:
                self.data[i] = root_obj2

    def connected(self, obj1, obj2):
        """Are obj1 and obj2 in the same component?

        Args:
            obj1 (int): First object
            obj2 (int): Second object

        Returns:
            bool: True or False
        """
        return self.data[obj1] == self.data[obj2]

    def find(self, obj):
        """Component identifier for obj

        Args:
            obj (int): Object

        Returns:
            int: Object root

        :param obj: int
        :return: int
        """
        return self.data[obj]

    def count(self):
        """Number of components

        Returns:
            int: Number unique of components
        """
        return len(set(self.data))

    def __repr__(self):
        return ' '.join(map(str, self.data))

    __str__ = __repr__
