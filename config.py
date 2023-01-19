import os

basedir = os.path.abspath(os.path.dirname(__name__))

class config():
    FLASK_App = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')