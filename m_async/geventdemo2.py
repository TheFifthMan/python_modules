# 使用gevent+queue

import gevent 
from gevent import monkey
monkey.patch_all()
import time 
from datetime import datetime 
from gevent.queue import Queue 

q = Queue()
def producer():
    for i in range(10):
        #sleep(0.5)
        q.put(i)

def workers():
    while not q.empty():
        try:
            item = q.get()
            print("[Start]task {} and time {}".format(item,datetime.now()))
            time.sleep(2)
            print("[Done]task {} and time {}".format(item,datetime.now()))

        except Exception as e:
            pass
    

if __name__ == "__main__":
    start = datetime.now()
    producer()
    ts = [gevent.spawn(workers)for i in range(10)]
    gevent.joinall(ts)
    end=datetime.now()

    duration = (end - start)
    print(duration)


#0:00:02.004000


