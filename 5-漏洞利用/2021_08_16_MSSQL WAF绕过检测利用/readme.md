# 0、基于大小写的WAF绕过
对每个字符进行大小写尝试

# 1、基于拦截空格的WAF绕过
常见有5个位置即：select * from admin where id=1【位置一】union【位置二】select【位置三】1,2,db_name()【位置四】from【位置五】admin

经测试发现，MSSQL中关键字能和前边的值没有空格（能和前边的值挨着），但不能和后边的值没有空格（不能和后边的值挨着）

## 1.1 基于拦截空格的WAF绕过——使用注释符代替空格
```
select session_id,command from sys.dm_exec_requests where session_id=12/**/and/**/1=@@VERSION;
```
如下图  
![image](./pic/0.png)
## 1.2 基于拦截空格的WAF绕过——使用%00-%1F代替空格
%20本身是空格的URL编码，故它不能绕过WAF

## 网上误导纠正
1、有人提到浮点数能充当空格，经过测试，浮点数充当空格是不报错，但并不能正确显示结果，如下图  
![image](./pic/1.png)

参考链接：  
https://www.cnblogs.com/xiaozi/p/6930013.html

# 2、基于拦截关键字的WAF绕过
## 网上误导纠正
MSSQL下并不能使用&&代替and、||代替or，mssql 2008 r2下测试如下：  
![image](./pic/2.png)
