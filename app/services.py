import db.mysql_repository
from model.verb_class_1_generator import *
from model.verb_class_4_generator import *
from app.graph import *
from app.util import *


class Vertex:

    def __init__(self, form: str, start: int, end: int):
        self.form = form
        self.start = start
        self.end = end


class Services:

    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()

    # Use case 2: the app takes a stem and returns all forms
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
    def parse_word(self, input_form: str) -> list[dict]:
        results = self.repo.query_word_form(input_form)
        words = []
        for w in results:
            if w.lex_entry.pos == PartOfSpeech.FINITE_VERB:
                words.append(self.repo.get_verb_details(w))
            else:
                words.append(w)
        return [w.get_json() for w in words]

    # Helper function for segment_compound
    def test_substr(self, t_list):
        words = []
        for i in range(len(t_list) + 1):
            substr = ''.join(t_list[:i])
            hits = self.parse_word(substr)
            if len(hits) > 0:
                words.append(substr)
        return words

    # Use case 3: the app takes a string and returns its constituent parts
    def segment_compound(self, input_form: str) -> list[list[str]]:
        tokens = tokenize(input_form)

        # Find all substring matches
        results = []
        for t in range(len(tokens)):
            result = self.test_substr(tokens[t:])
            if len(result) > 0:
                results.append([t, result])

        # Get start and end points for each substring that returned a match and create a vertex
        vertices = [Vertex('start', 0, 0)]
        for i in range(len(results)):
            start = results[i][0]
            for j in range(len(results[i][1])):
                form = results[i][1][j]
                end = start + len(form)
                vertices.append(Vertex(form, start, end))
        vertices.append(Vertex('end', len(input_form), len(input_form)))

        # Build the Graph
        n_vert = len(vertices)
        g = Graph(n_vert)
        # Add an edge if the start and end points of two vertices match
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if j == i:
                    continue
                if vertices[i].end == vertices[j].start:
                    g.add_edge(i, j)

        # Get the candidate parses from graph search
        paths = g.print_all_paths(0, n_vert - 1)
        breakdowns = []
        for path in paths:
            breakdown = []
            for i in path[1:-1]:
                breakdown.append(vertices[i].form)
            breakdowns.append(breakdown)
        return breakdowns


if __name__ == "__main__":
    services = Services()
    print(services.segment_compound('aṇḍasvedajarāyujāḥ'))
