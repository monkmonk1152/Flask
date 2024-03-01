import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config():
    '''
    Set config variables for the flask app
    using Environment variables were avaiable.
    Otherwise, create the config varialbe if not already done
    '''

    FLASKAPP_APP = os.getenv('FLASK_APP')
    FLASKAPP_APP = os.getenv('FLASK_ENV')
    SECERT_KEY = os.environ.get('SECERT_KEY') or 'I am monkmonk'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False