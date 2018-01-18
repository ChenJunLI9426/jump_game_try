# -*- coding:utf-8 -*-
import subprocess
import os
import sys
from PIL import Image

SCREENSHOT_WAY = 3

#有几种可截图的方式
def pull_screenshot():
    global SCREENSHOT_WAY

    if 1 <= SCREENSHOT_WAY <= 3:
        # 先截图
        process = subprocess.Popen("adb shell screencap -p",
                                   shell=True,stdout=subprocess.PIPE)
        #截图结果以二值化形式输出
        binary_shot = process.stdout.read()
        if SCREENSHOT_WAY == 2:
            binary_shot = binary_shot.replace(b"\r\n",b"\n")
        elif SCREENSHOT_WAY == 1:
            binary_shot = binary_shot.replace(b"\r\r\n", b"\n")
        #新建图片并写入
        f = open("{path}/auto_jump.jpg".format(path=sys.path[0]),'wb')
        # print(os.path.abspath("auto_jump.jpg"))
        f.write(binary_shot)
        f.close()

#查看手机截图的获取方式
def check_screenshot():
    global SCREENSHOT_WAY
   #先把已有截图删除
    if os.path.isfile("{path}/auto_jump.jpg".format(path=sys.path[0])):
        # print('yes auto_jump.jpg')
        try:
            os.remove("{path}/auto_jump.jpg".format(path=sys.path[0]))
        except Exception:
            pass
    if SCREENSHOT_WAY < 0:
        print("暂不支持该设备")
        sys.exit()
    #新截图上传
    pull_screenshot()
    try:
        Image.open("{path}/auto_jump.jpg".format(path=sys.path[0])).load()
        print("采用第{}种方式获取截图".format(SCREENSHOT_WAY))
    except Exception:
        SCREENSHOT_WAY -= 1
        check_screenshot()