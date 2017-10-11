#!/usr/bin/python
# -*- coding: utf-8 -*-

# import http
import cookielib
import urllib
import urllib2
import requests, os, time, re
from bs4 import BeautifulSoup
import requests

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 当前项目路径
cur_path = os.getcwd() + '/'

class ZhiHuSpider(object):
    def __init__(self):
        self.session = requests.session()
        self.session.cookies = cookielib.LWPCookieJar(filename='cookies')
        self.url_s = 'https://www.zhihu.com/question/28139333'
        self.url_signin = 'https://www.zhihu.com/#signin'
        self.url_login = 'https://www.zhihu.com/login/phone_num'
        self.url_captcha = 'https://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
        self.num = 1
        try:
            self.session.cookies.load(ignore_discard=True)
            print("Cookie 加载成功")
        except:
            print("Cookie 未能加载")

    def get_captcha(self):
        if not os.path.exists(cur_path + 'captcha'):
            os.mkdir(cur_path + 'captcha')

        # 下载验证码图片
        captcha = self.session.get(self.url_captcha, headers=self.headers).content
        captcha_path = cur_path + 'captcha/captcha.gif' # 验证码图片路径
        captcha_path_new = cur_path + 'captcha/captcha_new.gif' # 处理后的验证码图片路径
        with open(captcha_path, 'wb') as f:
            f.write(captcha)
        return raw_input('capture:')

    def login(self, username, password):
        soup = BeautifulSoup(self.session.get(self.url_signin, headers=self.headers).content, 'html.parser')

        # session = requests.session()
        # index_page = session.get(self.url_signin, headers=self.headers)
        # html = index_page.text
        # soup = BeautifulSoup(html, 'html.parser')

        xsrf = soup.find('input', attrs={'name': '_xsrf'}).get('value')

        # regex = re.compile(r'name="_xsrf" value="(.*)"')
        # xsrf2 = re.search(regex, html)
        # print xsrf2.group(1)

        post_data = {
            '_xsrf': xsrf,
            'phone_num': username,
            'password': password,
            'captcha': self.get_captcha()
        }

        login_ret = self.session.post(self.url_login, post_data, headers=self.headers).json()

        if login_ret['r'] == 0:
            print('登陆成功! ')
            self.session.cookies.save()
            print('已保存 session')

    def isLogin(self):
        # 通过查看用户个人信息来判断是否已经登录
        url = "https://www.zhihu.com/settings/profile"
        login_code = self.session.get(url, headers=self.headers, allow_redirects=False).status_code
        if login_code == 200:
            print('您已经登录')
            return True
        else:
            print('您尚未登录')
            return False

    def get_index_topic(self):
        '''
        获取首页第一条话题记录
        '''
        # print('-'*50, '获取知乎首页第一条话题记录', '-'*50, sep="\n")
        soup = BeautifulSoup(self.session.get(self.url_signin, headers=self.headers).content, 'html.parser')

        items = soup.find_all('div', attrs={'class': 'Card TopstoryItem TopstoryItem--experimentExpand TopstoryItem--experimentButton'})
        for item in items:
            if item.find('div', attrs={'class': 'Feed-title'}).find('div', attrs={'class': 'Popover'}).find('div').find('a') != None:
                popover = item.find('div', attrs={'class': 'Feed-title'}).find('div', attrs={'class': 'Popover'}).find('div').find('a').get_text() # 某关注的人
                print('来自某人：%s' % popover)
            else:
                popover = item.find('div', attrs={'class': 'Feed-title'}).find('div', attrs={'class': 'Popover'}).find('div').get_text() # 话题
                print('来自话题：%s' % popover)
            if item.find('div', attrs={'class': 'ContentItem AnswerItem'}) != None:
                title = item.find('div', attrs={'class': 'ContentItem AnswerItem'}).find('meta', attrs={'itemprop': 'name'}).get('content') # 标题
                print('title: %s' % title)
                content = item.find('div', attrs={'class': 'ContentItem AnswerItem'}).find('span', attrs={'class': 'RichText CopyrightRichText-richText'}).get_text() # 内容
                print('content: %s' % content)
            else:
                title = item.find('div', attrs={'class': 'ContentItem ArticleItem'}).find('meta', attrs={'itemprop': 'name'}).get('content') # 标题
                print('title: %s' % title)
                content = item.find('div', attrs={'class': 'ContentItem ArticleItem'}).find('span', attrs={'class': 'RichText CopyrightRichText-richText'}).get_text() # 内容
                print('content: %s' % content)

    def get_search(self):
        keywords = raw_input('请输入问题关键字: ')
        keywordList = keywords.split(' ')
        url = 'https://www.zhihu.com/search?type=content&q=' + '+'.join(keywordList)
        soup = BeautifulSoup(self.session.get(url, headers=self.headers).content, 'html.parser')

        items = soup.find_all('li', attrs={'class': 'item clearfix'})
        print('问题：')
        for item in items:
            title = item.find('div', attrs={'class': 'title'}).find('a').get_text()
            print(title)
        print('文章：')
        items = soup.find_all('li', attrs={'class': 'item clearfix article-item'})
        for item in items:
            title = item.find('div', attrs={'class': 'title'}).find('a').get_text()
            print(title)
        print('专栏：')
        items = soup.find_all('li', attrs={'class': 'item clearfix column-item'})
        for item in items:
            title = item.find('div', attrs={'class': 'title'}).find('a').get_text()
            print(title)


if  __name__ == '__main__':
    zhihu = ZhiHuSpider()
    if zhihu.isLogin():
        # zhihu.get_index_topic()
        zhihu.get_search()
    else:
        ret = zhihu.login('', '')
