"""
Annotator utilizes Spacy to annotate text.
"""

from .algorithms.subject_object_extraction import find_svos
from .algorithms.question_classifier import question_likelihood
from .algorithms.spacy_utils import extract_entities
from .algorithms.spacy_utils import extract_debug_data
from .algorithms.spacy_utils import extract_debug_graphs

QUESTION_LIKELIHOOD = 'question_likelihood'
IDEAS = 'ideas'
TEXT = 'text'
LEXICON = 'lexicon'
DEPENDENCIES = 'dependencies'
ANSWER = 'answer'
ENTITIES = 'entities'
SVO = 'svos'
STRUCTURE = 'structure'
SVGS = 'svgs'


class Annotator(object):
    """
    The Annotator annotates blobs of text, returning Spacy's annotations in
    addition to custom annotations about the text.the
    """

    def __init__(self, spacy_en):
        """
        Constructor for annotator.

        Keyword arguments:
        spacy_en -- Spacy English model
        """
        self.nsubj = None
        self.nlp = spacy_en

    def annotate(self, text, extras=False):
        """
        Annotate text. The text can be in sentence or large blobs.

        Keyword arguments:
        text -- text string to annotate (default None)
        extras -- enables extra information (Lexicon, Dependencies, SVGs)
            (default False)

        Returns:
        list - a list of annotated sentence(s)
        """
        parsed_data = self.nlp(text)
        output = []

        # break down the blob into sentences, processing them sequentially.
        for sent in parsed_data.sents:
            sent = ''.join(sent.string.strip())
            # check if anything is available to parse
            if len(sent) >= 1:
                sent = self.nlp(sent)
                output.append(self.process_sentence(sent, extras))

        return output

    def process_sentence(self, sent, extras):
        """
        Processes a parsed Spacy sentence.

        Keyword arguments:
        sent -- Spacy text object (default None)
        extras -- enables extra information (Lexicon, Dependencies, SVGs)
            (default False)

        Returns:
        An annotated sentence
        """
        output = {}
        output[STRUCTURE] = {}

        # Determine the likelihood of this sentence being a question
        output[QUESTION_LIKELIHOOD] = question_likelihood(sent)

        # gather entities
        output[ENTITIES] = extract_entities(sent)

        # Find all the subject verb pairs
        output[SVO] = find_svos(sent)

        # Find noun subject
        nsubj_exp = ''
        for token in sent:
            if token.dep_ == 'nsubj':
                output[STRUCTURE]['nsubj'] = token.text.lower()
                self.nsubj = token
            elif token.dep_ == 'ROOT':
                output[STRUCTURE]['root'] = token.text.lower()
            elif output[QUESTION_LIKELIHOOD] and token.dep_ == 'dobj' or \
                    output[QUESTION_LIKELIHOOD] and \
                    token.dep_ == 'dobj' and \
                    nsubj_exp.startswith('wh-'):
                output[STRUCTURE]['nsubj'] = token.lemma_
                self.nsubj = token
                output[STRUCTURE]['edge'] = token.head.lemma_

        # include extras if needed
        if extras:
            # Lexicon and Dependencies
            output[LEXICON], \
                output[DEPENDENCIES] = extract_debug_data(self.nlp, sent)

            # Display graph
            output[SVGS] = extract_debug_graphs(self.nlp, sent)
        return output
