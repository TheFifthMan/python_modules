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
    t1 = threading.Thread(target=thread1,daemon=True)
    t2 = threading.Thread(target=thread2,daemon=True)

    threads = []
    threads.append(t1)
    threads.append(t2)

    for t in threads:
        print(t.daemon)
        t.start()
    
    print("The thread name is {} and end in {}".format(threading.current_thread().name,ctime()))
 
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