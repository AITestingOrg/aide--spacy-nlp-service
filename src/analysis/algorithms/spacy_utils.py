"""
Contains methods to extract useful information from a parsed text.
"""


def extract_lexicon(spacy, parsed_data):
    """
    extracts the lexicon from the parsed data.

    Keyword arguments:
    spacy -- Spacy model to use.
    parsed_data -- the parsed text to extract lexicon from.

    Returns:
    list - a list of the lexicon inside parsed_data.
    """
    lexicon = []
    for token in parsed_data:
        lexicon.append([token.orth_, spacy.explain(token.pos_), spacy.explain(token.tag_), token.tag_, token.lemma_])
    return lexicon


def extract_dependencies(parsed_data):
    """
    extracts all the dependencies from the parsed data.

    Keyword arguments:
    parsed_data -- the parsed text to extract lexicon from.

    Returns:
    list - a list of the dependencies inside parsed_data.
    """
    deps = []
    for token in parsed_data:
        deps.append([token.orth_, token.dep_, token.head.orth_, ' '.join([t.orth_ for t in token.lefts]),
                     ' '.join([t.orth_ for t in token.rights])])
    return deps


def extract_compound_dependencies(parsed_data):
    """
    extracts only the compound dependencies from the parsed data.

    Keyword arguments:
    parsed_data -- the parsed text to extract lexicon from.

    Returns:
    list - a list of the compound dependencies inside parsed_data.
    """
    deps = []
    for token in parsed_data:
        if token.dep_ == "compound":
            deps.append([token.orth_, token.dep_, token.head.orth_, ' '.join([t.orth_ for t in token.lefts]),
                         ' '.join([t.orth_ for t in token.rights])])
    return deps


def extract_debug_data(spacy, parsed_data):
    """
    extracts useful lexicon and dependencies from the parsed data.

    Keyword arguments:
    spacy -- Spacy model to use.
    parsed_data -- the parsed text to extract lexicon from.

    Returns:
    (list, list) - a tuple with a list of the lexicon and a list of dependencies inside parsed_data.
    """
    return extract_lexicon(spacy, parsed_data), extract_dependencies(parsed_data)


def extract_debug_graphs(spacy, parsed_data):
    """
    extracts all the dependencies from the parsed data.

    Keyword arguments:
    spacy -- Spacy model to use.
    parsed_data -- the parsed text to extract lexicon from.

    Returns:
    list - a list of the dependencies inside parsed_data.
    """
    return [spacy.displacy.render(parsed_data, style='dep'), spacy.displacy.render(parsed_data, style='ent')]


def extract_entities(parsed_data):
    """
    extracts all the entities from the parsed data.

    Keyword arguments:
    parsed_data -- the parsed text to extract lexicon from.

    Returns:
    list - a list of the entities inside parsed_data.
    """
    entities = []
    ents = list(parsed_data.ents)
    for entity in ents:
        entities.append(
            [str(entity.label), entity.label_, ' '.join([str(t.orth_) for t in entity])])
    return entities
