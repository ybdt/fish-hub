# 起源
有个需求，需要在Windows10下实现frp开机自启，配置计划任务后一直失败

# 解决
配置计划任务需要指定文件启动路径，否则不能开机自启

# 新问题
用一段时间后，内网穿透会失效，怀疑是程序down了

# 新问题解决
采用nssm，将bat注册为服务，不确定内网穿透是否不会失效，用一段时间试试

```
进入win64目录下
nssm install frp
填入文件路径和启动目录这2个参数
```
参考：https://lz5z.com/nssm将应用写入Windows服务/  
nssm下载：https://nssm.cc/download  

#### 经排查，用一段时间失效不是服务或计划任务的问题，是frp设置了有效时间为7天

# 参考
https://www.3mg.net/news/33.html  