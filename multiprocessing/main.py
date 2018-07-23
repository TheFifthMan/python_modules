#!/usr/bin/env python
#-*-  coding:utf-8 -*-

from multiprocessing import Process
import os
from datetime import datetime

def run_proc(name):
    print('Child process {0} is running'.format(name,os.getpid()))


if __name__ == "__main__":
    print('parent process {} is running'.format(os.getpid()))
    for i in range(5):
        p = Process(target=run_proc,args=(str(i),))
        print('process start {}'.format(datetime.now()))
        p.start()
    p.join()
    print('close')