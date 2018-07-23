#!/usr/bin/env python
#-*-coding:utf-8-*-

# 使用多协程+多进程

import gevent 
from gevent import monkey
monkey.patch_all()
from datetime import datetime 
from gevent.queue import Queue
from multiprocessing import Process,Pool,freeze_support,Array
import signal,os,time


# 失败的例子
# 有些点还没想清楚

q=Queue()

def producer():
    for i in range(10):
        q.put(i)

def workers(i):
    while not q.empty():
        item = q.get()
        print("[Start]the pid is {} 协程 {} deal with {} and time {}".format(os.getpid(),i,item,datetime.now()))
        time.sleep(2)
        print("[Done]the pid is {} 协程 {} deal with {} and time {}".format(os.getpid(),i,item,datetime.now()))

def user_abort(sig, frame):
    exit(-1)

def run():
    #print('this is run ')
    ts = [gevent.spawn(workers,i)for i in range(10)]
    gevent.joinall(ts)

def run_process():
    producer() 
    run()

if __name__ =="__main__":
    freeze_support()
    for i in range(10):
        p = Process(target=run_process)
        p.start()
    p.join()
    
        
