#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'gozar'
SITENAME = u'Power without the Price'
SITEURL = ''

MARKUP = (('rst', 'md', 'markdown'))

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
THEME = 'theme/pelican-bootstrap3'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

STATIC_PATHS = ['extra/CNAME','images',]
EXTRA_PATH_METADATA = {
                    'extra/CNAME': {'path': 'CNAME'},
                }

DISPLAY_TAGS_ON_SIDEBAR = True

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
        ('RSS','/feeds/all.atom.xml'),
        )
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
