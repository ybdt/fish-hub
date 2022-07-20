```
import threading
import time
import queue
 
 
# 下面来通过多线程来处理Queue里面的任务：
def work(q):
    while True:
        if q.empty():
            return
        else:
            t = q.get()
            print("当前线程sleep {} 秒".format(t))
            time.sleep(t)
 
 
def main():
    # 创建队列并填充消息
    q = queue.Queue()
    for i in range(5):
        q.put(i)  # 往队列里生成消息
    
    # 单线程
    # work(q)
 
    # 多线程
    thread_num = 5
    threads = []
    for i in range(thread_num):
        t = threading.Thread(target=work, args=(q,))
        threads.append(t)
        t.start()
    for i in range(thread_num):
        threads[i].join()
 
 
if __name__ == "__main__":
    start = time.time()
    main()
    print('耗时：', time.time() - start)
```
参考链接：  
https://www.cnblogs.com/franknihao/p/6627857.html  
https://www.liujiangblog.com/course/python/79  
https://juejin.cn/post/6875330340534583309  
https://developer.aliyun.com/article/700856  
https://blog.csdn.net/qq_24285815/article/details/98727058  
https://blog.csdn.net/xuezhangjun0121/article/details/105199165  