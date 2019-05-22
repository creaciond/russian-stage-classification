from copy import copy
from nltk.corpus import stopwords
from pymystem3 import Mystem
import warnings

warnings.simplefilter("ignore")
stops = set(stopwords.words("russian"))
mystem = Mystem()


def extract_lemmas(directions_raw, mystem):
    """Performs lemmatization of the directions.

    :arg directions_raw - (list of str) list of particular play's directions the
    way they were extracted from the text
    :arg mystem - an instance of Mystem, morphological analyzer, part of
    pymoystem3 module (a Python wrapper for the original programme)

    :return directions_lemmas - (list of str) same directions yet converted to
    their lemmas"""
    directions_lemmas = []
    for direction in directions_raw:
        words_analyses = mystem.analyze(direction)
        dir_lemmas = [parse['analysis'][0]['lex'] for parse in words_analyses if parse.get('analysis')]
        directions_lemmas.append(dir_lemmas)
    return directions_lemmas


def extract_pos(directions_raw, mystem):
    """Computes POS tags for directions.

    :arg directions_raw - (list of str) list of particular play's directions the
    way they were extracted from the text
    :arg mystem - an instance of Mystem, morphological analyzer, part of
    pymoystem3 module (a Python wrapper for the original programme)

    :return directions_morph - (list of str lists) list of POS tags for each
    direction"""
    directions_pos = []
    for direction in directions_raw:
        words_analyzed = mystem.analyze(direction)
        grammar_info = [parse["analysis"][0]["gr"] for parse in words_analyzed if parse.get("analysis")]
        dir_pos = [tag.split(",")[0] for tag in grammar_info]
        directions_pos.append(dir_pos)
    return directions_pos


def prepare_for_classification(directions_lemmas, directions_pos, stops):
    """Performs direction transformations to enhance the quality of the TF-IDF
    and other algorithms used later for classification.
    1) replaces all proper nouns usage with a word ИМЯ & part of speech PROPN
    2) removes stop-words

    :arg directions_lemmas - (list of str lists) same directions already converted to
    their lemmas
    :arg directions_pos - (list of str lists) list of POS tags for each
    direction
    :arg stops - (set of str) all stopwords to remove

    :return clf_all_directions - (list of str) directions ready for putting into
    classifiers
    :return clf_pos - (list of str) POS of corresponding lemmas"""
    clf_all_directions = []
    clf_lemmas = copy(directions_lemmas)
    for dir_num, direction_l in enumerate(directions_lemmas):
        for lem_num, lemma in enumerate(direction_l):
            if lemma in stops:
                del clf_lemmas[dir_num][lem_num]
                del directions_pos[dir_num][lem_num]
            lemma_analyzed = mystem.analyze(lemma)
            all_gr = lemma_analyzed[0]['analysis'][0]['gr']
            pos = all_gr.split(",")[1]
            if (pos == "имя") or (pos == "отч"):     
                clf_lemmas[dir_num][lem_num] = "ИМЯ"
                directions_pos[dir_num][lem_num] = "PROPN"
        if len(directions_pos[dir_num]) == len(clf_lemmas[dir_num]):
            clf_direction = clf_lemmas[dir_num] + directions_pos[dir_num]
            clf_all_directions.append(clf_direction)
    return clf_all_directions
