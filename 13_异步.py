#concurrent.futures模块，具有线程池和进程池，管理并行任务等功能
#concurrent.futures.Executor虚拟基类，提供了异步执行方法：submit（func，args）;map（func，args）;shutdown(Wait=Tue);
#concurrent.futures.Future，Futur对象是submit任务到executor的实例；Executor是抽象类，
#concurrent.futures提供两个子类，各操作一个线程池和一个进程池:#concurrent.futures.ThreadPoolExecutor(max_workers),concurrent.futures.ProcessPoolExecutor(max_workers)
import concurrent.futures
import time
number_list=[1,2,3,4,5,6,7,8,9,10]
def mycount(number):
    for i in range(0,100000000):
        i+=1
    return i*number
if __name__=="__main__":
    #1.单线程运行cpu密集任务
    # s=time.time()
    # for item in number_list:
    #     out_ever=mycount(item)
    #     print(out_ever)
    # print("单线程使用时间："+str(time.time()-s))#50.15273666381836
    #2.线程池运行cpu密集任务
    # s=time.time()
    # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as excutor:
    #     futures=[excutor.submit(mycount,item) for item in number_list]
    #     for future in concurrent.futures.as_completed(futures):
    #         print(future.result())
    # print("线程池使用时间："+str(time.time()-s))#50.292454957962036
    #3.进程池运行cpu密集任务
    s=time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as excutor:
        futures=[excutor.submit(mycount,item) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print("进程池使用时间："+str(time.time()-s))#19.581161737442017