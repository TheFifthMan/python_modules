import asyncio

'''
I am test1 and the param is 2
20
'''
async def test1(x):
    print("I am test1 and the param is {}".format(x))
    await asyncio.sleep(10)
    return x*10


a = test1(2)
loop = asyncio.get_event_loop()
# task 是来自未来的对象
task = asyncio.ensure_future(a)
# task.add_done_callback(callback)
loop.run_until_complete(task)
print(task.result())
