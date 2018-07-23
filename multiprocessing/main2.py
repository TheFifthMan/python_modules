#!/usr/bin/env python
#-*-coding:utf-8-*-
# Pool 指定数量的进程，默认是CPU数量，如果池子没有满，就创建一个新进程，否则就等待
# apply_async 允许多个进程进入池子进行执行
# apply 只允许一个进程

from multiprocessing import Process,Pool
import os 
from datetime import datetime 
import time
import signal

def run_proc(i):
    #time.sleep(10)
    print('[process {}]I am child process {} and the start time is {}'.format(i,os.getpid(),datetime.now()))
    time.sleep(10)
    print('task done')

if __name__ == "__main__":
    p = Pool(processes=os.cpu_count())
    try:
        for i in range(10):
            p.apply_async(run_proc,args=(str(i),))
        p.close()
        p.join()
        
        print('all done')
    except Exception as e:
        p.terminate()
