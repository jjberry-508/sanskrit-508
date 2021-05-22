from db.mysql_repository import *


repo = MysqlRepository()
verb_entry = {'id': 8,
              'form': u'bhṛ',
              'pos': 'verb',
              'definition': 'to bear, carry',
              'verb_class': 'I',
              'verb_surface': 'bharati',
              'preverb': None,
              'noun_gender': None,
              'noun_declension': None,
              'chapter': 4}
noun_entry = {'id': 80,
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
