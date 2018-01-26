"""
This module contains some helpful classes for testing purposes.
"""
import spacy
from .singleton import Singleton


class SpacyMock:
    """
    Helper class to mock spacy for testing purposes.
    """
    def __init__(self, explain_output):
        """
        Initializes the mock with some values to override spacy methods.
        :param explain_output: The desired custom explain output for this mock.
        """
        self.explain_output = explain_output

    def explain(self, _):
        """
        Mocks the explain method of spacy to return a custom output.
        :param _: the input of the explain function, just to match method signature.
        :return: the custom explain_output provided to the mock.
        """
        return self.explain_output


class SpacySingleton(metaclass=Singleton):
    """
    This class creates a singleton that has the spacy nlp module for testing purposes
    """
    def __init__(self):
        self.nlp = spacy.load('en')
