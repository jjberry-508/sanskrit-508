from model.common_enums import *
from model.lexical_entry import LexicalEntry
from model.word import Word


class Noun(Word):

    def __init__(self,
                 lex_entry: LexicalEntry,
                 surface_form: str,
                 case: Case,
                 number: Number,
                 gender: Gender):
        super().__init__(lex_entry, surface_form)
        self.case = case
        self.number = number
        self.gender = gender
