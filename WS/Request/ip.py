# -*- coding:utf-8 -*-

# 主要内容: 使用 request 查 ip 相关
import requests
#import inspect
from time import time

startTime = time()

# ======== Exp1 start ======== 调用人家 api 而已

# headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url + '192.168.2.15')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print (r.text[-500:])
except:
    print ("error ~!")

# ======== Exp1 end ========

endTime = time()
print ("last: " + str(endTime - startTime))
