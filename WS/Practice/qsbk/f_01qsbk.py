# -*- coding:utf-8 -*-

import urllib as ul
import urllib2 as ul2
import re
import thread
import time

class QSBK:

    def __init__(self):
        self.count = 0
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent': self.user_agent }

        # 每个 Obj 代表 1 页段子
        self.stories = []
        # Flag
        self.enable = False

    # 传入 page index 获得页面
    def getPage(self, pageIndex):
        print u"正在连接第 %d 页" %(pageIndex)
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            # 构建 request
            request = ul2.Request(url, headers = self.headers)
            # 利用 urlopen 获取页面代码
            response = ul2.urlopen(request)
            # 转 utf-8

            pageCode = response.read().decode('utf-8')
            print "...成功"
            return pageCode

        except ul2.URLError, e:
            if hasattr(e, "reason"):
                print u"...失败，错误原因：%s" %(e.reason)
                return None

    # 根据 pageIndex 从对应页面获取段子列表并返回
    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败..."
            return None
        pattern = re.compile('<div.*?author clearfix".*?src="(.*?)".*?<h2>(.*?)</h2>.*?content">.*?<span>(.*?)</span>.*?class="stats.*?class="number">(.*?)</i>', re.S)
        items = re.findall(pattern, pageCode)
        # 用来存储每夜段子
        pageStories = []
        # item[0]: 头像图片链接
        # item[1]: 用户昵称
        # item[2]: 内容
        # item[3]: 点赞量
        for item in items:
            replaceBR = re.compile('<br/>')
            text = re.sub(replaceBR, "\n", item[2])
            pageStories.append([item[1].strip(), text.strip(), item[3].strip()])
        return pageStories

    def loadPage(self):
        # 如果当前未看页数少于2页，则加载新一页
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    def getOneStory(self, pageStories, page):
        for story in pageStories:
            # input = raw_input()
            self.loadPage()
            # if input == "Q":
            #     self.enable = False
            #     return
            # print u"第%d页\t发布人:%s\t赞:%s\n%s" %(page, story[0], story[2], story[1])
            self.count += 1
            file_object.write("第" + str(page) + "页\t" + "发布人: " + story[0].encode('utf-8') + "\t赞: " + story[2].encode('utf-8') + "\t合计第 " + str(self.count) + " 条\n" + story[1].encode('utf-8') + "\n\n")

    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        # 标记为可运行
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                if nowPage == 100:
                    self.enable = False
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)
        print "进程运行完毕。"

# fileName = 'qsbk.txt'
# file_object = open(fileName, 'w+')

spider = QSBK()
# spider.start()

# file_object.close( )

for i in range(100):
    spider.getPage(i)

























