# pylint: disable=missing-docstring

import unittest

from week1.quick_union import QuickUnion


class QuickUnionTest(unittest.TestCase):

    def setUp(self):
        self.lst = QuickUnion(10)

    def test_correct_init(self):
        self.assertEqual(str(self.lst), "0 1 2 3 4 5 6 7 8 9")

    def test_union(self):
        self.lst.union(6, 2)
        self.assertEqual(str(self.lst), "0 1 6 3 4 5 6 7 8 9")
        self.lst.union(0, 8)
        self.assertEqual(str(self.lst), "0 1 6 3 4 5 6 7 0 9")
        self.lst.union(3, 2)
        self.assertEqual(str(self.lst), "0 1 6 6 4 5 6 7 0 9")
        self.lst.union(1, 4)
        self.assertEqual(str(self.lst), "0 1 6 6 1 5 6 7 0 9")
        self.lst.union(3, 9)
        self.assertEqual(str(self.lst), "0 1 6 6 1 5 6 7 0 6")
        self.lst.union(0, 4)
        self.assertEqual(str(self.lst), "0 0 6 6 1 5 6 7 0 6")
        self.lst.union(7, 9)
        self.assertEqual(str(self.lst), "0 0 6 6 1 5 6 6 0 6")
        self.lst.union(8, 2)
        self.assertEqual(str(self.lst), "6 0 6 6 1 5 6 6 0 6")
        self.lst.union(3, 5)
        self.assertEqual(str(self.lst), "6 0 6 6 1 6 6 6 0 6")

    def test_connected(self):
        self.assertFalse(self.lst.connected(1, 2))
        self.lst.union(1, 2)
        self.assertTrue(self.lst.connected(1, 2))
        self.assertFalse(self.lst.connected(1, 3))
