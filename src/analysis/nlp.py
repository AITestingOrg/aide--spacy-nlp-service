import spacy
from spacy import displacy

from ..common.models.node import Node
from .algorithms.subject_object_extraction import findSVOs
from ..common.persitence.wrapper_factory import WrapperFactory
from .algorithms.question_classifier import question_likelihood

nlp = spacy.load('en')
state = {}


class NLP:
    def __init__(self):
        self.db = WrapperFactory.build_neo4j_wrapper(
            'localhost', 7687, 'neo4j', 'test')
        self.nsubj = None

    def annotate(self, text, debug=False):
        output = {}
        output['text'] = text
        if len(text.split(' ')) == 1:
            ideas = self.db.get_direct_relations(text.strip())
            related_nodes = {}
            for idea in ideas.records():
                if idea['r'].type not in related_nodes:
                    related_nodes[idea['r'].type] = []
                related_nodes[idea['r'].type].append(
                    idea['node'].properties['name'])
            output['ideas'] = [[text.strip(), edge, ', '.join(related_nodes[edge])]
                               for edge in related_nodes]
            return output

        parsedData = nlp(text)

        for sent in parsedData.sents:
            sent = ''.join(sent.string.strip())
            if len(sent) > 3:
                sent = nlp(sent)
                self.process_sentence(sent, output, debug, write)

        if 'nsubj' in output['structure']:
            ideas = self.db.get_direct_relations(self.nsubj.lemma_)
            related_nodes = {}
            for idea in ideas.records():
                if idea['r'].type not in related_nodes:
                    related_nodes[idea['r'].type] = []
                related_nodes[idea['r'].type].append(
                    idea['node'].properties['name'])
            output['ideas'] = [[output['structure']['nsubj'].strip(), edge, ', '.join(
                related_nodes[edge])] for edge in related_nodes]

        return output

    def process_sentence(self, sent, output, debug, write):
        print('TEXT ' + sent.text)
        output['structure'] = {}

        # Determine if this is a question
        output['is_question'] = question_likelihood(sent)

        # Entities
        output['entities'] = self.extract_entities(sent)

        # Find all the subject verb pairs
        output['svos'] = findSVOs(sent)
        nsubj_exp = ''
        for token in sent:
            print(token.text.lower(), token.dep_, nsubj_exp)
            if token.dep_ == 'nsubj':
                output['structure']['nsubj'] = token.text.lower()
                self.nsubj = token
                nsubj_exp = spacy.explain(token.tag_)

                answer = self.db.get_node_from_relationship(
                    token.lemma_, token.head.lemma_).single()
                output['answer'] = answer['node'].properties['name'] if answer != None else None
            elif token.dep_ == 'ROOT':
                output['structure']['root'] = token.text.lower()
            elif output['is_question'] and token.dep_ == 'dobj' or \
                    output['is_question'] and \
                    token.dep_ == 'dobj' and \
                    nsubj_exp.startswith('wh-'):
                print('Looking for alternative nsubj')
                output['structure']['nsubj'] = token.lemma_
                self.nsubj = token
                output['structure']['edge'] = token.head.lemma_
                print('Querying for answer')
                answer = self.db.get_node_from_relationship(
                    token.lemma_, token.head.lemma_).single()
                output['answer'] = answer['node'].properties['name'] if answer != None else None

        if write:
            for svo in output['svos']:
                if output['is_question'] == False:
                    print(' '.join(svo))
                    svoParsed = nlp(' '.join(svo))
                    if spacy.explain(svoParsed[0].tag_).startswith('noun') and svoParsed[1].lemma_ != '!':
                        print('Inserting svo')
                        self.db.insert_edge(
                            svoParsed[0].lemma_, svoParsed[2].lemma_, svoParsed[1].lemma_)

        if output['is_question'] and 'nsubj' in output['structure'] and output['structure']['nsubj'] in state and state[output['structure']['nsubj']] == True:
            output['result'] = output['structure']['nsubj']

        if debug:
            output['lexicon'] = []
            output['dependencies'] = []
            # Lexicon and Dependencies
            lexicon, deps = self.extract_debug_data(sent)
            output['lexicon'].extend(lexicon)
            output['dependencies'].extend(deps)

            # Display graph
            output['svgs'] = self.extract_debug_graphs(sent)

