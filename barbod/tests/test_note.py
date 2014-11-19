# -*- coding: utf-8 -*-


import unittest
from barbod import Note

__author__ = 'vahid'


class TestNote(unittest.TestCase):

    def test_constructor(self):
        for note in ['A',
                     'A1',
                     'C#',
                     ('Bb', 'A#'),
                     'C2',
                     'C-2',
                     ('C0', 'C'),
                     'G-20',
                     (1, 'C#'),
                     (0, 'C'),
                     (12, 'C1'),
                     (-12, 'C-1'),
                     (-13, 'B-2'),
                     (Note('A'), 'A')]:
            if isinstance(note, tuple):
                note_name , expect = note
            else:
                note_name = expect = note
            self.assertEqual(str(Note(note_name)), expect)

    def test_repr(self):
        for note in ['A',
                     'A1',
                     ('C#', 'C# Db'),
                     ('Bb', 'A# Bb'),
                     'C2',
                     'C-2',
                     ('C0', 'C'),
                     'G-20',
                     (1, 'C# Db'),
                     (0, 'C'),
                     (12, 'C1'),
                     (-12, 'C-1'),
                     (-13, 'B-2'),
                     (Note('A#'), 'A# Bb')]:
            if isinstance(note, tuple):
                note_name , expect = note
            else:
                note_name = expect = note
            self.assertEqual(repr(Note(note_name)), expect)

    def test_operators(self):

        la = Note('A')
        self.assertEqual(la, Note('A'))
        self.assertEqual(la, 9)
        self.assertNotEqual(la, Note('A#'))
        self.assertNotEqual(la, 10)
        self.assertNotEqual(la, Note('A1'))
        self.assertTrue(la == Note('A'))
        self.assertTrue(la == Note('A0'))
        self.assertTrue(la != Note('B'))

        self.assertTrue(la < Note('B'))
        self.assertTrue(la < Note('A1'))
        self.assertTrue(la > Note('A-1'))
        self.assertTrue(la <= Note('A'))
        self.assertTrue(la >= Note('A'))
        self.assertTrue(la <= Note('B'))
        self.assertTrue(la <= Note('A1'))
        self.assertTrue(la >= Note('A-1'))

        self.assertEqual(la + 1, Note('A#'))
        self.assertEqual(la - 1, Note('Ab'))
        self.assertEqual(la + 24, Note('A2'))
        self.assertEqual(la - 12, Note('A-1'))

        la += 1
        self.assertEqual(la, Note('A#'))


if __name__ == '__main__':
    unittest.main()