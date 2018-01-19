# AI Domain Expert
![alt text](https://travis-ci.org/AITestingOrg/aide--spacy-nlp-service.svg?branch=master "Build Status")

# Setup
## Requirements
* Python 3.x

## NLP Setup
### Install NLTK
* `pip install -U nltk`
* `python`
* ```python
    import nltk
    nltk.download()
  ```
* Choose whichever Corpora.

### Install SpaCy
* `pip install -U spacy`
* Then install the English language.
* `python -m spacy download en`
* On Windows ensure you have Visual Studio C++ Build Tools 2015 installed from http://landinghub.visualstudio.com/visual-cpp-build-tools

### Install Neo4j
* Download and install from https://neo4j.com/download/?ref=hro
* Start the service

## Setup Flask
* `pip install -U flask`
### Setup the path to the app
* UNIX `export FLASK_APP=src/app.py`
* WINDOWS `set FLASK_APP=src/app.py`

## Run the backend
* `Flask run`

## Pre-seed DB
* Add the lines below to the app.py file
```python
for sent in brown.sents():
    NLP().find_useful_stuff(re.sub(r'[^\w]', ' ', ' '.join(sent)))
```

## Run Tests
```bash
cd src/
python -m pytest tests/
```
