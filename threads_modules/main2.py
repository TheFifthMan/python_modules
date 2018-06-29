import threading
from time import ctime,sleep

# 引入多线程类
# 只能重写两个方法，一个__init__ 一个是run
class MyThread(threading.Thread):

    def run(self):
        for i in range(2):
            print("The thread name is {} and start in {}".format(threading.current_thread().name,ctime()))
            sleep(1)
            print("The thread name is {} and end in {}".format(threading.current_thread().name,ctime()))

if __name__ == "__main__":
    threads = []
    for i in range(2):
        mt = MyThread()
        threads.append(mt)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

'''
The thread name is Thread-1 and start in Fri Jun 29 17:04:41 2018
The thread name is Thread-2 and start in Fri Jun 29 17:04:41 2018
The thread name is Thread-1 and end in Fri Jun 29 17:04:42 2018
The thread name is Thread-1 and start in Fri Jun 29 17:04:42 2018
The thread name is Thread-2 and end in Fri Jun 29 17:04:42 2018
The thread name is Thread-2 and start in Fri Jun 29 17:04:42 2018
The thread name is Thread-1 and end in Fri Jun 29 17:04:43 2018
The thread name is Thread-2 and end in Fri Jun 29 17:04:43 2018
'''
    