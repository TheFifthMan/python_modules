#!/usr/bin/env python
#-*- coding:utf-8 -*-
from time import ctime,sleep
import threading
import queue
from datetime import datetime
q = queue.Queue()

def work(i):
    while not q.empty():
        item = q.get()
        #if item is None:
            #print("线程 {} 发现了一个None， 可以休息了. time:{}".format(i,ctime()))
            #break
        sleep(2) # do some work
        print("线程{}将任务<{}>给完成了。time : {}".format(i,item,ctime()))
        q.task_done()

def producer():
    for i in range(10):
        #sleep(0.5)
        q.put(i)


start = datetime.now()    
producer()
work_threads = [threading.Thread(target=work,args=(i,)) for i in range(10)]


for t in work_threads:
    t.start()

for t in work_threads:
    t.join()
end = datetime.now()

print(end-start)

#0:00:02.008000
