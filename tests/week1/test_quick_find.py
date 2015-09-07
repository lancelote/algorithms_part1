# pylint: disable=missing-docstring

import unittest

from week1.quick_find import QuickFind


class QuickFindTest(unittest.TestCase):

    def setUp(self):
        self.lst = QuickFind(10)

    def test_correct_init(self):
        self.assertEqual(str(self.lst), "0 1 2 3 4 5 6 7 8 9")

    def test_union(self):
        self.lst.union(9, 0)
        self.assertEqual(str(self.lst), "0 1 2 3 4 5 6 7 8 0")
        self.lst.union(5, 6)
        self.assertEqual(str(self.lst), "0 1 2 3 4 6 6 7 8 0")
        self.lst.union(2, 1)
        self.assertEqual(str(self.lst), "0 1 1 3 4 6 6 7 8 0")
        self.lst.union(2, 9)
        self.assertEqual(str(self.lst), "0 0 0 3 4 6 6 7 8 0")
        self.lst.union(7, 9)
        self.assertEqual(str(self.lst), "0 0 0 3 4 6 6 0 8 0")
        self.lst.union(1, 5)
        self.assertEqual(str(self.lst), "6 6 6 3 4 6 6 6 8 6")

    def test_connected(self):
        self.assertFalse(self.lst.connected(9, 0))
        self.lst.union(9, 0)
        self.assertTrue(self.lst.connected(9, 0))
        self.assertFalse(self.lst.connected(9, 1))

    def test_find(self):
        self.assertEqual(self.lst.find(9), 9)
        self.lst.union(9, 0)
        self.assertEqual(self.lst.find(9), 0)

    def test_count(self):
        self.assertEqual(self.lst.count(), 10)
        self.lst.union(9, 0)
        self.assertEqual(self.lst.count(), 9)
        self.lst.union(8, 1)
        self.assertEqual(self.lst.count(), 8)
        self.lst.union(1, 0)
        self.assertEqual(self.lst.count(), 7)
