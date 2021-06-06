from app.util import tokenize, syllabify


def test_tokenize_bhr():
    word = u'bhṛ'
    tokens = tokenize(word)
    assert tokens == [u'bh', u'ṛ']


def test_tokenize_ksip():
    word = u'kṣip'
    tokens = tokenize(word)
    assert tokens == [u'k', u'ṣ', u'i', u'p']


def test_tokenize_davau():
    word = u'devau'
    tokens = tokenize(word)
    assert tokens == [u'd', u'e', u'v', u'au']


def test_tokenize_long_r():
    word = u'pṝt'
    tokens = tokenize(word)
    assert tokens == [u'p', u'ṝ', u't']


def test_syllabify_dana():
    word = u'dāna'
    syllables = syllabify(word)
    assert syllables == [[u'd', u'ā'], [u'n', u'a']]


def test_syllabify_mahant():
    word = u'mahant'
    syllables = syllabify(word)
    assert syllables == [[u'm', u'a'], [u'h', u'a', u'n', u't']]


def test_syllabify_svayamvarah():
    word = u'svayaṃvaraḥ'
    syllables = syllabify(word)
    assert syllables == [[u's', u'v', u'a'], [u'y', u'a', u'ṃ'], [u'v', u'a'], [u'r', u'a', u'ḥ']]


def test_syllabify_ksatriyah():
    word = u'kṣatriyaḥ'
    syllables = syllabify(word)
    assert syllables == [[u'k', u'ṣ', u'a', u't'], [u'r', u'i'], [u'y', u'a', u'ḥ']]

