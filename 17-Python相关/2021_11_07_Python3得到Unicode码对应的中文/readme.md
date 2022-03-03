先检查text是什么类型

如果type(text) is bytes，那么
```
text.decode('unicode_escape')
```

如果type(text) is str，那么
```
text.encode('latin-1').decode('unicode_escape')
```

参考链接：  
https://www.zhihu.com/question/26921730  
