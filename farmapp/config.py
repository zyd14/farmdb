import os
DEBUG = True
POSTGRES_URL = '127.0.0.1'
POSTGRES_PORT = '5432'
POSTGRES_USER = 'zach'
POSTGRES_DB = 'farmdb'
POSTGRES_PW = os.getenv('FARMDB_PG_PW')

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = 'localhost'
MAIL_PORT = 20025
MAIL_USE_SSL = False
MAIL_USERNAME = 'romerzs14@gmail.com'

LOG_FOLDER = 'logs'

SECRET_KEY = os.urandom(32)