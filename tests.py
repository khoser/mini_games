# coding: utf-8

import unittest


class TestFunctions(unittest.TestCase):

    def first(self):
        self.assertEqual('test', 'test')

    def second(self):
        """second test"""
        self.assertEqual('2','2')

    def third(self):
        """?????? ????"""
        self.assertEqual(3, 3)
