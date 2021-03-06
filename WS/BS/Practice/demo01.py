# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "get fail"

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            # print(te)
            ulist.append([tds[0].string.encode('utf-8').strip(), tds[1].string.encode('utf-8').strip(), tds[2].string.encode('utf-8').strip(), tds[3].string.encode('utf-8').strip()])
    pass

def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^30}\t{2:^20}\t{3:^10}"
    print ("{0:^10}\t{1:^30}\t{2:^20}\t{3:^10}".format("排名", "学校", "地区", "分数"))
    # print ("Suc" + str(num))
    for i in range(num):
        u = ulist[i]
        print ("{0:^10}\t{1:^30}\t{2:^20}\t{3:^10}".format(u[0], u[1], u[2], u[3]))


# invoke
def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    # print(html)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 20

main()