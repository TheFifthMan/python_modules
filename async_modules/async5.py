import requests
import asyncio
from datetime import datetime 
import time
'''
start http://www.baidu.com and time is 2018-07-25 15:09:52.206003
done http://www.baidu.com and time is  2018-07-25 15:10:02.208971
start http://www.google.com and time is 2018-07-25 15:10:02.978971
done http://www.google.com and time is  2018-07-25 15:10:12.978971
start http://www.sina.com.cn and time is 2018-07-25 15:10:16.063971
done http://www.sina.com.cn and time is  2018-07-25 15:10:26.063971
'''
async def run(url):
    r = requests.get(url,verify=False)
    print('start {} and time is {}'.format(url,datetime.now()))
    time.sleep(10)
    print('done {} and time is  {}'.format(url,datetime.now()))

url_list = ['http://www.baidu.com','http://www.google.com','http://www.sina.com.cn']
tasks = [asyncio.ensure_future(run(url)) for url in url_list]
loop = asyncio.get_event_loop()
# 这里是并发的场景，每当有协程挂起，就需要wait，如果没加，就会报错。
loop.run_until_complete(asyncio.wait(tasks))
