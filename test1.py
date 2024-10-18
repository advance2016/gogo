# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import os
import time
from ctypes import *
import sys
import json
import pyautogui


dd_dll = windll.LoadLibrary('C:/text/key.dll')

# DD虚拟码，可以用DD内置函数转换。
vk = {'5': 205, 'c': 503, 'n': 506, 'z': 501, '3': 203, '1': 201, 'd': 403, '0': 210, 'l': 409, '8': 208, 'w': 302,
        'u': 307, '4': 204, 'e': 303, '[': 311, 'f': 404, 'y': 306, 'x': 502, 'g': 405, 'v': 504, 'r': 304, 'i': 308,
        'a': 401, 'm': 507, 'h': 406, '.': 509, ',': 508, ']': 312, '/': 510, '6': 206, '2': 202, 'b': 505, 'k': 408,
        '7': 207, 'q': 301, "'": 411, '\\': 313, 'j': 407, '`': 200, '9': 209, 'p': 310, 'o': 309, 't': 305, '-': 211,
        '=': 212, 's': 402, ';': 410}
# 需要组合shift的按键。
vk2 = {'"': "'", '#': '3', ')': '0', '^': '6', '?': '/', '>': '.', '<': ',', '+': '=', '*': '8', '&': '7', '{': '[', '_': '-',
        '|': '\\', '~': '`', ':': ';', '$': '4', '}': ']', '%': '5', '@': '2', '!': '1', '(': '9'}

def down_up(code):
    # 进行一组按键。

    dd_dll.DD_key(vk[code], 1)
    dd_dll.DD_key(vk[code], 2)


def dd(key):
    # 500是shift键码。
    if key.isupper():
        # 如果是一个大写的玩意。

        # 按下抬起。
        dd_dll.DD_key(500, 1)
        down_up(key.lower())
        dd_dll.DD_key(500, 2)

    elif key in '~!@#$%^&*()_+{}|:"<>?':
        # 如果是需要这样按键的玩意。
        dd_dll.DD_key(500, 1)
        down_up(vk2[key])
        dd_dll.DD_key(500, 2)
    else:
        down_up(key)


def start():
    #dd_dll = windll.LoadLibrary('C:/text/key.dll')
    st = dd_dll.DD_btn(0)  # DD Initialize
    if st != 1:
        print("Error")
        return False
    print("begin")
    for i in range(30):
        # w
        dd_dll.DD_key(709, 1)
        dd_dll.DD_key(709, 2)
        time.sleep(0.1)
        # s
        dd_dll.DD_key(709, 1)
        dd_dll.DD_key(709, 2)
        time.sleep(0.1)
        time.sleep(1)


def start1():
    while True:
        # 模拟按键按下
        pyautogui.keyDown('w')

        # 模拟按键释放
        pyautogui.keyUp('w')


        time.sleep(0.2)

def start2():
    #dd_dll = windll.LoadLibrary('C:/text/key.dll')
    st = dd_dll.DD_btn(0)  # DD Initialize
    if st != 1:
        print("Error")
        return False

    while True:
        # 模拟按键按下
        #pyautogui.keyDown('w')

        # 模拟按键释放
        #pyautogui.keyUp('w')

        dd_dll.DD_key(302, 1)
        dd_dll.DD_key(302, 2)

        time.sleep(1)

if __name__ == "__main__":
    start1()
