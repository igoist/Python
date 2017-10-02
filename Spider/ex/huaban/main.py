#!/usr/bin/python
# -*- coding: utf-8 -*-

import cookielib
import re
import urllib
import urllib2


filename = 'cookie'
cookie = cookielib.LWPCookieJar(filename)

try:
    cookie.load(ignore_discard=True)
except IOError:
    print dir(IOError)
    print IOError.message
    print('Cookie未加载')

