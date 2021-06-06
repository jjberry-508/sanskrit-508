from model.verb_generator import *


class VerbClass4Generator(VerbGenerator):

    def __init__(self):
        super().__init__()

    def generate_present_indicative_active(self, lex_entry: LexicalEntry):
        stem = lex_entry.verb_surface[:-4]
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
            link_vowel = "ya"
            if person == Person.FIRST:
                link_vowel = "yā"
            surface_form = stem + link_vowel + self.get_primary_active_ending(person, number)
            words.append(FiniteVerb(1, lex_entry, surface_form, person, number,
                                    Tense.PRESENT, Voice.ACTIVE, Mood.INDICATIVE))
        return words
