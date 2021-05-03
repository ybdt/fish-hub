shodan、zoomeye、fofa三大网络空间测绘引擎，zoomeye会每个月赠送10000条查询结果，故选择zoomeye

zoomeye搜索关键词的获取：先使用网站搜索，然后将网站搜索中的关键词用在命令行下

步骤1：  
注册一个zoomeye账户来获取token

步骤2：  
安装zoomeye官方提供的命令行程序zoomeye-python，地址：[https://github.com/knownsec/ZoomEye-python](https://github.com/knownsec/ZoomEye-python)，具体安装方式查看说明

步骤3：  
安装完成后执行zoomeye-python.bat，会生成一个json文件

步骤4：  
使用脚本zoomeye-python-auxiliary.py从json文件中提取ip、端口、协议到文件ip.txt中

亲测可用  
![image](./pic/0.png)
