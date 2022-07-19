```
import time
import threading

class MyThread(threading.Thread):
    def __init__(self, counter, name):
        threading.Thread.__init__(self)
        self.counter = counter
        self.name = name

    def run(self):
        self.counter[0] += 1
        time.sleep(1)
        print(self.counter[0])


if __name__ == '__main__':
    counter = [0]
    for i in range(1, 11):
        t = MyThread(counter, i)
        t.start()
```
参考链接：  
https://www.cnblogs.com/franknihao/p/6627857.html  
https://www.liujiangblog.com/course/python/79  
https://juejin.cn/post/6875330340534583309  