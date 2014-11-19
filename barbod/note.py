# -*- coding: utf-8 -*-

import re
from barbod.constants import NOTE_NAMES, NOTE_OFFSETS

__author__ = 'vahid'


class Note(object):
    def __init__(self, name_or_index):
        if isinstance(name_or_index, int):
            self._c_offset = name_or_index
        elif isinstance(name_or_index, Note):
            self._c_offset = name_or_index._c_offset
        else:
            self._c_offset = self.parse(name_or_index)

    @staticmethod
    def parse(expr):
        match = re.match('^(?P<note>[CDEFGAB][#b]{0,1})(?P<octave>-?\d{0,2})$', expr).groupdict()
        if not match:
            raise ArgumentError('Invalid note name: %s' % expr)

        try:
            index_in_octave = NOTE_OFFSETS[match['note']]
        except KeyError:
            raise ArgumentError('Invalid note name: %s' % expr)

        if match['octave']:
            octave = int(match['octave'])
        else:
            octave = 0

        return octave * len(NOTE_NAMES) + index_in_octave

    @property
    def octave(self):
        return self._c_offset // len(NOTE_NAMES)

    @property
    def index(self):
        return self._c_offset % len(NOTE_NAMES)

    def __str__(self):
        return '%s%s' % (NOTE_NAMES[self.index][0], '' if self.octave == 0 else self.octave)

    def __repr__(self):
        return ' '.join(['%s%s' % (n, '' if self.octave == 0 else self.octave) for n in NOTE_NAMES[self.index]])

    def __recognize_other(self, other):
        return other if not isinstance(other, Note) else other._c_offset

    def __eq__(self, other):
        return self._c_offset == self.__recognize_other(other)

    def __ne__(self, other):
        return self._c_offset != self.__recognize_other(other)

    def __gt__(self, other):
        return self._c_offset > self.__recognize_other(other)

    def __ge__(self, other):
        return self._c_offset >= self.__recognize_other(other)

    def __lt__(self, other):
        return self._c_offset < self.__recognize_other(other)

    def __le__(self, other):
        return self._c_offset <= self.__recognize_other(other)

    def __hash__(self):
        return self._c_offset