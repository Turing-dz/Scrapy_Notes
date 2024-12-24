#io密集型任务使用多线程，计算密集型使用多进程
#1.全局解释器锁（GIL）global interpreter lock
import time
import threading
#cpu密集型任务
# def start():
#     i=0
#     for i in range(10000000):
#         i+=1
#     return
# def main():
#     s=time.time()
#     #2.单线程，裸奔
#     # for i in range(10):
#     #     start()
#     #3.多线程并发(伪并发)
#     ts={}
    
#     for i in range(10):
#         t=threading.Thread(target=start)#线程运行start函数
#         # t.setDaemon(True)#4.开启守护线程，非守护线程（“用户线程”）守护线程（“后台线程”）
#         t.start() # 启动线程，线程开始运行 `start` 函数
#         ts[i]=t#将线程放到字典中
#     for i in range(10):
#         ts[i].join() # 调用每个线程的 `join()` 方法，阻塞主线程直到该线程运行结束；join() 方法会阻塞主线程，直到调用 join() 的那个线程完成为止。
#     print(time.time()-s)
# if __name__=="__main__":
#     main()
#线程池（pip install threadpool）
#5.多进程：多线程对io密集型有效果，对cpu密集型没太大效果，所以使用多进程multiprocessing，因为每个进程都有独立独立的GIL锁，成本大，无法看到对方数据，需要使用栈（先进后出）或者队列(先进先出)进行获取
import multiprocessing
# def start(i):
#     time.sleep(3)
#     print(i)
#     print(multiprocessing.current_process().name)
#     print(multiprocessing.current_process().pid)
#     print(multiprocessing.current_process().is_alive())
# if __name__=="__main__":
#     print("start")
#     p=multiprocessing.Process(target=start,args=(1,),name="my_process")
#     p.start()
#     p.join()
#     print("stop")
#6.多进程通信,使用队列queue
def writeM(q):
    print("W:%s"%(multiprocessing.Process.pid))
    for i in range(10):
        print("W：%d"%i)
        q.put(i)
def readM(q):
    while True:
        value=q.get()
        print("R：%d"%value)
if __name__=="__main__":
    q=multiprocessing.Queue()
    print("start")
    pw=multiprocessing.Process(target=writeM,args=(q,))#这两个进程共享这个queue，传递信息
    pr=multiprocessing.Process(target=readM,args=(q,))
    pw.start()
    pr.start()
    pw.join() 
    print("finish")
#进程池(multiprocessing.Pool)
#7.lock锁（例如当连个线程操作同一个数字）
# number=0
# lock=threading.Lock()#创建一把锁，对多线程操作的数据上锁,开锁
# def addN():
#     global number
#     for i in range(1000000):
#         lock.acquire()#上锁
#         number+=1#计算机需要执行计算，赋值两步
#         lock.release()#开锁
# def downN():
#     global number
#     for i  in range(1000000):
#         lock.acquire()#上锁
#         number-=1
#         lock.release()#开锁
# print("start")
# t1=threading.Thread(target=addN)
# t2=threading.Thread(target=downN)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(number)
# print("stop")
#8.递归锁Rlock()递归锁在同一线程中可以多次获取，而不会发生死锁。当同一线程第一次获取锁后，可以再次获取锁，直到释放相同次数为止。递归锁内部维护一个计数器来记录当前锁被获取的次数，只有当计数器降到0时，锁才会真正释放。
# rlock = threading.RLock()
# def recursive_task(n):
#     rlock.acquire()
#     print(f"Acquired lock, n = {n}")
#     if n > 0:
#         recursive_task(n - 1)  # 递归调用，仍然会请求同一个锁
#     rlock.release()
#     print(f"Released lock, n = {n}")
# if __name__ == "__main__":
#     recursive_task(3)

