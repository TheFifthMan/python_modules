import threading
from time import ctime,sleep
'''
可以看到输出
Listen music :爱情买卖, and the time is Fri Jun 29 15:38:34 2018
Watch movie :绿巨人, and the time is Fri Jun 29 15:38:34 2018

是同一秒启动的，然后总共费时是一秒钟
'''

def music(func):
    for i in range(2):
        print(threading.current_thread().name)
        print("Listen music :{}, and the time is {}".format(func,ctime()))
        sleep(1)
        print('Music done in:{}'.format(ctime()))


def movie(func):
     for i in range(2):
        print(threading.current_thread().name)
        print("Watch movie :{}, and the time is {}".format(func,ctime()))
        sleep(1)
        print("Movie done in:{}".format(ctime()))


if "__main__" == __name__:
    threads = []
    t1 = threading.Thread(target=music,args=("爱情买卖",))
    t2 = threading.Thread(target=movie,args=("绿巨人",))

    threads.append(t1)
    threads.append(t2)

    for t in threads:
        t.setDaemon(False)
        print("the daemon is ",t.daemon)
        t.start()
    

    print("All threads - {} are done in {}".format(threading.current_thread().name, ctime()))
    