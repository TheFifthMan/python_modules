#!/usr/bin/env python
#-*- coding:utf-8 -*-

from multiprocessing import Queue,Pool,Process

# 使用队列进行多进程

def producer(q):
    for i in range(20):
        q.put(i)

def worker(q):
    while not q.empty():
        item = q.get()
        
        print(item)

if __name__ == "__main__":
    # 在这里多进程
    q=Queue()
    producer(q)
    for i in range(10):
        p = Process(target=worker,args=(q,))

        p.start()
    
    p.join()
    print("done")
