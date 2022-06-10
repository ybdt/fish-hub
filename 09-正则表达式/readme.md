vscode中批量替换指定字符串  
idea代码审计时查询指定字符串  
...
均需要用到正则表达式

# 例子1
```
http://baichuan.sinopec.com/baichuan 想截取 /baichuan

(?<=com/).*$
```