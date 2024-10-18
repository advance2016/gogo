# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import os
import time
from ctypes import *
import sys
import json


def start():
    dd_dll = windll.LoadLibrary('C:/text/key.dll')
    st = dd_dll.DD_btn(0)  # DD Initialize
    if st != 1:
        print("Error")
        return False

    config_file='data.json'
    if len(sys.argv) == 2:
        config_file=sys.argv[1]
		
    # 从文件加载JSON数据
    with open(config_file, 'r') as file:
        config = json.load(file)

    STR_LAST = 'last_time'
    STR_KEY = 'key'
    STR_DIFF = 'diff'

    for item in config['data']:
        item[STR_LAST] = time.time()

    while True:
        for item in config['data']:
            curr = time.time()
            if curr - item[STR_LAST] >= item[STR_DIFF]:
                item[STR_LAST] = curr

                dd_dll.DD_key(item[STR_KEY], 1)
                dd_dll.DD_key(item[STR_KEY], 2)

                time.sleep(0.1)
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " press key: " + str(item[STR_KEY]))

            time.sleep(1)

if __name__ == "__main__":
    start()
