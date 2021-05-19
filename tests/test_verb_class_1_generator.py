from model.verb_class_1_generator import *


def test_get_primary_active_ending():
    generator = VerbClass1Generator()
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


def test_present_indicative_active():
    lex_entry = LexicalEntry(form='bhṛ',
                             pos=PartOfSpeech.FINITE_VERB,
                             definition='to bear, carry',
                             verb_class=VerbClass.I,
                             verb_surface='bharati',
                             chapter='3')
    generator = VerbClass1Generator()
    words = generator.generate_present_indicative_active(lex_entry)
    assert len(words) == 9
    for (i, surface, person, number) in [(0, "bharāmi", Person.FIRST, Number.SINGULAR),
                                         (1, "bharāvaḥ", Person.FIRST, Number.DUAL),
                                         (2, "bharāmaḥ", Person.FIRST, Number.PLURAL),
                                         (3, "bharasi", Person.SECOND, Number.SINGULAR),
                                         (4, "bharathaḥ", Person.SECOND, Number.DUAL),
                                         (5, "bharatha", Person.SECOND, Number.PLURAL),
                                         (6, "bharati", Person.THIRD, Number.SINGULAR),
                                         (7, "bharataḥ", Person.THIRD, Number.DUAL),
                                         (8, "bharanti", Person.THIRD, Number.PLURAL)]:
        assert words[i].surface_form == surface
        assert words[i].person == person
        assert words[i].number == number
        assert words[i].tense == Tense.PRESENT
        assert words[i].voice == Voice.ACTIVE
        assert words[i].mood == Mood.INDICATIVE


def test_switcher():
    switcher = {(PartOfSpeech.FINITE_VERB, VerbClass.I): VerbClass1Generator}
    lex_entry = LexicalEntry(form='bhṛ',
                             pos=PartOfSpeech.FINITE_VERB,
                             definition='to bear, carry',
                             verb_class=VerbClass.I,
                             verb_surface='bharati',
                             chapter='3')
    generator = switcher.get((lex_entry.pos, lex_entry.verb_class))()
    words = generator.generate_present_indicative_active(lex_entry)
    assert len(words) == 9
