#-*-coding:utf-8-*-
import gevent 
from gevent import monkey
from datetime import datetime 
import time
monkey.patch_all()


#(venv) C:\Users\johnw\Music\note>python c:/Users/johnw/Music/note/async_modules/geventdemo.py
#[Movie] I am watch movie in 2018-07-11 12:10:29.017256
#[music] I am watch music in 2018-07-11 12:10:29.017256
#[Movie] Movie done 2018-07-11 12:10:31.018248
#[music] music done 2018-07-11 12:10:34.018833


def movie():
    print("[Movie] I am watch movie in {}".format(datetime.now()))
    print("[Movie] I am watch movie in {}".format(datetime.now()))
    print("[Movie] I am watch movie in {}".format(datetime.now()))
    print("[Movie] I am watch movie in {}".format(datetime.now()))
    time.sleep(2)
    print("[Movie] Movie done {}".format(datetime.now()))

def music():
    print("[music] I am watch music in {}".format(datetime.now()))
    time.sleep(5)
    print("[music] music done {}".format(datetime.now()))


if __name__ == "__main__":
    # 并发执行，并不阻塞，一旦遇到IO变化，立即挂起。
    ts = [gevent.spawn(movie),gevent.spawn(music)]
    gevent.joinall(ts)

