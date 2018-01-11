# -*- coding: utf-8 -*-
import math
from PIL import Image
from common import debug,config

#检测手机是否通过adb正常连接，正常连接后识别设备，设置相应参数
configs = config.para()
#参数用处明日理解
print(configs["under_game_score_y"])
print(configs["press_coefficient"])
print(configs["piece_base_height_1_2"])
print(configs["piece_body_width"])
print(configs["swipe"])



def yes_or_no(prompt,true_value = 'Y',false_value = 'N',default_value = True):
    """
    启动程序前的提示检查步骤
    """
    #根据默认值设定默认提示信息
    default = true_value if default_value else false_value
    prompt = "{} {}/{} [{}?]:".format(prompt,true_value,false_value,default)
    i = input(prompt)
    if not i:
        return default_value

    while True:
        if i == true_value:
            return True
        elif i == false_value:
            return False
        print("please input {} or {} ".format(true_value,false_value))
        i = input(prompt)

def main():
    op = yes_or_no("请确保手机通过adb连上了电脑,"
                   "进入微信跳一跳,点击【开始游戏】,确定开始？")
    if not op:
        print('bye')
        return

    # #显示设备信息(要补充)
    debug.find_service_inf()
    # #检查设备截图方式
    # screenshot.checkshot()
    #
    # prime = set_for("{},{}/{},[{}]").format(op,"y","n","y?")
    #
    # while True:
    #     #把截图pull到指定位置并命名“auto_jump.png”
    #     screenshot.pull_screenshot()
    #     #到指定位置获取截图，处理图片获取棋子和棋盘的位置
    #     im = Image.open("auto_jump.png")
    #     x1,y1,x2,y2 = find_piece_and_board(im)
    #
    #     #设置点击位置，为让游戏能一直玩下去，将按压位置设置为【开始游戏】处
    #     set_press_position(x1,y1,x2,y2)
    #     #依据棋子、棋盘的位置，按压点的位置及按压时间，棋子做跳动动作
    #     jump(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
    #     #如果需要调试
    #     if DEBUG_SWITH:
    #         screeenshot.save()
    #         screenshot.backup()
    #     im.close()


if __name__ == "__main__":
    main()