"""
    There are 10 WH- words
    The pronouns are who, whose, whom, which, what, that.
    The adverbs are:where, when, why, how.
    If a sentence starts with one of these it is almost always a question.
    If it does not, then the likelihood is zero until further analysis is node.
    """
import spacy


def question_likelihood(parsed_data, sub_component=False):
    """
    Determines likelihood that a parsed spacy sentence is a question.

    Keyword arguments:
    spacy -- Spacy English model
    parsed_data -- Spacy text object
    sub_component -- If True will not attempt recursion (default = False)

    Return:
    float -- likelihood of question
    """
    starts_with_wh = spacy.explain(parsed_data[0].tag_).startswith(u'wh-')
    is_question = 0.95 if starts_with_wh else 0.0

    # check if the sentence starts with to be or has
    non_wh_question_starters = [
        u'be',
        u'do',
        u'could',
        u'should',
        u'may',
        u'can',
        u'shall',
        u'have',
        u'will',
        u'doe',
        u'would']
    if parsed_data[0].lemma_ in non_wh_question_starters:
        is_question = 0.95

    # if second word is not a verb then this is probably not a question
    if len(parsed_data) > 1 and starts_with_wh:
        is_question += -0.45 if parsed_data[1].pos_ != u'VERB' else 0

    # the case of 'to whom should I write this check?'
    if parsed_data[0].lemma_ == u'to':
        if spacy.explain(parsed_data[1].tag_).startswith(u'wh-'):
            is_question = 0.95

    # break down the comma seperated components of a sentence
    # analyze the components
    # Todo: enhance this to break on multiple punct types.
    if not sub_component and is_question <= 0.5:
        component_tokens = [[]]
        i = 0
        for token in parsed_data:
            if token.pos_ == 'PUNCT' and token.orth_ == ',':
                i += 1
                component_tokens.append([])
                continue
            component_tokens[i].append(token)

        if len(component_tokens) > 1:
            is_question = max(
                [question_likelihood(component, True)
                 for component in component_tokens if len(component) > 0])

    return is_question
