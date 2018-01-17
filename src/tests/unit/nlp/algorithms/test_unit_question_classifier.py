from analysis.algorithms.question_classifier import question_likelihood
import tests.unit.utils.spacy_utils as utils
import spacy

# Given a sentence starts with a WH word


# When the sentence is a question that starts with 'Where'
# Then the result is above 85% likelihood
def test_positive_wh_where_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('Where is Tom?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'When'
# and has a to be component
# Then the result is above 85% likelihood
def test_positive_wh_when_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('When is Tom going to the store?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'how'
# Then the result is above 85% likelihood
def test_positive_wh_how_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('How did the chicken cross the road?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# Given a sentence does not start with a wh word

# When the sentence is a question that starts with 'should'
# Then the result is above 85% likelihood
def test_positive_should_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('Should there be a fee?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'would'
# Then the result is above 85% likelihood
def test_positive_would_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('Would traveling across the border be legal?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'will'
# Then the result is above 85% likelihood
def test_positive_will_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('Will there be a fee?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'Does'
# Then the result is above 85% likelihood
def test_positive_does_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('Does he have to pay the fee?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'Do'
# Then the result is above 85% likelihood
def test_positive_do_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('Do you enjoy paying fees?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'is'
# Then the result is above 85% likelihood
def test_positive_is_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('Is the rooster crossing the road?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'are'
# Then the result is above 85% likelihood
def test_positive_are_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('Are you going to translate these sentences?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'to'
# Then the result is above 85% likelihood
def test_positive_to_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('To whom should I write this check for?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'has'
# Then the result is above 85% likelihood
def test_positive_has_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('Has Tom returned from the store?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'have'
# Then the result is above 85% likelihood
def test_positive_have_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('Have you ever eaten ramen?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'could'
# Then the result is above 85% likelihood
def test_positive_could_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('Could you pay the fee?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'may'
# Then the result is above 85% likelihood
def test_positive_may_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('May I assist you?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'can'
# Then the result is above 85% likelihood
def test_positive_can_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('Can you pay the fee?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'shall'
# Then the result is above 85% likelihood
def test_positive_shall_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('Shall we go?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# Given a sentences with subject verb injection not occuring
# in the first component.


# When the sentence is a question that starts with 'if'
# Then the result is above 85% likelihood
def test_positive_component_sentence1(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('If I travel to NY, do I need to pay a fee?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'when'
# Then the result is above 85% likelihood
def test_positive_component_sentence2(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('When I travel to NY, do I need to pay a fee?')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94


# When the sentence is a question that starts with 'I'
# Then the result is above 85% likelihood
def test_positive_component_sentence3(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp("I know he is here, is she here as well?")
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood > 0.94

# Given a sentences that starts with a WH word.


# When the sentence is not a question that starts with 'When'
# Then the result is less than 50% likelihood
def test_negative_wh_when_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp('When Tom went to the store, he bought bread.')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood <= 0.50


# When the sentence is not a question that starts with 'Why'
# Then the result is less than 50% likelihood
def test_negative_wh_what_sentence(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp(
        'Why Dumbo suddenly burst into tears no longer remains a mystery.')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood <= 0.50


# When the sentence is not a question that starts with 'When'
# Then the result is less than 50% likelihood
def test_negative_wh_when_sentence3(mocker):
    # arrange
    spacySingleton = utils.SpacySingleton()
    text = spacySingleton.nlp(
        'When the beguine will begin depends on when the beguiners show up.')
    # act
    likelihood = question_likelihood(spacy, text)
    # assert
    assert likelihood <= 0.50
