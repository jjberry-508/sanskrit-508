import abc
from model.common_enums import *
from model.lexical_entry import LexicalEntry


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_lexicon(self) -> list[LexicalEntry]:
        raise NotImplementedError
