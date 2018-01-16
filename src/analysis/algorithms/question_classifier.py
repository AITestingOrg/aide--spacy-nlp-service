def is_question(spacy, parsedData):
    # There are 10 WH- words
    # The pronouns are who, whose, whom, which, what, that.
    # The adverbs are:where, when, why, how.
    # If a sentence starts with one of these it is almost always a question.
    # If it does not, then the likelihood is zero until further analysis is node.
    starts_with_wh = spacy.explain(parsedData[0].tag_).startswith(u'wh-')
    is_question = 0.95 if starts_with_wh else 0.0

    # check if the sentence starts with to be or has
    if parsedData[0].lemma_ == u'has' or parsedData[0].lemma_ == u'be' or parsedData[0].lemma_ == u'do'  or parsedData[0].lemma_ == u'be':
        is_question = 0.95

    # if second word is not a verb then this is probably not a question
    if len(parsedData) > 1 and starts_with_wh:
        is_question += -0.45 if parsedData[1].pos_ != u'VERB' else 0

    return is_question
