import psycopg2
from psycopg2 import connect
import os

def db_connector():
    return psycopg2.connect(database = os.getenv('DATABASE'),
                            user = os.getenv('DATABASE_USER'),
                            host= os.getenv('DATABASE_HOST'),
                            password = os.getenv('DATABASE_PASSWORD'),
                            port = os.getenv('DATABASE_PORT'))
    # return psycopg2.connect(database = 'okz',
    #                         user = 'okz',
    #                         host= 'localhost',
    #                         password = 'SOULpost',
    #                         port = '5436')