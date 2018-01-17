def extract_debug_data(self, spacy, parsedData):
    lexicon = []
    deps = []
    for token in parsedData:
        lexicon.append(
            [token.orth_, spacy.explain(token.pos_), spacy.explain(token.tag_), token.tag_, token.lemma_])
        deps.append(
            [token.orth_, token.dep_, token.head.orth_, ' '.join([t.orth_ for t in token.lefts]),
             ' '.join([t.orth_ for t in token.rights])])
    return lexicon, deps


def extract_debug_graphs(self, spacy, parsedData):
    return [displacy.render(parsedData, style='dep'), displacy.render(parsedData, style='ent')]


def extract_entities(self, spacy, parsedData):
    entities = []
    ents = list(parsedData.ents)
    for entity in ents:
        entities.append(
            [str(entity.label), entity.label_, ' '.join([str(t.orth_) for t in entity])])
    return entities
