from enum import Enum


class Case(Enum):
    NOMINATIVE = 1
    VOCATIVE = 2
    ACCUSATIVE = 3
    INSTRUMENTAL = 4
    DATIVE = 5
    ABLATIVE = 6
    GENITIVE = 7
    LOCATIVE = 8


class Gender(Enum):
    MASCULINE = 1
    FEMININE = 2
    NEUTER = 3


class Number(Enum):
    SINGULAR = 1
    DUAL = 2
    PLURAL = 3


class Person(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3


class Tense(Enum):
    PRESENT = 1
    IMPERFECT = 2
    FUTURE = 3
    PERFECT = 4
    AORIST = 5


class Voice(Enum):
    ACTIVE = 1
    MIDDLE = 2
    PASSIVE = 3


class Mood(Enum):
    INDICATIVE = 1
    IMPERATIVE = 2
    POTENTIAL = 3


class VerbClass(Enum):
    I = 1
    II = 2
    III = 3
    IV = 4
    V = 5
    VI = 6
    VII = 7
    VIII = 8
    IX = 9
    X = 10


class NounDeclension(Enum):
    SHORT_A = 1
    LONG_A = 2
    LONG_I = 3
    LONG_U = 4
    SHORT_I = 5
    SHORT_U = 6
    DOT_R = 7
    CONS_T = 8
    CONS_D = 9
    CONS_C = 10
    CONS_J = 11
    CONS_AS = 12
    CONS_US = 13
    CONS_AN = 14
    CONS_IN = 15


class PartOfSpeech(Enum):
    FINITE_VERB = 1
    NOUN = 2
    ADJECTIVE = 3
    INDECLINABLE = 4
    NUMERAL = 5
    PRONOUN = 6
