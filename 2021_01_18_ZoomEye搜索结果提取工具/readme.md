shodan、zoomeye、fofa三大网络空间测绘引擎，zoomeye会每个月赠送10000条查询结果，故选择zoomeye

#### 步骤1：
需要注册一个zoomeye账户来获取token

#### 步骤2：
需要安装zoomeye官方提供的命令行程序zoomeye-python获取zoomeye的搜索结果，地址：[https://github.com/knownsec/ZoomEye-python](https://github.com/knownsec/ZoomEye-python)，具体安装方式查看说明

#### 步骤3：
安装完成后执行zoomeye-python.bat，会生成一个包含搜索结果的文件

#### 步骤4：
使用脚本zoomeye_ip_extract.py从搜索结果文件中提取ip、端口到文件ip.txt中

亲测可用  
![image](./pic/a.png)
