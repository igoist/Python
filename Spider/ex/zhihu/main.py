#!/usr/bin/python
# -*- coding: utf-8 -*-

# import http
import cookielib
import re
import urllib
import urllib2

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests, os, time, re
from bs4 import BeautifulSoup
# from PIL import Image

# 当前项目路径
cur_path = os.getcwd() + '/'

class ZhiHuSpider(object):
    '''
    本类主要用于实现模拟知乎登陆并使用tesseract-ocr识别验证码

    Attribute:
        session: 建立会话
        url_signin: 登陆页面链接
        url_login: 登陆接口
        url_captcha: 验证码链接
        headers： 请求头部信息
        num: 识别验证码次数
    '''

    def __init__(self):
        self.session = requests.Session();
        self.url_s = 'https://www.zhihu.com/question/28139333'
        self.url_signin = 'https://www.zhihu.com/#signin'
        self.url_login = 'https://www.zhihu.com/login/phone_num'
        self.url_captcha = 'https://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
        self.num = 1

    def get_captcha(self):
        # raw_input('capture:')
        if not os.path.exists(cur_path + 'captcha'):
            os.mkdir(cur_path + 'captcha')
        captcha_text = ''
        # while True:
        # 下载验证码图片
        captcha = self.session.get(self.url_captcha, headers=self.headers).content
        captcha_path = cur_path + 'captcha/captcha.gif' # 验证码图片路径
        captcha_path_new = cur_path + 'captcha/captcha_new.gif' # 处理后的验证码图片路径
        with open(captcha_path, 'wb') as f:
            f.write(captcha)
        return raw_input('capture:')

    def login(self, username, password):
        '''
        登陆接口

        Args:
            username: 登陆账户
            password: 登陆密码
        Returns:
            返回登录结果list
        '''
        soup = BeautifulSoup(self.session.get(self.url_signin, headers=self.headers).content, 'html.parser')

        # 获取xsrf_token
        xsrf = soup.find('input', attrs={'name': '_xsrf'}).get('value')

        post_data = {
            '_xsrf': xsrf,
            'phone_num': username,
            'password': password,
            'captcha': self.get_captcha()
            # 'captcha_type': 'cn'
        }
        login_ret = self.session.post(self.url_login, post_data, headers=self.headers).json()
        print login_ret
        return login_ret

    def get_index_topic(self):
        '''
        获取首页第一条话题记录
        '''
        # print('-'*50, '获取知乎首页第一条话题记录', '-'*50, sep="\n")
        soup = BeautifulSoup(self.session.get(self.url_signin, headers=self.headers).content, 'html.parser')
        item = soup.find('div', attrs={'class': 'Card TopstoryItem TopstoryItem--experimentExpand TopstoryItem--experimentButton'})
        popover = item.find('div', attrs={'class': 'Feed-title'}).find('div', attrs={'class': 'Popover'}).find('div').find('a').get_text() # 话题
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

    def get_imgs(self):
        soup = BeautifulSoup(self.session.get(self.url_s, headers=self.headers).content, 'html.parser')
        main = soup.find('div', attrs={'class': 'Question-mainColumn'})
        items = main.find_all('img')
        for idx, i in enumerate(items):
            print 'downloading: ' + i.get('src')
            img = urllib.urlopen(i.get('src'))
            data = img.read()
            img_name = ''# = i.get('alt') ? i.get('alt') : str(idx)
            if i.get('alt'):
                img_name = i.get('alt')
            else:
                img_name = str(idx)
            with open('./imgs/' + img_name + '.jpg', 'wb') as f:
                f.write(data)
                f.close()

if  __name__ == '__main__':
    zhihu = ZhiHuSpider()
    # 循环尝试登陆
    # while True:
    ret = zhihu.login('18806529366', 'qq111111')
    if ret['r'] == 0:
        print('登陆成功! ')
        # zhihu.get_index_topic()
        zhihu.get_imgs()
        # break
    else:
        print('登陆失败: %s' % ret['msg'])
