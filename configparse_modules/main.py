#!/usr/bin/env python 
#-*- coding:utf-8 -*-

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

sections = config.sections()
print(sections)  # head body

head = config['head']
print(head)

title = head['title']
print(title)

body = config['body']
print(body)  

for k,v in body.items():
    print(k,v)
