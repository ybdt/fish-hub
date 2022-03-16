# 常用语句记录
```
update user set host='%' where user='root' AND host='localhost';
update user set host='localhost' where user='root' AND host='%';
FLUSH PRIVILEGES;
Linux下查询输出行数：
cat pass.txt | wc -l
Windows下查询输出行数：
kubectl.exe -s 172.16.61.100:8089 get pods | find /v /c ""
```

# MSSQL
```
CREATE TABLE #temp_41c0549e42919922 (TableName VARCHAR (255),RowsCount INT)
DECLARE @dbname NVARCHAR(500)
DECLARE @SQL NVARCHAR(4000)
DECLARE MyCursor CURSOR
FOR (SELECT Name FROM master..SysDatabases where name not in ('master','model', 'msdb', 'tempdb') and status not in (66048,66056))
OPEN MyCursor;
FETCH NEXT FROM MyCursor INTO @dbname;
WHILE @@FETCH_STATUS = 0
Begin
SET @SQL = 'insert into #temp_41c0549e42919922 SELECT '''+@dbname+'..''+a.name, b.rows FROM '+@dbname+'..sysobjects AS a INNER JOIN '+@dbname+'..sysindexes AS b ON a.id = b.id WHERE (a.type = ''u'') AND (b.indid IN (0, 1)) ORDER BY b.rows DESC'
exec(@SQL);
FETCH NEXT FROM MyCursor INTO @dbname;
End
CLOSE MyCursor;
DEALLOCATE MyCursor;
SELECT TableName,RowsCount FROM #temp_41c0549e42919922 WHERE RowsCount>0 ORDER
BY RowsCount desc
DROP TABLE #temp_41c0549e42919922
select schema_name(t.schema_id) as [Schema], t.name as TableName,i.rows as [RowCount]
from sys.tables as t, sysindexes as i
where t.object_id = i.id and i.indid <=1 ORDER BY [RowCount] desc
```

# MySQL
```
select table_schema,table_name,table_rows,table_comment from information_schema.tables WHERE table_schema not in ('performance_schema','mysql', 'sys', 'information_schema') order by table_rows desc;oracle
```

# Oracle
```
SELECT '/*'||OWNER||'.'||TABLE_NAME||'*/

SELECT ROWNUM,'||OWNER||'.'||TABLE_NAME||'.*'||' from
'||OWNER||'.'||TABLE_NAME||' where ROWNUM<100;',NUM_ROWS FROM SYS.ALL_TABLES where OWNER not in ('SYS','SYSMAN') and NUM_ROWS>0 ORDER BY NUM_ROWS desc;
```
可插入and rownum < 100筛选前100条数据