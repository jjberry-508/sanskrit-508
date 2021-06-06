from model.verb_class_4_generator import *


def test_present_indicative_active_hrs():
    lex_entry = LexicalEntry(id=15,
                             form='hṛṣ',
                             pos=PartOfSpeech.FINITE_VERB,
                             definition='to be excited, happy',
                             verb_class=VerbClass.IV,
                             verb_surface='hṛṣyati',
                             chapter='3')
    generator = VerbClass4Generator()
    words = generator.generate_present_indicative_active(lex_entry)
    assert len(words) == 9
    for (i, surface, person, number) in [(0, "hṛṣyāmi", Person.FIRST, Number.SINGULAR),
                                         (1, "hṛṣyāvaḥ", Person.FIRST, Number.DUAL),
                                         (2, "hṛṣyāmaḥ", Person.FIRST, Number.PLURAL),
                                         (3, "hṛṣyasi", Person.SECOND, Number.SINGULAR),
                                         (4, "hṛṣyathaḥ", Person.SECOND, Number.DUAL),
                                         (5, "hṛṣyatha", Person.SECOND, Number.PLURAL),
                                         (6, "hṛṣyati", Person.THIRD, Number.SINGULAR),
                                         (7, "hṛṣyataḥ", Person.THIRD, Number.DUAL),
                                         (8, "hṛṣyanti", Person.THIRD, Number.PLURAL)]:
        assert words[i].surface_form == surface
        assert words[i].person == person
        assert words[i].number == number
        assert words[i].tense == Tense.PRESENT
        assert words[i].voice == Voice.ACTIVE
        assert words[i].mood == Mood.INDICATIVE


def test_present_indicative_active_drs():
    lex_entry = LexicalEntry(id=14,
                             form='dṛś',
                             pos=PartOfSpeech.FINITE_VERB,
                             definition='to see',
                             verb_class=VerbClass.IV,
                             verb_surface='paśyati',
                             chapter='3')
    generator = VerbClass4Generator()
    words = generator.generate_present_indicative_active(lex_entry)
    assert len(words) == 9
    for (i, surface, person, number) in [(0, "paśyāmi", Person.FIRST, Number.SINGULAR),
                                         (1, "paśyāvaḥ", Person.FIRST, Number.DUAL),
                                         (2, "paśyāmaḥ", Person.FIRST, Number.PLURAL),
                                         (3, "paśyasi", Person.SECOND, Number.SINGULAR),
                                         (4, "paśyathaḥ", Person.SECOND, Number.DUAL),
                                         (5, "paśyatha", Person.SECOND, Number.PLURAL),
                                         (6, "paśyati", Person.THIRD, Number.SINGULAR),
                                         (7, "paśyataḥ", Person.THIRD, Number.DUAL),
                                         (8, "paśyanti", Person.THIRD, Number.PLURAL)]:
        assert words[i].surface_form == surface
        assert words[i].person == person
        assert words[i].number == number
        assert words[i].tense == Tense.PRESENT
        assert words[i].voice == Voice.ACTIVE
        assert words[i].mood == Mood.INDICATIVE