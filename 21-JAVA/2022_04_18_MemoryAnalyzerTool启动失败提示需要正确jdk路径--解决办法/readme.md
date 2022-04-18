我用的MemoryAnalyzerTool版本是1.12.0，这个版本需要jdk11，可我本机默认是jdk8，所以需要折腾一下

可修改MemoryAnalyzerTool的配置文件MemoryAnalyzer.ini指定jdk路径
```
-vm
C:\Program Files\Java\jdk-11.0.10\bin\javaw.exe

-startup
plugins/org.eclipse.equinox.launcher_1.6.200.v20210416-2027.jar

--launcher.library
plugins/org.eclipse.equinox.launcher.win32.win32.x86_64_1.2.200.v20210429-1609

-vmargs
-Xmx1024m
```

这里需要注意一点，也是我碰到的一个小坑：即使jdk路径有空格也不能用双引号（跟多数情况不太一样），否则还是会报错找不到