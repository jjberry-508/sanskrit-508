from model.verb_class_1_generator import *


def test_present_indicative_active_bhr():
    lex_entry = LexicalEntry(id=9,
                             form='bhṛ',
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


def test_present_indicative_active_budh():
    lex_entry = LexicalEntry(id=12,
                             form='budh',
                             pos=PartOfSpeech.FINITE_VERB,
                             definition='to wake up, understand',
                             verb_class=VerbClass.I,
                             verb_surface='bodhati',
                             chapter='3')
    generator = VerbClass1Generator()
    words = generator.generate_present_indicative_active(lex_entry)
    assert len(words) == 9
    for (i, surface, person, number) in [(0, "bodhāmi", Person.FIRST, Number.SINGULAR),
                                         (1, "bodhāvaḥ", Person.FIRST, Number.DUAL),
                                         (2, "bodhāmaḥ", Person.FIRST, Number.PLURAL),
                                         (3, "bodhasi", Person.SECOND, Number.SINGULAR),
                                         (4, "bodhathaḥ", Person.SECOND, Number.DUAL),
                                         (5, "bodhatha", Person.SECOND, Number.PLURAL),
                                         (6, "bodhati", Person.THIRD, Number.SINGULAR),
                                         (7, "bodhataḥ", Person.THIRD, Number.DUAL),
                                         (8, "bodhanti", Person.THIRD, Number.PLURAL)]:
        assert words[i].surface_form == surface
        assert words[i].person == person
        assert words[i].number == number
        assert words[i].tense == Tense.PRESENT
        assert words[i].voice == Voice.ACTIVE
        assert words[i].mood == Mood.INDICATIVE


def test_switcher():
    switcher = {(PartOfSpeech.FINITE_VERB, VerbClass.I): VerbClass1Generator}
    lex_entry = LexicalEntry(id=9,
                             form='bhṛ',
                             pos=PartOfSpeech.FINITE_VERB,
                             definition='to bear, carry',
                             verb_class=VerbClass.I,
                             verb_surface='bharati',
                             chapter='3')
    generator = switcher.get((lex_entry.pos, lex_entry.verb_class))()
    words = generator.generate_present_indicative_active(lex_entry)
    assert len(words) == 9
