# 概述
众所周知，运行一个程序最重要的是它的执行效率，比如爬虫，要如何节省爬虫的时间，提高爬虫效率是一件很重要的事情。
虽然python的多线程是鸡肋，在任意时间内，只有一个python的解释器在解释python的bytecode。但也不是多线程就是没有用的，我们的代码分为两种，一种是计算密集型，一种是IO密集型，其中计算密集型主要是需要CPU进行大量的计算的，这个时候，python的多线程没什么用，反而可能会比单线程的效率差。而相对于IO密集型的代码，主要瓶颈在于网络的传输，硬盘IO之类的上面，这个时候，使用python多线程就可以提高其效率。
上面的理解可能稍显有些片面，但不管如何，偏底层的东西先做一个了解，先学会一下如何用python写多线程

# threading.Thread
以一段代码为例，做一下学习
```python
import threading
from time import ctime,sleep

def thread1():
    for i in range(2):
        print("The thread name is {} and start in {}".format(threading.current_thread().name,ctime()))
        sleep(1)
        print("The thread name is {} and end in {}".format(threading.current_thread().name,ctime()))

def thread2():
    for i in range(2):
        print("The thread name is {} and start in {}".format(threading.current_thread().name,ctime()))
        sleep(1)
        print("The thread name is {} and end in {}".format(threading.current_thread().name,ctime()))


if "__main__" == __name__:
    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)

    threads = []
    threads.append(t1)
    threads.append(t2)

    for t in threads:
        print(t.daemon)
        t.start()
    
    print("The thread name is {} and end in {}".format(threading.current_thread().name,ctime()))
# result： 最后一个线程退出，用时两秒。
'''
False
The thread name is Thread-1 and start in Fri Jun 29 16:34:43 2018
False
The thread name is Thread-2 and start in Fri Jun 29 16:34:43 2018
The thread name is MainThread and end in Fri Jun 29 16:34:43 2018
The thread name is Thread-2 and end in Fri Jun 29 16:34:44 2018
The thread name is Thread-1 and end in Fri Jun 29 16:34:44 2018
The thread name is Thread-2 and start in Fri Jun 29 16:34:44 2018
The thread name is Thread-1 and start in Fri Jun 29 16:34:44 2018
The thread name is Thread-2 and end in Fri Jun 29 16:34:45 2018
The thread name is Thread-1 and end in Fri Jun 29 16:34:45 2018
'''
```

## daemon属性
如果你设置一个线程的daemon属性为True的话，说明这个线程是不重要的，整个python的程序无需等待这个线程即可结束。
（注意，很多地方说是主线程结束，但是我实验了一下，主线程已经执行完了，但是其子线程还是会继续执行下去的。）
从代码可见，其daemon属性，从一开始就是False的。
但是如果你将daemon设置为True，那么程序将不会等待，主线程结束，程序就会退出，我们可以试着将代码改为
```python

t1 = threading.Thread(target=thread1,daemon=True)
t2 = threading.Thread(target=thread2,daemon=True)

threads = []
threads.append(t1)
threads.append(t2)

for t in threads:
    print(t.daemon)
    t.start()

print("The thread name is {} and end in {}".format(threading.current_thread().name,ctime()))

# result
'''
True
The thread name is Thread-1 and start in Fri Jun 29 16:39:36 2018
True
The thread name is Thread-2 and start in Fri Jun 29 16:39:36 2018
The thread name is MainThread and end in Fri Jun 29 16:39:36 2018
'''
```
## join方法
官方解释，join方法是用于阻塞线程的，一般要等待当前线程完成，才会进行下一个线程。根据实验，如果你对于每个线程都加一个join方法的话，那么就等于将程序变成了单线程，所以一般只给最后执行的子线程加一个join，这样，主线程就不会提前退出。
1. 每个子线程都加join
```python
for t in threads:
    print(t.daemon)
    t.start()
    t.join()
```
2. 先启动,再遍历子线程加join
```
for t in threads:
    print(t.daemon)
    t.start()

for t in threads:
    t.join()
```

## start方法
这个方法很直白，就是启动一个线程。

# 线程类
```python
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
```
# 总结
以上学习了python多线程的简单用法，实际中用法肯定比较复杂，比如说锁，比如说队列的多线程，还有待探索。
