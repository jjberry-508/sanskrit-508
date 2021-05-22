from db.repository import *
import mysql.connector


class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': '32000',
            'database': 'sanskrit'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
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
        lexical_entry = LexicalEntry(form=entry.get('form'),
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
