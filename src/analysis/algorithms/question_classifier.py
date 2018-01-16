import spacy


def is_question(parsedData):
    # There are 10 WH- words
    # The pronouns are who, whose, whom, which, what, that.
    # The adverbs are:where, when, why, how.
    # If a sentence starts with one of these it is almost always a question.
    # If it does not, then the likelihood is zero until further analysis is node.
    is_question = 0.95 if spacy.explain(
        parsedData[0].tag_).startswith('wh-') else 0.0

    # if second word is not be when "when" is the first word then it may not be a question
    if len(parsedData) > 1 and is_question:
        is_question += -0.25 if parsedData[0].lemma_ == 'when' and parsedData[1].lemma_ != 'be' else 0

    # if the sentence starts with a 'to be' word then it is most likely a question.
    if not is_question:
        is_question = 0.95 if parsedData[0].lemma_ == 'be' else is_question

    return is_question
