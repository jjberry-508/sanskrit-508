from model.lexical_entry import LexicalEntry


class Word:

    def __init__(self,
                 lex_entry: LexicalEntry,
                 surface_form: str):
        self.lex_entry = lex_entry
        self.surface_form = surface_form
