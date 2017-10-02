#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import requests
import re

folder = './imgs/'

print os.getcwd()


class Page(object):
    def __init__(self, url):
        self._url = url

    def __str__(self):
        return '[URL]: %s' %(self._url)

    __repr__ = __str__

    @property
    def url(self):
        return self._url

    def url(self, value):
        if not isinstance(value, str):
            raise ValueError('url must be a string!')
        if value == '':
            raise ValueError('url must be not empty')
        self._url = value


# page = Page('https://sylvanassun.github.io/')
# print page

def download():
    r = requests.get(url = 'http://huaban.com/favorite/')
    page = r.content
    # print page
    prog = re.compile(r'app\.page\["pins"\].*')
    # print prog
    appPins = prog.findall(page)
    # print appPins
    true = True
    null = None
    result = eval(appPins[0][19:-1])
    # print result
    images = []
    for i in result:
        info = {}
        info['id'] = str(i['pin_id'])
        info['url'] = "http://img.hb.aicdn.com/" + i["file"]["key"] + "_fw658"
        info['type'] = i["file"]["type"][6:]
        images.append(info)
    # print images
    for image in images:
        req = requests.get(image["url"])
        imageName = "./imgs/" + image["id"] + "." + image["type"]
        print('downloading: ' + imageName)
        with open(imageName, 'wb') as fp:
                fp.write(req.content)


def clean():
    for f in os.listdir(folder):
        file_path = os.path.join(folder, f)
        try:
            if os.path.isfile(file_path):
                print('removing ' + file_path)
                os.unlink(file_path)
        except Exception as e:
            print(e)

download()
