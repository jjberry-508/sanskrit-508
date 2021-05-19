from model.common_enums import *
from model.word import Word
from model.lexical_entry import LexicalEntry


class FiniteVerb(Word):

    def __init__(self,
                 lex_entry: LexicalEntry,
                 surface_form: str,
                 person: Person,
                 number: Number,
                 tense: Tense,
                 voice: Voice,
                 mood: Mood):
        super().__init__(lex_entry, surface_form)
        self.person = person
        self.number = number
        self.tense = tense
        self.voice = voice
        self.mood = mood
