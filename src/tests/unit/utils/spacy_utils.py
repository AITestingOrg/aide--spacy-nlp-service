import spacy
from .singleton import Singleton


class SpacyMock:
    def __init__(self, explain_output):
        self.explain_output = explain_output

    def explain(self, input):
        return self.explain_output


class SpacySingleton(metaclass=Singleton):
    def __init__(self):
        self.nlp = spacy.load('en')
