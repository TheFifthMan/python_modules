#-*- cdoing:utf-8 -*-

# 多进程学习
# 创建进程池，启动多进程
# 多进程的例子应该用于一个函数，需要执行多次
# 比如 连续下载一个网页10 次
# 那么就可以使用多进程的方式进行下载

from multiprocessing import Pool
import time
from datetime import datetime 

def movie():
    print("[start] I am watching Movie in {}".format(datetime.now()))
    time.sleep(2)
    print("[end] I am watched Movie in {}".format(datetime.now()))

def music():
    print("[start] I am watching music in {}".format(datetime.now()))
    time.sleep(2)
    print("[end] I am watched music in {}".format(datetime.now()))

if __name__ == "__main__":
    p = Pool(4)
    for i in range(5):
        p.apply_async(music)
        #p.apply_async(movie)

    p.close()
    p.join()

    

