# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import os
import time
from ctypes import *
import sys
import json
import pyautogui
from logger import get_logger


class guai(object):
    def __init__(self):
        self.dd_dll = windll.LoadLibrary('C:/text/key.dll')
        st = self.dd_dll.DD_btn(0)  # DD Initialize
        if st != 1:
            print("Error")

        self.attack_cnt = 0
        self.Fighting = False
        self.fight_time = 0
        self.clear_fight_time = 0
        self.keys = {"f4": 104, "f5": 105, "f6": 106, "f7": 107, "f8": 108, "f9": 109, "f10": 110
            , "1": 201, "2": 202, "3": 203, "4": 204, "5": 205, "6": 206, "7": 207, "8": 208
            , "9": 209, "0": 210, "-": 211, "=": 212}

        self.logger = get_logger("yaya.log")
        # self.logger.info(response.text)

    def start1(self):
        dd_dll = windll.LoadLibrary('C:/text/key.dll')
        st = dd_dll.DD_btn(0)  # DD Initialize
        if st != 1:
            print("Error")
            return False

    def isFightOver(self):
        return self.Fighting

    def hasTargetEnemy(self, x=430, y=79):
        print(pyautogui.pixel(x, y))
        return pyautogui.pixelMatchesColor(x, y, (204, 0, 0))

    # 检查攻击距离
    def checkAttackDistance(self, x=446, y=1011):
        print("检查攻击距离", pyautogui.pixel(x, y))
        return pyautogui.pixelMatchesColor(x, y, (236, 71, 24))

    def isFighting(self, x=142, y=67):
        return pyautogui.pixelMatchesColor(x, y, (218, 0, 0))

    def attack(self):
        self.logger.info("攻击目标")
        # 按一下交互键f8，防止朝向错误
        # if not self.isFighting():
        self.attack_cnt = self.attack_cnt + 1
        if self.attack_cnt % 5 == 0:
            self.press(108)

        # 判断是否要加血
        self.need_blood()

        # 攻击f7
        self.press(107)

    def no_blood(self):
        """
        if pyautogui.pixelMatchesColor(105, 94, (178, 84, 0)):
            return True

        if pyautogui.pixelMatchesColor(102, 93, (226, 38, 0)):
            return True

        if pyautogui.pixelMatchesColor(105, 93, (209, 63, 0)):
            return True

        if pyautogui.pixelMatchesColor(105, 93, (162, 182, 0)):
            return True

        return False
        """

        rgb_color = pyautogui.pixel(100, 94)
        # self.logger.info("血条数值：{}".format(rgb_color))
        if rgb_color[0] >= 128 and rgb_color[1] <= 168:
            return True

        return False

    def need_blood(self):

        if self.no_blood():
            self.logger.info("开始加血")
            self.press(209)
            time.sleep(0.1)			
            self.press(205)
            time.sleep(0.2)
            self.press(211)
            time.sleep(0.2)
            self.press(212)
            # f4
            self.press(104)
            time.sleep(0.1)
            # self.press(104)
            # 7
            self.press(207)

    def moveToTarget(self):
        print("走向目标, 按互动键f8")
        self.press(108)

    def clearTarget(self):
        self.logger.info("清理目标")

        self.clear_fight_time = time.time()

        self.press(109)

        # print("搜索敌人，按f6")
        self.press(106)

        # print("走向目标, 按互动键f8")
        self.press(108)

    def press(self, key):
        self.dd_dll.DD_key(key, 1)
        self.dd_dll.DD_key(key, 2)

    def searchTarget(self):
        # self.pickupTreasure()

        # 先转换视角，a字符
        self.dd_dll.DD_key(401, 1)
        time.sleep(0.2)
        self.dd_dll.DD_key(401, 2)

        self.logger.info("搜索敌人，按f6")
        self.press(106)

        # print("走向目标, 按互动键f8")
        self.press(108)
        time.sleep(0.2)
        self.press(110)

        if self.hasTargetEnemy():
            self.Fighting = True
            self.fight_time = time.time()
            self.clear_fight_time = time.time()
            self.logger.info("开始战斗")

    def pickupTreasure(self):
        self.logger.info("拾取宝物, 按互动键f8")
        time.sleep(0.2)
        self.press(108)
        time.sleep(0.2)
        self.press(110)

    def start(self):
        while True:
            if self.hasTargetEnemy():
                if time.time() - self.clear_fight_time >= 10:
                    self.clearTarget()

                if not self.checkAttackDistance():
                    self.attack()
                else:
                    self.moveToTarget()
            else:
                if self.isFightOver():
                    self.Fighting = False
                    self.logger.info("战斗结束")
                    self.pickupTreasure()
                else:
                    # print("没有发现敌人")
                    self.searchTarget()

            time.sleep(0.5)


if __name__ == "__main__":
    api = guai()
    api.start()
