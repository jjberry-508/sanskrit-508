from model.lexical_entry import LexicalEntry


class Word:

    def __init__(self,
                 lex_entry: LexicalEntry,
                 surface_form: str):
        self.lex_entry = lex_entry
        self.surface_form = surface_form

    def get_fields(self) -> dict:
        fields = {
            'lex_entry': self.lex_entry.get_fields(),
            'surface_form': self.surface_form
        }
        return fields

    def get_json(self) -> dict:
        json = {
            'lex_entry': self.lex_entry.get_json(),
            'surface_form': self.surface_form
        }