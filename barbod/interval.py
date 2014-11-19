# -*- coding: utf-8 -*-
__author__ = 'vahid'


class Interval(object):
    def __init__(self, cents):
        self.cents = cents

    @property
    def semitones(self):
        return self.cents / 100.0

    @property
    def quarter_tones(self):
        return self.cents / 50.0

    @property
    def farabs(self):
        return self.cents / 8.333333

    @property
    def mems(self):
        return self.cents / 5.85365

    @property
    def savarts(self):
        return self.cents / 4.0

    def __repr__(self):
        return '%s Cents' % self.cents

    def __recognize_other(self, other):
        return other if not isinstance(other, Interval) else other.cents

    def __eq__(self, other):
        return self.cents == self.__recognize_other(other)

    def __ne__(self, other):
        return self.cents!= self.__recognize_other(other)

    def __gt__(self, other):
        return self.cents> self.__recognize_other(other)

    def __ge__(self, other):
        return self.cents>= self.__recognize_other(other)

    def __lt__(self, other):
        return self.cents< self.__recognize_other(other)

    def __le__(self, other):
        return self.cents<= self.__recognize_other(other)

    def __hash__(self):
        return self._c_offset

    def __add__(self, other):
        return Interval(self.cents+ self.__recognize_other(other))

    def __sub__(self, other):
        return Interval(self.cents- self.__recognize_other(other))