import os

basedir = os.path.abspath(os.path.dirname(__name__))

class config():
    Flask_App = os.environ.get('Flask_APP')
    Flask_ENV = os.environ.get('development')