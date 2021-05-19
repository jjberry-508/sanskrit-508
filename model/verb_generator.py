from abc import abstractmethod

from model.finite_verb import *
from model.lexical_entry import LexicalEntry


class VerbGenerator:

    @abstractmethod
    def generate_present_indicative_active(self, lex_entry: LexicalEntry):
        raise NotImplementedError

    def get_primary_active_ending(self, person: Person, number: Number):
        switcher = {(Person.FIRST, Number.SINGULAR): "mi",
                    (Person.FIRST, Number.DUAL): "vaḥ",
                    (Person.FIRST, Number.PLURAL): "maḥ",
                    (Person.SECOND, Number.SINGULAR): "si",
                    (Person.SECOND, Number.DUAL): "thaḥ",
                    (Person.SECOND, Number.PLURAL): "tha",
                    (Person.THIRD, Number.SINGULAR): "ti",
                    (Person.THIRD, Number.DUAL): "taḥ",
                    (Person.THIRD, Number.PLURAL): "nti"}
        return switcher.get((person, number))

