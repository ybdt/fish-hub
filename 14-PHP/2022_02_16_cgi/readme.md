# cgi是什么？
简单讲，是一个协议，规定web server将哪些数据，以什么样的格式传递给后端，后端再以什么格式，将哪些数据传递给web server，这些规范就是cgi

# fastcgi是什么？
简单讲，是cgi协议的增强版，可以并行执行，提高效率，也是一个协议  

# php-fpm是什么？
简单讲，是一个实现了fastcgi协议的进程管理器程序，管理php-cgi  

# php-cgi是什么？  
简单讲，是一个实现了cgi协议的程序，只能处理请求返回结果，不能管理进程，故需要php-fpm  

参考链接：  
https://blog.csdn.net/wplblog/article/details/103612817  