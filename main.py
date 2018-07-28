#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 18:01
# @Author  : zhouie
# @File    : main.py
# @Software: PyCharm

import speech
import time
import csv

data = []  # 暂存 *.csv 文件每行数据
Interval_Time = 4  # 两次读词的间隔时间
LOOP_NUM = 8  # 循环基数
Think_Time = 15  # 回顾等待时间

csv_file = open('./res/test.csv', encoding='utf-8')
csv_reader_lines = csv.reader(csv_file)
# print(csv_reader_lines)

num = 0
for one_line in csv_reader_lines:
    data.append(one_line)
    num = num + 1

speech.say("计算机专业相关的英语单词 中英互译 测试小程序，demo版")
speech.say("This is a small routine (compiled by Python) for exercise about English phrases in the field of computer")

i = 0
while i < num:
    # print(i + 1, data[i][0])
    # speech.say(i + 1)
    # speech.say(data[i][0])
    # time.sleep(Interval_Time)
    # speech.say(data[i][0])
    if 0 == (i + 1) % LOOP_NUM:
        speech.say("来回顾一下 以上所学的几个词汇吧")
        speech.say("Just follow me , look back on the words you have learned...")
        print("!--#######--*--#######--!")
        print("第", int(i / LOOP_NUM) + 1, "组词汇：")
        for j in range(i - (LOOP_NUM - 1), i + 1):
            print(data[j][0], data[j][1])
            speech.say(data[j][0])
            speech.say(data[j][1])
        print("!--#######--*--#######--!")
        speech.say("你的正确率如何呢？")
        speech.say("So , What about your correct rate?")
        time.sleep(Think_Time)
    i = i + 1

speech.say("Congratulation!")
