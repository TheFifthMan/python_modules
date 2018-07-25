import asyncio

'''
I am test1 and the param is 2
the waitting x is 20
'''
async def test1(x):
    print("I am test1 and the param is {}".format(x))
    await asyncio.sleep(10)
    return x*10

# param 是一个future对象。想象一下，这个类来自未来。
def callback(param):
    print('the waitting x is {}'.format(param.result()))

#a = test1(2)
loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(test1(x)) for x in range(10)]
#task.add_done_callback(callback)
loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print(task.result())
