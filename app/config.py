import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fsdfjkhasjkdfh6gddxg34rxcv'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
              'sqlite:///' + os.path.join(basedir, 'app.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TESTING = False

    RECOGNITION = True

    MAX_CONTENT_LENGTH = 50 * 1024 * 1024 


