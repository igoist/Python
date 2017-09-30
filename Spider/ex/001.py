#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import cookielib

# 设置代理
# enable_proxy = True
# proxy_handler = urllib2.ProxyHandler({"http" : 'http://www.baidu.com:8080'})
# null_proxy_handler = urllib2.ProxyHandler({})

# if enable_proxy:
#     opener = urllib2.build_opener(proxy_handler)
# else:
#     opener = urllib2.build_opener(null_proxy_handler)

# urllib2.install_opener(opener)

# 设置 debug
# httpHandler = urllib2.HTTPHandler(debuglevel=1)
# httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
# opener = urllib2.build_opener(httpHandler, httpsHandler)
# urllib2.install_opener(opener)

url = 'http://www.baidu.com/s?wd=临安天气'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
headers = {'User-Agent': user_agent}
# values = {}
# data = urllib.urlencode(values)

req = urllib2.Request(url, headers = headers)
res = urllib2.urlopen(req)

# page = res.read()

# print page


req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    res = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print "OK"

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
res = opener.open('http://www.baidu.com')

for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value

# filename = 'cookie.txt'
# cookie = cookielib.MozillaCookieJar(filename)
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# res = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# cookie = cookielib.MozillaCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# req = urllib2.Request('http://www.baidu.com')
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# res = opener.open(req)
# print res.read()

import requests

r = requests.get('http://huaban.com')
print type(r)
print r.status_code
print r.encoding
#print r.text
print r.cookies

