# -*- coding: utf-8 -*-
import os
import json
import sys
import re

def para():
    #根据_get_phone_size()返回的手机尺寸，读取相应尺寸里的json文件，获取手机配置信息
    phone_size = _get_phone_size()
    #sys.path是个列表，前两个元素返回的是所在文件夹的路径！！
    ppath = "{path}/config/{size}/config.json".format(path = sys.path[0],size = phone_size)
    if os.path.exists(ppath):
        with open(ppath,'r') as f:
            return json.load(f)
    else:
        with open("{path}/config/default.json".format(path = sys.path[0]),'r') as f:
            return json.load(f)


def _get_phone_size():
    #获取手机尺寸
    size_inf = os.popen("adb shell wm size").read()
    if not size_inf:
        print("请安装ADB驱动并将路径加入环境变量里")
        sys.exit() #相当于调试
    m = re.search(r"(\d+)x(\d+)",size_inf)
    if m:
        return "{height}x{width}".format(height=m.group(2),width=m.group(1))
    return "1920x1080"
