python3.8中  
读取文件的时候，会根据平台将\r\n（Windows下）和\n（Linux下）转换成\n，在写文件的时候，会根据平台再将\n转换为对应的\r\n（Windows下）和\n（Linux下）

官网文档：
```
In text mode, the default when reading is to convert platform-specific line endings (\n on Unix, \r\n on Windows) to just \n. When writing in text mode, 
the default is to convert occurrences of \n back to platform-specific line endings.
```

以后这段代码可以不用了
```
if platform.system() == "Windows":
    linefeed = "\r\n";
elif platform.system() == "Linux":
    linefeed = "\n";
else:
    print("Unknown platform, exiting...");
    exit();
```

参考链接：  
https://docs.python.org/3.8/tutorial/inputoutput.html#reading-and-writing-files
