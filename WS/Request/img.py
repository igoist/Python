# -*- coding:utf-8 -*-

# 主要内容: 使用 request 获取保存图片
import requests
import os
# import inspect
from time import time

startTime = time()

# ======== Exp1 start ======== 获取并保存单张图片，名字尚未做自动提取或生成，总之还得改

url = "http://imgsize.ph.126.net/?enlarge=true&imgurl=http://edu-image.nosdn.127.net/9AD94813F74DFDE716B49C10A481CEE3.jpg?imageView&amp;thumbnail=426y240&amp;quality=100_230x130x1x95.png"
root = "/Users/Egoist/Documents/Egoist/Python/WS/Request/img/"
fileName = "test.png"

path = root + fileName

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print "target img has been saved"
    else:
        print "file exists"
except:
    print "error !~"



# ======== Exp1 end ========

endTime = time()
print ("last: " + str(endTime - startTime))
