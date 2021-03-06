from flask import Flask
from flask_cors import CORS
from controllers.nlp_api import nlp

# initialize the flask app
app = Flask(__name__)
CORS(app)

# register the blueprints from controllers
app.register_blueprint(nlp)

# main function
if __name__ == "__main__":
    app.run()
