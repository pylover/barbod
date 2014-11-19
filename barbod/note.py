# -*- coding: utf-8 -*-

import re
from barbod.constants import CHROMATIC_NAMES, CHROMATIC_INDEXES, OCTAVE_CENTS, CHROMATIC_INTERVAL
from barbod import Interval

__author__ = 'vahid'


class Note(object):
    def __init__(self, note):
        if isinstance(note, int):
            self._c_offset = note
        elif isinstance(note, (Interval, Note)):
            self._c_offset = int(note)
        else:
            self._c_offset = self.parse(note)

    @staticmethod
    def parse(expr):
        match = re.match('^(?P<note>[CDEFGAB][#b]{0,1})(?P<octave>-?\d{0,2})$', expr).groupdict()
        if not match:
            raise ArgumentError('Invalid note name: %s' % expr)

        try:
            index_in_octave = CHROMATIC_INDEXES[match['note']] * CHROMATIC_INTERVAL
        except KeyError:
            raise ArgumentError('Invalid note name: %s' % expr)

        if match['octave']:
            octave = int(match['octave'])
        else:
            octave = 0

        return octave * OCTAVE_CENTS + index_in_octave

    @property
    def octave(self):
        return self._c_offset // OCTAVE_CENTS

    @property
    def chromatic_index(self):
        return int((self._c_offset % OCTAVE_CENTS) / CHROMATIC_INTERVAL)

    @property
    def names(self):
        return CHROMATIC_NAMES[self.chromatic_index]

    def __str__(self):
        return '%s%s' % (self.names[0], '' if self.octave == 0 else self.octave)

    def __repr__(self):
        return ' '.join(['%s%s' % (n, '' if self.octave == 0 else self.octave) for n in self.names])

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

    def __add__(self, other):
        return Note(self._c_offset + other)

    def __sub__(self, other):
        return Note(self._c_offset - other)

    def __int__(self):
        return self._c_offset