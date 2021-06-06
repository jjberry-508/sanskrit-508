import abc

from model.lexical_entry import LexicalEntry
from model.word import Word


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_lexicon(self) -> list[LexicalEntry]:
        raise NotImplementedError

    @abc.abstractmethod
    def persist_generated_words(self, word_list: list[Word]):
        raise NotImplementedError

    @abc.abstractmethod
    def drop_generated_words(self):
        raise NotImplementedError

    @abc.abstractmethod
    def create_word_tables(self):
        raise NotImplementedError

    @abc.abstractmethod
    def select_generated_words(self) -> list[Word]:
        raise NotImplementedError

    @abc.abstractmethod
    def query_word_form(self, word_form: str) -> list[Word]:
        raise NotImplementedError
