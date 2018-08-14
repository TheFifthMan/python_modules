import asyncio
from datetime import datetime 
import time,requests

'''
start http://www.baidu.com and time is 2018-07-25 15:37:57.221670
start http://www.google.com and time is 2018-07-25 15:37:57.222670
start http://www.sina.com.cn and time is 2018-07-25 15:37:57.223670
done http://www.sina.com.cn and time is  2018-07-25 15:38:07.759670
done http://www.google.com and time is  2018-07-25 15:38:07.936670
done http://www.baidu.com and time is  2018-07-25 15:38:08.014670
'''
async def run(url):
    loop = asyncio.get_event_loop()
    print('start {} and time is {}'.format(url,datetime.now()))
    try:
        task = loop.run_in_executor(None,requests.get,url)
        #task2 = loop.run_in_executor(None,time.sleep,10)
        complete,pending = await asyncio.wait([task])
        for t in complete:
            print(t.result())

    except Exception as e:
        print(e)

    print('done {} and time is  {}'.format(url,datetime.now()))

url_list = ['http://www.baidu.com','http://www.google.com','http://www.sina.com.cn']
tasks = [asyncio.ensure_future(run(url)) for url in url_list]
loop = asyncio.get_event_loop()
# 这里是并发的场景，每当有协程挂起，就需要wait，如果没加，就会报错。
loop.run_until_complete(asyncio.wait(tasks))
