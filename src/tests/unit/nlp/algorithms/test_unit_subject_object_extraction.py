"""Tests the extractor of subject-verb objects"""

import pytest
from analysis.algorithms.subject_object_extraction import find_svos
from tests.unit.utils.spacy_utils import SpacySingleton

TEST_DATA = [
    ("If i don't pay the fee what will happen? i don't think i can pay the fee.",
     {('i', '!pay', 'fee'), ('i', 'pay', 'fee')}),
    ("i don't have other fees", {('i', '!have', 'fees')}),
    ("they ate the pizza with anchovies.", {('they', 'ate', 'pizza')}),
    ("i have no other financial assistance available and he certainly won't pay the fees.",
     {('i', '!have', 'assistance'), ('he', '!pay', 'fees')}),
    ("i have no other financial assistance available and he certainly won't provide support.",
     {('he', '!provide', 'support'), ('i', '!have', 'assistance')}),
    ("he did not pay the fee", {('he', '!pay', 'fee')}),
    ("he had the money and paid the fee for my friend and i.", {('he', 'had', 'money')}),
    ("he told me I should pay the fee", {('he', 'told', 'me'), ('i', 'pay', 'fee')})
]


@pytest.mark.parametrize("sent,tokens", TEST_DATA)
def test_svos(sent, tokens):
    """
    :param sent: the sentence to extract svos from
    :param tokens: the correct svos that should be extracted
    """
    tok = SpacySingleton().nlp(sent)
    svos = find_svos(tok)
    assert set(svos) == tokens
