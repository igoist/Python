#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib
import urllib2
from bs4 import BeautifulSoup

# page = 30
# url = 'http://www.qiushibaike.com/hot/page/' + str(page)

# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = { 'User-Agent' : user_agent }

# def read(res):
#     content = res.read().decode('utf-8')
#     pattern = re.compile('<div.*?author clearfix".*?src="(.*?)".*?<h2>(.*?)</h2>.*?content">.*?<span>(.*?)</span>.*?class="stats.*?class="number">(.*?)</i>', re.S)
#     items = re.findall(pattern, content)
#     # print items
#     for item in items:
#         print item[0], item[1], item[2], item[3]
#     # soup = BeautifulSoup(content, 'html.parser')
#     # items = soup.find_all('div', attrs={'class': 'author clearfix'})
#     # for item in items:
#     #     user = item.find


# try:
#     req = urllib2.Request(url, headers = headers)
#     res = urllib2.urlopen(req)
#     # print res.read(res)
#     read(res)
# except urllib2.URLError, e:
#     if hasattr(e, 'code'):
#         print e.code
#     if hasattr(e, 'reason'):
#         print e.reason


class QSBK:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            req = urllib2.Request(url, headers=self.headers)
            res = urllib2.urlopen(req)
            html = res.read().decode('utf-8')
            return html
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print u'', e.reason
                return None

    def getPageItems(self, pageIndex):
        html = self.getPage(pageIndex)
        if not html:
            print '页面加载失败...'
            return None
        pattern = re.compile('<div.*?author clearfix".*?src="(.*?)".*?<h2>(.*?)</h2>.*?content">.*?<span>(.*?)</span>.*?class="stats.*?class="number">(.*?)</i>', re.S)
        items = re.findall(pattern, html)
        return items

    # def handleItems(self, items):

    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1



    def getStoryOneByOne(self, pageStories, page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == 'Q':
                self.enable = False
                return
            print u"第%d页\t发布人:%s\t发布时间:%s\t赞:%s\n%s" %(page, story[0], story[2], story[3], story[1])



    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getStoryOneByOne(pageStories, nowPage)


spider = QSBK()
spider.start()




