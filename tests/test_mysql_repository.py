from db.mysql_repository import *
from model.verb_class_1_generator import *

repo = MysqlRepository()
verb_entry = {'id': 9,
              'form': u'bhṛ',
              'pos': 'verb',
              'definition': 'to bear, carry',
              'verb_class': 'I',
              'verb_surface': 'bharati',
              'preverb': None,
              'noun_gender': None,
              'noun_declension': None,
              'chapter': 4}
noun_entry = {'id': 123,
              'form': u'ācāra',
              'pos': 'noun',
              'definition': 'conduct, manner',
              'verb_class': None,
              'verb_surface': None,
              'preverb': None,
              'noun_gender': 'masculine',
              'noun_declension': 'a',
              'chapter': 799}

def test_map_pos():
    pos = repo.map_pos(verb_entry)
    assert pos == PartOfSpeech.FINITE_VERB

def test_map_verb_class():
    vc = repo.map_verb_class(verb_entry)
    assert vc == VerbClass.I

def test_map_noun_gender():
    ng = repo.map_noun_gender(noun_entry)
    assert ng == Gender.MASCULINE

def test_map_noun_declension():
    nd = repo.map_noun_declension(noun_entry)
    assert nd == NounDeclension.SHORT_A

def test_null_verb():
    vc = repo.map_verb_class(noun_entry)
    assert vc is None

def test_null_noun():
    ng = repo.map_noun_gender(verb_entry)
    assert ng is None

def test_mapper():
    le = repo.mapper(verb_entry)
    assert le.pos == PartOfSpeech.FINITE_VERB
    assert le.verb_class == VerbClass.I
    assert le.noun_declension is None
    assert le.verb_surface == 'bharati'

def test_load_lexicon():
    lexicon = repo.load_lexicon()
    assert len(lexicon) >= 130

def persist_generated_words():
    generator = VerbClass1Generator()
    lex_entry = repo.mapper(verb_entry)
    words = generator.generate_present_indicative_active(lex_entry)
    repo.drop_generated_words()
    repo.create_word_tables()
    repo.persist_generated_words(words)
    word_list = repo.select_generated_words()
    assert len(word_list) == 9
