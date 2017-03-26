# -*- coding:utf-8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup

import re

# html = "<b><!--This is --></b><p>This is not</p>"
html = urlopen("http://localhost/~egoist/igoist.github.io/")
ns = BeautifulSoup(html, "html.parser")


# print (ns.find_all("li"))
# print (ns)
# print (ns.a)
# print dir(ns.a)
# print (ns.a.next_siblings)
# print type(ns.head.parent)

# for tag in ns.find_all(re.compile("li")):
#     print tag.name

# print(ns.find_all(string = re.compile("test")))
print(ns(string = re.compile("test")))

# .next_sibling
# .previouse_sibling
#
#

# <>.find_all(name, attrs, recursive, string, **kwargs)
# <>.find_all(..) <=> <>(..)
# soupObj.find_all(..) <=> soupObj(..)

