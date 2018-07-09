#!/usr/bin/env python
#-*- coding:utf-8 -*-
from time import ctime,sleep
import threading
import queue

q = queue.Queue()

def work(i):
    while True:
        item = q.get()
        if item is None:
            print("线程 {} 发现了一个None， 可以休息了. time:{}".format(i,ctime()))
            break
        sleep(0.5) # do some work
        print("线程{}将任务<{}>给完成了。time : {}".format(i,item,ctime()))
        q.task_done()


def producer():
    for i in range(10):
        sleep(0.5)
        q.put(i)
    


producer()


work_threads = []
for i in range(3):
    work_threads.append(threading.Thread(target=work,args=(i,)))

for t in work_threads:
    t.start()

for i in range(10):
    q.put(None)

for t in work_threads:
    t.join()
