# -*- coding: utf-8 -*-
__author__ = 'vahid'

import re

_NOTE_OFFSETS = {
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

_NOTE_NAMES = {
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


class Note(object):
    def __init__(self, name_or_index):
        if isinstance(name_or_index, int):
            self._c_offset = name_or_index
        else:
            match = re.match('^(?P<note>[CDEFGAB][#b]{0,1})(?P<octave>-?\d{0,2})$', name_or_index).groupdict()
            if not match:
                raise ArgumentError('Invalid note name: %s' % name_or_index)

            try:
                index_in_octave = _NOTE_OFFSETS[match['note']]
            except KeyError:
                raise ArgumentError('Invalid note name: %s' % name_or_index)

            if match['octave']:
                octave = int(match['octave'])
            else:
                octave = 0

            self._c_offset = octave * len(_NOTE_NAMES) + index_in_octave

    @property
    def octave(self):
        return self._c_offset // len(_NOTE_NAMES)

    @property
    def index(self):
        return self._c_offset % len(_NOTE_NAMES)

    def __repr__(self):
        return '%s%s' % (_NOTE_NAMES[self.index][0], '' if self.octave == 0 else self.octave)

