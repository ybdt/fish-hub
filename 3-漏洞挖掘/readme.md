### 经验1
拿下一个目标web系统，下载代码之前一定要先看一下各个目录的大小（之前碰到过一个案例，打包完之后发现167G），命令如下
```
du -h --max-depth=1
```
使用如下命令选择性打包
```
首选：tar -jcvf b.tar.bz2
不支持bz2的时候，再使用：tar -zcvf b.tar.gz --exclude=./data --exclude=./tmp --exclude=./log --exclude=./queue ./*
```
