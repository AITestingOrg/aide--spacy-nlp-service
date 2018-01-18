from flask import Blueprint
import spacy
from analysis.annotator import Annotator
from .api import Api

NLP = spacy.load('en')

# Create new blueprint with base path
nlp = Blueprint('nlp', __name__, url_prefix='/api')


@nlp.route("/annotate/<text>", methods=['GET'])
def get_annotated_text(text):
    return Api.respond(Annotator(NLP).annotate(text), True)


@nlp.route("/annotate--debug/<text>", methods=['GET'])
def get_annotated_debug_text(text):
    return Api.respond(Annotator(NLP).annotate(text, True), True)
