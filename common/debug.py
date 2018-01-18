# -*- coding: utf-8 -*-
import os
import sys


def find_service_inf():
    """
    显示设备信息,os.open()是指另开一个进程运行cmd，并且保留运行结果备用
    """
    size_str = os.popen("adb shell wm size").read()   #获取设备尺寸
    #adb shell getprop  获取安卓手机属性
    device_str = os.popen("adb shell getprop ro.product.device").read()#查看安卓手机设备参数
    phone_os_str = os.popen("adb shell getprop ro.build.version.release").read()  #查看手机系统版本
    density_str = os.popen("adb shell wm density").read() #获取手机分辨率

    print("""手机相关信息，
    phone_size：{size}，
    device：{device},
    phone_os:{phone_os},
    host_os:{host_os}
    density:{density},
    python:{python}
    """
          .format(size = size_str.strip(),
                  device = device_str.strip(),
                  phone_os = phone_os_str.strip(),
                  density = density_str.strip(),
                  python = sys.version.strip(),
                  host_os = sys.platform.strip()
                  ))