from .base import search, parse, login, logout, front_page, rss
from .utils import LOGGER, BASE_URL, soup, request, get_page, Object
from .enums import *
from .pages import *
from .client import Client

import requests
SESSION = requests.Session()

__version__ = "0.7"

#TODO:
#add @staticmethod, @classmethod, ect...
#double check that ResultList for get_blogs and get_reviews works, I have the sneaking suspicion they don't
