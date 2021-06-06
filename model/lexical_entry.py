from model.common_enums import *


class LexicalEntry:

    def __init__(self,
                 id: int,
                 form: str,
                 pos: PartOfSpeech,
                 definition: str,
                 verb_class: VerbClass = None,
                 verb_surface: str = None,
                 preverb: str = None,
                 noun_gender: Gender = None,
                 noun_declension: NounDeclension = None,
                 chapter: str = None):
        self.id = id
        self.form = form
        self.pos = pos
        self.definition = definition
        self.verb_class = verb_class
        self.verb_surface = verb_surface
        self.preverb = preverb
        self.noun_gender = noun_gender
        self.noun_declension = noun_declension
        self.chapter = chapter

    def get_fields(self) -> dict:
        fields = {
            'id': self.id,
            'form': self.form,
            'pos': self.pos,
            'definition': self.definition,
            'verb_class': self.verb_class,
            'verb_surface': self.verb_surface,
            'preverb': self.preverb,
            'noun_gender': self.noun_gender,
            'noun_declension': self.noun_declension,
            'chapter': self.chapter
        }
        return fields

    def get_json(self) -> dict:
        json = {
            'form': self.form,
            'pos': self.pos.name.lower(),
            'definition': self.definition,
            'verb_class': self.verb_class.name if self.verb_class is not None else None,
            'verb_surface': self.verb_surface,
            'preverb': self.preverb,
            'noun_gender': self.noun_gender.name.lower() if self.noun_gender is not None else None,
            'noun_declension': self.noun_declension.name.lower() if self.noun_declension is not None else None,
            'chapter': self.chapter
        }
        return json
