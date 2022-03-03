命令行下测试发现，mysql中的sql语句需要以分号结尾  
![image](./0.png)  
在命令行下进行联合查询注入测试，需要执行如下语句
```
select user from test0 where id='1' union select version();#';
```
如下图  
![image](./1.png)  
也就是注释符号前需要加个分号  
可是通常的sql注入payload
```
' union select version()#
```
并不需要加分号，这是为什么呢？
