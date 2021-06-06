from model.common_enums import *
from model.word import Word
from model.lexical_entry import LexicalEntry


class FiniteVerb(Word):

    def __init__(self,
                 id: int,
                 lex_entry: LexicalEntry,
                 surface_form: str,
                 person: Person,
                 number: Number,
                 tense: Tense,
                 voice: Voice,
                 mood: Mood):
        super().__init__(id, lex_entry, surface_form)
        self.person = person
        self.number = number
        self.tense = tense
        self.voice = voice
        self.mood = mood

    def get_fields(self) -> dict:
        fields = {
            'id': self.id,
            'lex_entry': self.lex_entry.get_fields(),
            'surface_form': self.surface_form,
            'person': self.person.value,
            'number': self.number.value,
            'tense': self.tense.value,
            'voice': self.voice.value,
            'mood': self.mood.value
        }
        return fields

    def get_json(self) -> dict:
        json = {
            'id': self.id,
            'lex_entry': self.lex_entry.get_json(),
            'surface_form': self.surface_form,
            'person': self.person.name.lower(),
            'number': self.number.name.lower(),
            'tense': self.tense.name.lower(),
            'voice': self.voice.name.lower(),
            'mood': self.mood.name.lower()
        }
        return json
