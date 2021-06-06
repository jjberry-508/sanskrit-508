import db.mysql_repository
from model.verb_class_1_generator import *
from model.verb_class_4_generator import *


class Services:

    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()

    def generate_words(self):
        # first clean up the existing tables
        self.repo.drop_generated_words()
        self.repo.create_word_tables()

        # load the lexical entries
        lexicon = self.repo.load_lexicon()
        for lex_entry in lexicon:
            # iterate through the lexicon and determine which generator to use
            # so far there are only 2 generators, so we'll skip the other words
            switcher = {(PartOfSpeech.FINITE_VERB, VerbClass.I): VerbClass1Generator,
                        (PartOfSpeech.FINITE_VERB, VerbClass.IV): VerbClass4Generator}
            try:
                generator = switcher.get((lex_entry.pos, lex_entry.verb_class), None)()

                # generate the forms
                word_list = generator.generate_present_indicative_active(lex_entry)

                # persist them to the db
                self.repo.persist_generated_words(word_list)
            except TypeError:
                # this will catch words that we haven't implemented a generator for
                pass

    # Use case 1: the app takes a word as input and returns morphological parse information
    def parse_word(self, input_form):
        # See if the word exists in the db
        results = self.repo.query_word_form(input_form)
        return [w.get_json() for w in results]

