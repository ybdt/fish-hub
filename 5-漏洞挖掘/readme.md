### 经验1
拿下一个目标web系统，想下载代码，一定要先看一下各个目录的大小（之前碰到过一个案例，打包完之后发现167G），命令如下
```
du -h --max-depth=1
```
再使用如下命令选择性打包
```
首选：tar -jcvf b.tar.bz2
不支持bz2的时候，再使用：tar -zcvf b.tar.gz --exclude=./data --exclude=./tmp --exclude=./log --exclude=./queue ./*
```
### 经验2
打点时拿到一个低权限的口子，提权失败，想上传fscan去扫描内网，需要知道ip，但不能执行
```
ifconfig、ip addr
```
可使用
```
netstat -antup
```
代替
