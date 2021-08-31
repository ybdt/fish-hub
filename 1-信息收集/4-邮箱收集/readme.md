### 1、原理
借助snov.io收集指定域名的邮箱

### 2、用法
直接用某大佬开发的工具snov.py，执行命令如下
```
python3.exe .\snov.py -u 注册时的邮箱 -p 注册时的密码 -t baidu.com
```
共收集到7898个邮箱，部分结果示例如下图  
![image](./pic/1.png)  

进一步优化的话，可考虑校验有效邮箱，可参考脚本verifyemail.py（脚本在用来校验baidu.com的邮箱时有问题，需要调整）  

### 3、参考链接
https://mp.weixin.qq.com/s/9QgYM3DU-93ODYDsTPUAxw
