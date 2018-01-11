# -*- coding: utf-8 -*-
import os



def find_service_inf():  #！！！要补充
    """
    显示设备信息
    """
    size_str = os.popen("adb shell wm size").read()   #获取设备尺寸
    print("手机尺寸：{size}".format(size = size_str.strip()))