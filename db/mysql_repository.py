import mysql.connector

from db.repository import *
from model.common_enums import *
from model.finite_verb import FiniteVerb


class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',  # to run LOCALLY, this should be localhost
            'port': '32000',  # to run LOCALLY, this should be 32000
            'database': 'sanskrit'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def map_pos(self, entry: dict) -> PartOfSpeech:
        pos_switcher = {'indeclinable': PartOfSpeech.INDECLINABLE,
                        'parsed form': PartOfSpeech.INDECLINABLE,
                        'verb': PartOfSpeech.FINITE_VERB,
                        'noun': PartOfSpeech.NOUN,
                        'postposition': PartOfSpeech.INDECLINABLE,
                        'adjective': PartOfSpeech.ADJECTIVE,
                        'pronominal adjective': PartOfSpeech.PRONOUN,
                        'ifc': PartOfSpeech.INDECLINABLE,
                        'numeral': PartOfSpeech.NUMERAL}
        pos = pos_switcher.get(entry.get('pos'), None)
        return pos

    def map_verb_class(self, entry: dict) -> VerbClass:
        verb_class_switcher = {'I': VerbClass.I,
                               'IV': VerbClass.IV,
                               'IV irreg.': VerbClass.IV,
                               'VI': VerbClass.VI,
                               'I irreg.': VerbClass.I,
                               'VI irreg.': VerbClass.VI,
                               'X': VerbClass.X}
        verb_class = verb_class_switcher.get(entry.get('verb_class'), None)
        return verb_class

    def map_noun_gender(self, entry: dict) -> Gender:
        noun_gender_switcher = {'neuter': Gender.NEUTER,
                                'masculine': Gender.MASCULINE,
                                'neuter/masculine': Gender.NEUTER,
                                'feminine': Gender.FEMININE}
        noun_gender = noun_gender_switcher.get(entry.get('noun_gender'), None)
        return noun_gender

    def map_noun_declension(self, entry: dict) -> NounDeclension:
        noun_declension_switcher = {'a': NounDeclension.SHORT_A,
                                    'u': NounDeclension.SHORT_U,
                                    'irreg.': NounDeclension.SHORT_A,
                                    'ī': NounDeclension.LONG_I}
        noun_declension = noun_declension_switcher.get(entry.get('noun_declension', None))
        return noun_declension

    def mapper(self, entry: dict) -> LexicalEntry:
        lexical_entry = LexicalEntry(id=entry.get('id'),
                                     form=entry.get('form'),
                                     pos=self.map_pos(entry),
                                     definition=entry.get('definition'),
                                     verb_class=self.map_verb_class(entry),
                                     verb_surface=entry.get('verb_surface'),
                                     preverb=entry.get('preverb'),
                                     noun_gender=self.map_noun_gender(entry),
                                     noun_declension=self.map_noun_declension(entry),
                                     chapter=entry.get('chapter'))
        return lexical_entry

    def load_lexicon(self) -> list[LexicalEntry]:
        sql = 'SELECT * FROM lexicon'
        self.cursor.execute(sql)
        entries = [{'id': id,
                    'form': form,
                    'pos': pos,
                    'definition': definition,
                    'verb_class': verb_class,
                    'verb_surface': verb_surface,
                    'preverb': preverb,
                    'noun_gender': noun_gender,
                    'noun_declension': noun_declension,
                    'chapter': chapter
                    } for (id, form, pos, definition, verb_class, verb_surface, preverb,
                           noun_gender, noun_declension, chapter) in self.cursor]
        lexicon = [self.mapper(entry) for entry in entries]
        return lexicon

    def insert_finite_verb(self, fields, last_id):
        sql = ("INSERT INTO finite_verbs "
               "(word_id, person, number, tense, voice, mood) "
               f"VALUES ({last_id}, "
               f"{fields.get('person')}, "
               f"{fields.get('number')}, "
               f"{fields.get('tense')}, "
               f"{fields.get('voice')}, "
               f"{fields.get('mood')})"
               )
        self.cursor.execute(sql)

    def persist_generated_words(self, word_list: list[Word]):
        for w in word_list:
            fields = w.get_fields()
            sql = ("INSERT INTO words "
                   "(form, lexicon_id) "
                   f"VALUES (N'{fields.get('surface_form')}', {fields.get('lex_entry').get('id')})"
                   )
            self.cursor.execute(sql)
            last_id = self.cursor.getlastrowid()
            if fields.get('lex_entry').get('pos') == PartOfSpeech.FINITE_VERB:
                self.insert_finite_verb(fields, last_id)
        self.connection.commit()

    def drop_generated_words(self):
        sql = "DROP TABLE IF EXISTS finite_verbs"
        self.cursor.execute(sql)
        sql = "DROP TABLE IF EXISTS words"
        self.cursor.execute(sql)
        self.connection.commit()

    def create_word_tables(self):
        sql = ("CREATE TABLE words ("
               "id INT NOT NULL AUTO_INCREMENT,"
               "form NVARCHAR(30),"
               "lexicon_id INT NOT NULL,"
               "CONSTRAINT pk_id PRIMARY KEY (id),"
               "CONSTRAINT fk_lexicon_id FOREIGN KEY (lexicon_id) REFERENCES lexicon (id)"
               ")")
        self.cursor.execute(sql)
        sql = ("CREATE TABLE finite_verbs ("
               "id INT NOT NULL AUTO_INCREMENT,"
               "word_id INT NOT NULL,"
               "person INT,"
               "number INT,"
               "tense INT,"
               "voice INT,"
               "mood INT,"
               "CONSTRAINT pd_id PRIMARY KEY (id),"
               "CONSTRAINT fk_word_id FOREIGN KEY (word_id) REFERENCES words (id)"
               ")")
        self.cursor.execute(sql)
        self.connection.commit()

    def select_generated_words(self) -> list[Word]:
        sql = ("SELECT w.id AS word_id, w.form AS surface_form, w.lexicon_id AS lexicon_id, "
               "l.form AS form, l.pos AS pos, l.definition AS definition, "
               "l.verb_class AS verb_class, l.verb_surface AS verb_surface, "
               "l.preverb AS preverb, l.noun_gender AS noun_gender, "
               "l.noun_declension AS noun_declension, l.chapter AS chapter "
               "FROM words w "
               "INNER JOIN lexicon l "
               "ON w.lexicon_id = l.id"
               )
        self.cursor.execute(sql)
        entries = [{'id': word_id,
                    'surface_form': surface_form,
                    'lexical_entry': {
                        'id': lexicon_id,
                        'form': form,
                        'pos': pos,
                        'definition': definition,
                        'verb_class': verb_class,
                        'verb_surface': verb_surface,
                        'preverb': preverb,
                        'noun_gender': noun_gender,
                        'noun_declension': noun_declension,
                        'chapter': chapter
                    }} for (word_id, surface_form, lexicon_id, form, pos, definition,
                            verb_class, verb_surface, preverb, noun_gender, noun_declension,
                            chapter) in self.cursor]
        words = [Word(lex_entry=self.mapper(entry.get('lexical_entry')),
                      surface_form=entry.get('surface_form')) for entry in entries]
        return words

    def query_word_form(self, word_form: str) -> list[Word]:
        sql = ("SELECT w.id AS word_id, "
               "  w.form AS surface_form, "
               "  l.id AS lexicon_id, "
               "  l.form AS form, "
               "  l.pos AS pos, "
               "  l.definition AS definition, "
               "  l.verb_class AS verb_class, "
               "  l.verb_surface AS verb_surface, "
               "  l.preverb AS preverb, "
               "  l.noun_gender AS noun_gender, "
               "  l.noun_declension AS noun_declension, "
               "  l.chapter AS chapter, "
               "  fv.person AS person, "
               "  fv.number AS number, "
               "  fv.tense AS tense, "
               "  fv.voice AS voice, "
               "  fv.mood AS mood "
               "FROM words w "
               "INNER JOIN lexicon l "
               "ON w.lexicon_id = l.id "
               "INNER JOIN finite_verbs fv "
               "ON w.id = fv.word_id "
               f"WHERE w.form= '{word_form}'"
               )
        self.cursor.execute(sql)
        entries = [{'id': word_id,
                    'surface_form': surface_form,
                    'person': Person(person),
                    'number': Number(number),
                    'tense': Tense(tense),
                    'voice': Voice(voice),
                    'mood': Mood(mood),
                    'lexical_entry': {
                        'id': lexicon_id,
                        'form': form,
                        'pos': pos,
                        'definition': definition,
                        'verb_class': verb_class,
                        'verb_surface': verb_surface,
                        'preverb': preverb,
                        'noun_gender': noun_gender,
                        'noun_declension': noun_declension,
                        'chapter': chapter
                    }} for (word_id, surface_form, lexicon_id, form, pos, definition,
                            verb_class, verb_surface, preverb, noun_gender, noun_declension,
                            chapter, person, number, tense, voice, mood) in self.cursor]
        words = [FiniteVerb(lex_entry=self.mapper(entry.get('lexical_entry')),
                            surface_form=entry.get('surface_form'),
                            person=entry.get('person'),
                            number=entry.get('number'),
                            tense=entry.get('tense'),
                            voice=entry.get('voice'),
                            mood=entry.get('mood')) for entry in entries]
        return words
