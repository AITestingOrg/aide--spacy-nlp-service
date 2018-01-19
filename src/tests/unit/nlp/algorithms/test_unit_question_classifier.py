"""Tests for the question classifier"""

import pytest
from analysis.algorithms.question_classifier import question_likelihood
import tests.unit.utils.spacy_utils as utils

TEST_DATA = [
    (True, 'Where is Tom?', 0.94),
    (True, 'When is Tom going to the store?', 0.94),
    (True, 'How did the chicken cross the road?', 0.94),
    (True, 'Should there be a fee?', 0.94),
    (True, 'Would traveling across the border be legal?', 0.94),
    (True, 'Will there be a fee?', 0.94),
    (True, 'Does he have to pay the fee?', 0.94),
    (True, 'Do you enjoy paying fees?', 0.94),
    (True, 'Is the rooster crossing the road?', 0.94),
    (True, 'Are you going to translate these sentences?', 0.94),
    (True, 'To whom should I write this check for?', 0.94),
    (True, 'Has Tom returned from the store?', 0.94),
    (True, 'Have you ever eaten ramen?', 0.94),
    (True, 'Could you pay the fee?', 0.94),
    (True, 'May I assist you?', 0.94),
    (True, 'Can you pay the fee?', 0.94),
    (True, 'Shall we go?', 0.94),
    (True, 'If I travel to NY, do I need to pay a fee?', 0.94),
    (True, 'When I travel to NY, do I need to pay a fee?', 0.94),
    (True, 'I know he is here, is she here as well?', 0.94),
    (False, 'When Tom went to the store, he bought bread.', 0.50),
    (False, 'Why Dumbo suddenly burst into tears no longer remains a mystery.', 0.50),
    (False, 'When the beguine will begin depends on when the beguiners show up.', 0.50),
]


@pytest.mark.parametrize("likely,sent,score", TEST_DATA)
def test_positive_wh_where_sentence(likely, sent, score):
    """
    :param likely: if the sentence is going to be determined to be a test or not
    :param sent: the sentence to test
    :param score: the threshold score to validate


    High likelihood:
        Questions that starts with 'When' and has a to be component
        Questions that start with 'how', 'who', 'should', 'would', 'will', 'do', 'does',
            'is', 'are', 'am', 'to', 'has', 'have', 'can', 'could', 'may', 'shall', 'if'
        Compound question that start with a statement and are followed with a question.

    Low likelihood:
        Sentences that start with 'when', 'why' but are not questions.
    """
    # arrange
    spacy_singleton = utils.SpacySingleton()
    text = spacy_singleton.nlp(sent)
    # act
    likelihood = question_likelihood(text)
    # assert
    if likely:
        assert likelihood > score
    else:
        assert likelihood < score
