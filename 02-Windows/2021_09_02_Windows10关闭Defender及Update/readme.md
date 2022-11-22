# 01-Win10 20H2下关闭Defender
01 关闭篡改防护  
02 进入下列注册表项并添加值  
```
计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender
New->DWORD (32-bit) Value
DisableAntiSpyware
1（十进制下）
```

# 02-Win10 1909、Win10 20H2下关闭Update
01 服务->Windows Update->1）停止服务、2）启动类型改为禁用、3）恢复中第一次失败改为无操作  
经此操作后，再次点击Windows更新，如下图  
![image](./pic/01.png)  
02 上述操作执行完，当时不能执行更新，不过几天后发现更新服务会自动启动，启动类型变为手动，参考：https://zhidao.baidu.com/question/1609863160952004547.html  
根据参考连接，关闭任务计划中的Windows Update，任务计划程序库 -> Microsoft -> Windows -> WindowsUpdate，禁用其中的Scheduled Start，如下图  
![image](./pic/02.png)  

# 03-终极关闭Windows Update服务
通过上述方式关闭Update，过段时间后Update服务仍会启动，经过和同事交流，可参考如下文章彻底关闭Update服务  
https://blog.csdn.net/baidu_33864675/article/details/120668484  
将上述文章实现为批处理Disable-Windows-Update-Fully.bat

或者采用同事推荐的Windows Update Blocker.zip