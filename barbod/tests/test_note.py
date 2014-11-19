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
                     (-13, 'B-2')]:
            if isinstance(note, tuple):
                note_name , expect = note
            else:
                note_name = expect = note
            self.assertEqual(repr(Note(note_name)), expect)




if __name__ == '__main__':
    unittest.main()