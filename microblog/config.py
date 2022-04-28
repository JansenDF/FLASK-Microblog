import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['developer.jansen@gmail.com', 'jansen.soares@hotmail.com']
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = "e0d7c60624044bc8b5183ce3714f5cd4" #não funcionou com variavel de ambiente.
    # e0d7c60624044bc8b5183ce3714f5cd4
    POSTS_PER_PAGE = 25

    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')