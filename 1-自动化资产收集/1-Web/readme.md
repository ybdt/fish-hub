# 0x00-获取公司备案名
ICP备案查询地址：https://beian.miit.gov.cn  
输入根域名（如wps.cn）查询对应的公司备案名  

# 0x01-收集父子公司
通过天眼查中的“股权穿透图”，收集目标企业的子公司及父公司  

# 0x02-收集根域  
ICP备案查询地址：https://beian.miit.gov.cn  
通过ICP备案收集根域，依次输入查询到的备案公司名，查询对应的全部根域名  

如果根域较多，可使用如下方式快速获取  
1、Chrome下F12，点击Network->All可查看全部请求及响应  
2、点击查询，可在右侧看到向/queryByCondition发起请求及对应的响应  
3、将响应保存到本地，通过脚本[ICP备案收集根域.py](./附件/ICP备案收集根域/ICP备案收集根域.py)批量提取  

# 0x03-收集子域
### 1-fofa收集子域
[https://fofa.so](https://fofa.so)  
结果导出：之前使用工具[https://github.com/wgpsec/fofa_viewer](https://github.com/wgpsec/fofa_viewer)，不过发现fofa_viewer导出的结果不完整，改用自己工具[fofa-Extractor.py](./附件/fofa-Extractor.py)  
### 2-phpinfo.me收集子域
[https://phpinfo.me/domain](https://phpinfo.me/domain)  
结果导出：可使用工具[phpinfo_me_extractor.py](./附件/phpinfo_me_extractor.py)  
### 3-subDomainsBrute收集子域
[https://github.com/lijiejie/subDomainsBrute](https://github.com/lijiejie/subDomainsBrute)  
### 4-ksubdomain收集子域
[https://github.com/knownsec/ksubdomain](https://github.com/knownsec/ksubdomain)  
### 5-OneForAll收集子域
[https://github.com/shmilylty/OneForAll](https://github.com/shmilylty/OneForAll)  
### 6-subfinder收集子域
[https://github.com/projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder)  

# 0x04-收集C段
### 1-nmap收集C段
查询到某个子域ip和目标组织位于同一城市，可考虑收集目标IP全端口、目标IP半个C段、目标IP整个C段  
坑1：上来就扫描整个C段，12小时候才发现，卡在第2台主机......  
经验1：扫描开始后要观察一下扫描进度，确实是否有防火墙，不要挂到VPS上就不管了  

# 0x05-参考链接
红蓝对抗之企业对外根域名资产收集 by 举起手来_火线Zone：https://mp.weixin.qq.com/s/irX-cQ23Pzb0pS8K-EE38Q  
fofa api相关：https://blog.csdn.net/wuyou1995/article/details/105592102  
fofa api相关：https://classic.fofa.so/api  
