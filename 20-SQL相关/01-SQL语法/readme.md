记住：SQL对大小写不敏感

1、关于单双引号  
SQL中要求文本值被单引号包围（多数系统也允许双引号）  
数字值不应该被引号包围（但是数字值被引号包围也不会造成语法错误）  
参考链接：  
https://www.w3schools.com/sql/sql_where.asp

2、关于分号  
分号的作用是分隔多条SQL语句，有些数据库要求分号，如MySQL，有些数据库不要求分号，如MS Access、SQL Server 2000

3、xml操作相关  
extractvalue(anything, "/x/xx/xxx")：从xml文档中提取数据，需要注意extractvalue能查询的最大长度为32位  
updatexml(anything, "/x/xx/xxx", andthing)：更新xml文档中的数据，需要注意extractvalue能查询的最大长度为32位

4、字符串连接  
concat(str1, str2, ..., strn)：连接多个字符串  
concat_ws->concat("连接符", str1, str2, ... strn)：使用连接符连接多个字符串

5、字符串切割  
substr(s, start, length)：从字符串s的start位置（位置从1开始计数），截取length长度  
substring：用法、功能完全等同于substr
