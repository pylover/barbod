# -*- coding: utf-8 -*-


import unittest
from barbod import Interval

__author__ = 'vahid'


class TestInterval(unittest.TestCase):

    def test_constructor(self):
        self.assertEqual(str(Interval(100)), '100 Cents')

    def test_other_units(self):
        i = Interval(1200)
        self.assertEqual(i.semitones, i.cents / 100.0)
        self.assertEqual(i.quarter_tones, i.cents / 50.0)
        self.assertEqual(i.farabs, i.cents / 8.333333)
        self.assertEqual(i.mems, i.cents / 5.85365)
        self.assertEqual(i.savarts, i.cents / 4.0)

    def test_operators(self):
        la = Interval(100)
        self.assertEqual(la, Interval(100))
        self.assertEqual(la, 100)
        self.assertNotEqual(la, Interval(101))
        self.assertNotEqual(la, 99)
        self.assertTrue(la == Interval(100))
        self.assertTrue(la == 100)
        self.assertTrue(la != Interval(99))
        self.assertTrue(la != 102)

        self.assertTrue(la < Interval(101))
        self.assertTrue(la < 101)
        self.assertTrue(la > Interval(99))
        self.assertTrue(la > 99)
        self.assertTrue(la <= Interval(100))
        self.assertTrue(la <= 100)
        self.assertTrue(la >= Interval(100))
        self.assertTrue(la >= 100)
        self.assertTrue(la <= Interval(101))
        self.assertTrue(la <= 101)
        self.assertTrue(la >= Interval(99))
        self.assertTrue(la >= 99)

        self.assertEqual(la + 1, Interval(101))
        self.assertEqual(la + 1, 101)
        self.assertEqual(la - 1, Interval(99))
        self.assertEqual(la - 1, 99)

        la += 1
        self.assertEqual(la, Interval(101))


if __name__ == '__main__':
    unittest.main()