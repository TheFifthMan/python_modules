import asyncio
from datetime import datetime 
'''
test1 start 2018-07-25 14:35:56.808890
test1 start 2018-07-25 14:35:56.808890
test1 start 2018-07-25 14:35:56.808890
test1 done 2018-07-25 14:36:01.835863
test1 done 2018-07-25 14:36:01.835863
test1 done 2018-07-25 14:36:01.835863
'''

async def test1():
    print("test1 start {}".format(datetime.now()))
    await asyncio.sleep(5)
    print("test1 done {}".format(datetime.now()))


if __name__ == "__main__":
    a = test1()
    b = test1()
    c = test1()
    loop = asyncio.get_event_loop()
    task = [
        asyncio.ensure_future(a),
        asyncio.ensure_future(b),
        asyncio.ensure_future(c),        
    ]
    loop.run_until_complete(asyncio.wait(task))
    