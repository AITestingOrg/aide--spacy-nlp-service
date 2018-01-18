from analysis.algorithms.subject_object_extraction import find_svos
from tests.unit.utils.spacy_utils import SpacySingleton


def test_svos1():
    tok = SpacySingleton().nlp(
        "If i don't pay the fee what will happen? i don't \
        think i can pay the fee.")
    svos = find_svos(tok)
    assert set(svos) == {('i', '!pay', 'fee'), ('i', 'pay', 'fee')}


def test_svos2():
    tok = SpacySingleton().nlp("i don't have other fees")
    svos = find_svos(tok)
    assert set(svos) == {('i', '!have', 'fees')}


def test_svos3():
    tok = SpacySingleton().nlp("they ate the pizza with anchovies.")
    svos = find_svos(tok)
    assert set(svos) == {('they', 'ate', 'pizza')}


def test_svos4():
    tok = SpacySingleton().nlp(
        "i have no other financial assistance available \
        and he certainly won't pay the fees.")
    svos = find_svos(tok)
    assert set(svos) == {('he', '!pay', 'fees')}


def test_svos5():
    tok = SpacySingleton().nlp(
        "i have no other financial assistance available,\
         and he certainly won't provide support.")
    svos = find_svos(tok)
    assert set(svos) == {('i', '!have', 'assistance'),
                         ('he', '!provide', 'support')}


def test_svos6():
    tok = SpacySingleton().nlp("he did not pay the fee")
    svos = find_svos(tok)
    assert set(svos) == {('he', '!pay', 'fee')}


def test_svos7():
    tok = SpacySingleton().nlp("he had the money and paid the fee \
        for my friend and i.")
    svos = find_svos(tok)
    assert set(svos) == {('he', 'had', 'money')}


def test_svos8():
    tok = SpacySingleton().nlp("he told me I should pay the fee")
    svos = find_svos(tok)
    assert set(svos) == {('he', 'told', 'me'), ('i', 'pay', 'fee')}
