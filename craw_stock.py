#!/usr/bin/env python
# coding=utf-8

import sys 
import re
import urllib2
from tabulate import tabulate
from qqbot import qqbotsched
import time
import os

flag = 0
price_target = 14.0

@qqbotsched(hour='9-15/1', minute='0-59/1', second='0-59/10')
def mytask(bot):
    global flag
    global price_target
    price = craw()
    if float(price) >= price_target and flag == 0:
        gl = bot.List('group', '测试群')
        if gl is not None:
            for group in gl:
                bot.SendTo(group, "你设置的股票已经到达预警价位")

def craw():
    url = "http://hq.sinajs.cn/list=sh600000"
    response = urllib2.urlopen(url)
    html = response.read()

    return html.split(',')[3]

def onQQMessage(bot, contact, member, content):
    global flag
    b = bot.List('group', '测试群')
    if content == '关闭':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()

if __name__ == "__main__":
    print("股票600000(浦发银行）现在的价位是："+craw())
