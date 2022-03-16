问题出现在写入文件时

解决方案：以后写入文件时习惯指定编码，代码如下
```
with open("live.txt", "w", encoding='UTF-8') as fw_s:
```
