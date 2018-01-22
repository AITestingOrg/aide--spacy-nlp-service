"""Tests some of the helper methods in algorithms.spacy_utils"""

import pytest
import tests.unit.utils.spacy_utils as utils
from analysis.algorithms.spacy_utils import extract_compound_dependencies
from analysis.algorithms.spacy_utils import extract_dependencies

SHORT_SENTENCE = "Computer hardware is important"
SENTENCE_NO_COMPOUNDS = "there is a beautiful place somewhere that has small things and big stuff"
LONG_SENTENCE_MULTIPLE_COMPOUNDS = "The fish tank is by the bus stop and the swimming pool"

TEST_DATA_DEPENDECY_COUNT = [
    (SHORT_SENTENCE, len(SHORT_SENTENCE.split())),
    (SENTENCE_NO_COMPOUNDS, len(SENTENCE_NO_COMPOUNDS.split())),
    (LONG_SENTENCE_MULTIPLE_COMPOUNDS, len(LONG_SENTENCE_MULTIPLE_COMPOUNDS.split()))
]

TEST_DATA_COMPOUND_COUNT = [
    (SHORT_SENTENCE, 1),
    (SENTENCE_NO_COMPOUNDS, 0),
    (LONG_SENTENCE_MULTIPLE_COMPOUNDS, 3)
]


@pytest.mark.parametrize("sent,expected_count", TEST_DATA_DEPENDECY_COUNT)
def test_number_of_dependencies(sent, expected_count):
    """
    Tests that the expected number of dependencies are found in a given sentence.

    :param sent: The sentence to check nlp analysis on.
    :param expected_count: The expected number of dependencies in the sentence.
    """
    # arrange
    spacy_singleton = utils.SpacySingleton()
    sent = spacy_singleton.nlp(sent)
    # act
    tokens = extract_dependencies(sent)
    # assert
    assert len(tokens) == expected_count


@pytest.mark.parametrize("sent,count", TEST_DATA_COMPOUND_COUNT)
def test_compound_detected(sent, expected_count):
    """
    Tests that the expected number of compound dependencies are found in a given sentence.

    :param sent: The sentence to check nlp analysis on.
    :param expected_count: The expected number of compound dependencies in the sentence.
    """
    # arrange
    spacy_singleton = utils.SpacySingleton()
    sent = spacy_singleton.nlp(sent)
    # act
    tokens = extract_compound_dependencies(sent)
    # assert
    assert len(tokens) == expected_count


def test_no_compounds_found():
    """Tests that in a sentence with no compound dependencies none is found."""
    # arrange
    spacy_singleton = utils.SpacySingleton()
    sent = spacy_singleton.nlp(SENTENCE_NO_COMPOUNDS)
    # act
    tokens = extract_dependencies(sent)
    # assert
    for token in tokens:
        assert token[1] != "compound"
