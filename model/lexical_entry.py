from model.common_enums import *


class LexicalEntry:

    def __init__(self,
                 form: str,
                 pos: PartOfSpeech,
                 definition: str,
                 verb_class: VerbClass = None,
                 verb_surface: str = None,
                 preverb: str = None,
                 noun_gender: Gender = None,
                 noun_declension: NounDeclension = None,
                 chapter: str = None):
        self.form = form
        self.pos = pos
        self.definition = definition
        self.verb_class = verb_class
        self.verb_surface = verb_surface
        self.preverb = preverb
        self.noun_gender = noun_gender
        self.noun_declension = noun_declension
        self.chapter = chapter
