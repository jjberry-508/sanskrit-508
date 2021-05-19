from model.finite_verb import *
from model.lexical_entry import LexicalEntry


class VerbClass1Generator:

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

    def generate_present_indicative_active(self, lex_entry: LexicalEntry):
        stem = lex_entry.verb_surface[:-3]
        words = []
        for (person, number) in [(Person.FIRST, Number.SINGULAR),
                                 (Person.FIRST, Number.DUAL),
                                 (Person.FIRST, Number.PLURAL),
                                 (Person.SECOND, Number.SINGULAR),
                                 (Person.SECOND, Number.DUAL),
                                 (Person.SECOND, Number.PLURAL),
                                 (Person.THIRD, Number.SINGULAR),
                                 (Person.THIRD, Number.DUAL),
                                 (Person.THIRD, Number.PLURAL)]:
            link_vowel = "a"
            if person == Person.FIRST:
                link_vowel = "ā"
            surface_form = stem + link_vowel + self.get_primary_active_ending(person, number)
            words.append(FiniteVerb(lex_entry, surface_form, person, number,
                                    Tense.PRESENT, Voice.ACTIVE, Mood.INDICATIVE))
        return words

