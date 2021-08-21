shodan、zoomeye、fofa三大网络空间测绘引擎，zoomeye会每个月赠送10000条查询结果，本文介绍如何使用zoomeye及提取zoomeye查询结果

zoomeye命令行模式下的搜索关键词：先使用zoomeye网站进行搜索测试，然后将网站搜索中的关键词用在命令行下

步骤1：  
注册一个zoomeye账户来获取token

步骤2：  
安装zoomeye官方提供的命令行程序zoomeye-python，地址：[https://github.com/knownsec/ZoomEye-python](https://github.com/knownsec/ZoomEye-python)，具体安装方式查看说明

步骤3：  
安装完成后执行如下命令，会生成一个json文件
```
zoomeye search -num 20 -save port,service "网康下一代防火墙"
```

步骤4：  
使用脚本zoomeye-extractor.py从json文件中提取ip、端口、协议到文件ip.txt中
