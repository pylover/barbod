# -*- coding: utf-8 -*-
__author__ = 'vahid'

CHROMATIC_INDEXES = {
    'C': 0,
    'C#': 1,
    'Db': 1,
    'D': 2,
    'D#': 3,
    'Eb': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'Gb': 6,
    'G': 7,
    'G#': 8,
    'Ab': 8,
    'A': 9,
    'A#': 10,
    'Bb': 10,
    'B': 11
}

CHROMATIC_NAMES = {
    0: ('C',),
    1: ('C#', 'Db'),
    2: ('D',),
    3: ('D#', 'Eb'),
    4: ('E',),
    5: ('F',),
    6: ('F#', 'Gb'),
    7: ('G',),
    8: ('G#', 'Ab'),
    9: ('A',),
    10: ('A#', 'Bb'),
    11: ('B',)
}

OCTAVE_CENTS = 1200 #  cents
CHROMATIC_INTERVAL = 100 #  cents