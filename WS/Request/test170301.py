# -*- coding:utf-8 -*-

# 主要内容 request 的使用
import requests
import inspect
from time import time

# r = requests.get("https://www.baidu.com")
# print (r.status_code)
# print (r.text)
# print (r.encoding)
# print (r.apparent_encoding)
# print (r.content)

# print (inspect.getsource(requests.put))


def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error Happened"

def getSuccess(url, count):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        return (count + 1)
    except:
        print ("Error Happened")
        return count






# payload = {'k': 'v1', 'k2': 'v2'}
# r = requests.put('http://httpbin.org/put', data = payload)
# print r.text



startTime = time()
count = 0
# while(count < 100):
#     count = getSuccess(url, count)

# url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
# kv = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
# r = requests.get(url, headers = kv)
url = "https://www.baidu.com/s"
# 对于 360 搜索 ( www.so.com/s ) 关键字为 'q'
kv = {'wd': 'Python'}
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
r = requests.get(url, headers = headers, params = kv)


print (r.request.url)

print r.raise_for_status()
print (r.status_code)
print (r.request.headers)
print ("the length of result: " + str(len(r.text)))

endTime = time()

print ("last: " + str(endTime - startTime))


# example url
# - https://item.jd.com/2967929.html
# requests.exceptions.SSLError: hostname '220.181.111.188' doesn't match either of '*.baidu.com', '*.baifubao.com', '*.bdstatic.com', '*.hao123.com', '*.nuomi.com', '*.bce.baidu.com', '*.eyun.baidu.com', '*.map.baidu.com', 'baidu.com', 'baifubao.com', 'www.baidu.cn', 'www.baidu.com.cn', 'click.hm.baidu.com', 'log.hm.baidu.com', 'cm.pos.baidu.com', 'wn.pos.baidu.com', 'update.pan.baidu.com', 'mct.y.nuomi.com'
# - http://220.181.111.188/duty

# 访问用 5 大属性
# - .status_code
# - .text
# - .encoding
# - .apparent_encoding
# - .content
# - .raise_for_status 若不是 200，返回异常


# requests.ConnectionError
#         .HTTPError HTTP 异常
#         .URLRequired URL 缺失
#         .TooManyRedirects
#         .ConnectTimeout 连接远程服务器超时
#         .Timeout 请求 URL 超时


# HTTP 协议对资源的操作
# > * GET    请求获取 URL 位置的资源                             request('get', url, params=params, **kwargs)
# > * HEAD   请求获取 URL 位置资源的响应消息报告，即获得该资源头部信息
# > * POST   请求向 URL 位置的资源后附加新的数据
# > * PUT    请求向 URL 位置存储一个资源，覆盖原 URL 位置的资源
# > * PATCH  请求局部更新 URL 位置的资源，即改变该处资源的部分内容     request('put', url, data=None, **kwargs)
# > * DELETE 请求删除 URL 位置存储的资源

# PATCH vs PUT
# 采用PATCH，仅向 URL 提交 UserName 的局部更新请求
# 采用PUT，必须将 20个 字段一并提交到 URL，未提交字段被删除
# 故 PATCH 最主要好处: 节省网络带宽


# requests.request(method, url, **kwargs)
# method 跟 url 不用多说
# - requests.request('get'...)
# - ...
# - requests.request('options'...)
# **kwargs 共 13 个参数
# > *
# > * params  字典或字节序列，作为参数增加到 url 中 kv = {'k1': 'v1', 'k2': 'v2'}
# > * data    字典、字节序列或文件对象，作为 Request 的内容
# > * json    JSON 格式的数据，作为 Request 的内容
# > * headers 字典，HTTP 定制头
# > * cookies 字典或 CookieJar，Request 中的 cookie
# > * auth    元组，支持 HTTP 认证功能
# > * files   字典类型，传输文件 files = {'file': open("...", 'rb'), 'file2': ..., ...}
# > * timeout 设定超时 单位 s (秒)
# > * proxies 字典类型，设定访问代理服务器，可以增加登陆认证，反追踪
# 以下 4 个属于高级功能
# > * allow_redirects True/False，默认 True，重定向开关
# > * stream  True/False，默认 True，获取内容立即下载开关
# > * verify  True/False，默认 True，认证 SSL 证书开关
# > * cert    本地 SSL 证书路径



