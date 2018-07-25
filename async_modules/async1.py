import asyncio

async def test1():
    await test2()
    print('This is test1')

async def test2():
    print("This is test2")


if __name__ =="__main__":
    b = test1()
    b.send(None)