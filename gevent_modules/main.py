#/usr/bin/env python
#-*- coding:utf-8 -*-
import gevent
from gevent import socket
urls = ['www.google.com','www.baidu.com','www.python.org']
jobs = [gevent.spawn(socket.gethostbyname,url) for url in urls]
gevent.joinall(jobs,timeout=2)
t = [job.value for job in jobs]
print(t)