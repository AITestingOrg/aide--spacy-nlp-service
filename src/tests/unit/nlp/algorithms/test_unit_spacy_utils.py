import tests.unit.utils.spacy_utils as utils
from analysis.algorithms.spacy_utils import extract_dependencies
from analysis.algorithms.spacy_utils import extract_compound_dependencies


short_sent = "Computer hardware is important."
long_sent_no_compounds = "there is a beautiful place somewhere that has small things and big stuff."
long_sent_mult_compounds = "The fish tank is by the bus stop and the swimming pool."


def test_correct_number_of_dependencies():
    # arrange
    spacy_singleton = utils.SpacySingleton()
    sent = spacy_singleton.nlp(short_sent)
    # act
    tokens = extract_dependencies(sent)
    # assert
    assert len(tokens) == 5


def test_correct_number_of_dependencies_longer():
    # arrange

    spacy_singleton = utils.SpacySingleton()
    sent = spacy_singleton.nlp(long_sent_mult_compounds)
    # act
    tokens = extract_dependencies(sent)
    # assert
    assert len(tokens) == len(long_sent_mult_compounds.split()) + 1


def test_multiple_compound_detected():
    # arrange
    spacy_singleton = utils.SpacySingleton()
    sent = spacy_singleton.nlp(long_sent_mult_compounds)
    # act
    tokens = extract_compound_dependencies(sent)
    # assert
    assert len(tokens) == 3


def test_no_compounds_found():
    # arrange
    spacy_singleton = utils.SpacySingleton()
    sent = spacy_singleton.nlp(long_sent_no_compounds)
    # act
    tokens = extract_dependencies(sent)
    # assert
    for token in tokens:
        assert token[1] != "compound"


def test_no_compounds_found_empty_list():
    # arrange
    spacy_singleton = utils.SpacySingleton()
    sent = spacy_singleton.nlp(long_sent_no_compounds)
    # act
    tokens = extract_compound_dependencies(sent)
    # assert
    assert len(tokens) == 0
