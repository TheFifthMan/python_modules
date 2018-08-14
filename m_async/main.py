#-*- coding:utf-8 -*-
# 异步
'''
在我们的异步编程中，有两个东西
1. 我们的应用程序
2. 我们的系统
如果要做异步程序，我们的程序就要做成非阻塞调用。
因为异步程序跟多线程和多进程不一样，其不同点为：
1. 异步程序是单线程，通过代码切换IO状态变化
2. 代码中不能有阻塞，否则就停在这里了。
非阻塞调用后，应用程序去做其他的事情。
这个需要处理的IO就放在了这里，应用程序不管了。

那么怎么判断IO状态的变化？
这个时候就需要系统来做这个事情
所以，系统将IO状态变化都叫做事件，可读事件，可写事件。并提供了专门的模块用于接受事件的通知
比如说 kqueue 和 epoll模块

系统知道了IO变化，那么该如何进行下去？
这个时候要用到回调。
我们要设置一个事件循环接受系统传过来的消息去绑定回调函数

一旦有了事件，也就是IO状态变化，我们就调用函数进行下一步的执行
否则我们应用程序就执行其他的东西

缺点：
共享状态管理困难
错误处理困难

'''

import asyncio
import time
from datetime import datetime 

async def test1():
    print("I am test1...the start time is {}".format(datetime.now()))
    # 没有挂起
    await test2()
    print("test1 done. {}".format(datetime.now()))

async def test2():
    print("I am test2...the start time is {}".format(datetime.now()))
    time.sleep(5)
    print("test2 done. {}".format(datetime.now()))

loop =  asyncio.get_event_loop()
loop.run_until_complete(test1())
