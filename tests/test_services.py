from app.services import *
from db.mysql_repository import *

services = Services()
repo = MysqlRepository()

'''
# this is slow
def test_generate_words():
    services.generate_words()
    words = repo.select_generated_words()
    assert len(words) > 0
'''

def test_parse_word_bharami():
    info = services.parse_word('bharāmi')
    assert len(info) == 1
    assert info[0].get('person') == 'first'
    assert info[0].get('number') == 'singular'
    assert info[0].get('tense') == 'present'
    assert info[0].get('voice') == 'active'
    assert info[0].get('mood') == 'indicative'

def test_segment_compound():
    parsed = services.segment_compound(u'aṇḍasvedajarāyujāḥ')
    assert parsed == [[u'aṇḍa', u'sveda', u'jarāyu', u'jāḥ']]
