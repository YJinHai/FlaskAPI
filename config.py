# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

__author__ = '杨金海'

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    URL_PREFIX = '/api'
    SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://@localhost:6379/1'
    3