from model.verb_generator import *


def test_get_primary_active_ending():
    generator = VerbGenerator()
    for (person, number, ending) in [(Person.FIRST, Number.SINGULAR, "mi"),
                                     (Person.FIRST, Number.DUAL, "vaḥ"),
                                     (Person.FIRST, Number.PLURAL, "maḥ"),
                                     (Person.SECOND, Number.SINGULAR, "si"),
                                     (Person.SECOND, Number.DUAL, "thaḥ"),
                                     (Person.SECOND, Number.PLURAL, "tha"),
                                     (Person.THIRD, Number.SINGULAR, "ti"),
                                     (Person.THIRD, Number.DUAL, "taḥ"),
                                     (Person.THIRD, Number.PLURAL, "nti")]:
        assert generator.get_primary_active_ending(person, number) == ending
