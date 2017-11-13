#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHORS = 'John Bachman, Carlos Lopez, Alex Lubbock, Jeremy Muhlich'
SITENAME = 'PySB'
SITESUBTITLE = 'Systems biology modeling in Python'
SITEURL = ''
SITELOGO = '/images/pysb-swirl.png'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = 'themes/pelican-blueidea'

STATIC_PATHS = ['images', 'extra/']
EXTRA_PATH_METADATA = {}
for f in os.listdir('content/extra/'):
    EXTRA_PATH_METADATA['extra/'+f] = {'path':f}

MENUITEMS=[('Home', '/'),
           ('Download', '/download'),
           ('News', '/news'),
           ('Tutorials', '/tutorials'),
           ('Support', '/support')]
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

MARKUP = ('md', 'ipynb')
PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
