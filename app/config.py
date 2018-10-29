import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'cuongpianna1996@gmail.com'
    MAIL_PASSWORD = '01649886076'
    ADMINS = ['cuongpianna1996@gmail.com']
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'es']
    ELASTICSEARCH_URL = 'http://localhost:9200'
