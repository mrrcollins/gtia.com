#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://gtia.com'
SITENAME = 'GozAtari8'
RELATIVE_URLS = False

MARKUP = (('rst', 'md', 'markdown'))

AUTHOR = 'gozar'
DEFAULT_DATE = 'fs'
THEME = 'theme/pelican-bootstrap3'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

AUTHOR_URL = ('author/{slug}/')  
AUTHOR_SAVE_AS = ('author/{slug}/index.html')

CATEGORY_URL = ('category/{slug}/') 
CATEGORY_SAVE_AS = ('category/{slug}/index.html')  
TAG_URL = ('tag/{slug}/') 
TAG_SAVE_AS = ('tag/{slug}/index.html')

PAGE_URL = ('{slug}/')
PAGE_SAVE_AS = ('{slug}/index.html')

#FEED_RSS = 'feed/index.html'
FEED_ALL_RSS = 'feed/index.rss'
CATEGORY_FEED_RSS = 'feed/category/%s.rss'
TAG_FEED_RSS = 'feed/tag/%s.rss'



DELETE_OUTPUT_DIRECTORY = True
STATIC_PATHS = [
            'extra/CNAME',
                ]
EXTRA_PATH_METADATA = {
            'extra/CNAME': {'path': 'CNAME'},
                }

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
