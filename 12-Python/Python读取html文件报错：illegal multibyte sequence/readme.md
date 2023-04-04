```
f = open(file_name, "r");
html_doc = f.read();
其中file_name是html页面的文件句柄
```
上述代码报错
```
UnicodeDecodeError: 'gbk' codec can't decode byte 0xfe in position 1501064: illegal multibyte sequence
```
说明python3解释器已经在用gbk字符集去解码目标文件，但仍然碰到不能识别的多字节序列，改用字符集更大的gb18030，下述代码不再报错
```
f = open(file_name, "r", encoding="gb18030");
html_doc = f.read();
```

参考链接：  
https://www.huaweicloud.com/articles/f3dc1b1666cf4c11c0c7e5824317f1c0.html