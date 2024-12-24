#异步是事件驱动模型，异步是一种编程方式，专注于非阻塞执行，而多线程/多进程是一种并发模型。异步操作可以在单线程中实现，也可以与多线程、多进程组合使用来增强处理能力。
#协程是一个函数，有io操作，在进行io操作时可以暂停，无法直接执行
#1.asynico 标记异步函数,await 等待异步函数返回
import asyncio
# async def net():
#     return 11
# async def main():
#     d=await net()
#     print(d)
# # asyncio.run(main())
# # 代替 asyncio.run(main()) 使用以下代码，python3.7以下的版本使用
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()
#2.多个异步函数实现，使用列表存放任务对象
async def hello(i):
    print("start ",i)
    await asyncio.sleep(3)
    print("finish ",i)
if __name__=="__main__":
    tasks=[]
    for  i in range(4):
        tasks.append(hello(i))
    loop=asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()