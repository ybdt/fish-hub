# 1、根域收集
## 【1-ICP备案收集根域】
ICP备案查询地址：https://beian.miit.gov.cn  
输入域名如wps.cn，可查询所属公司，再通过所属公司查询所有根域名  
如果根域较多，可使用如下方式快速获取  
1、Chrome下F12，点击Network->All可查看全部请求及响应  
2、点击查询，可在右侧看到向/queryByCondition发起请求及对应的响应  
3、将响应保存到本地，通过脚本[ICP备案收集根域.py](./附件/ICP备案收集根域/ICP备案收集根域.py)批量提取  
## 【2-天眼查收集根域】
查看“股权穿透图”，收集目标企业的全资子公司  
# 2、子域收集
## 【1-fofa收集子域】
[https://fofa.so](https://fofa.so)  
结果导出：之前使用工具[https://github.com/wgpsec/fofa_viewer](https://github.com/wgpsec/fofa_viewer)，不过发现fofa_viewer导出的结果不完整，改用自己工具[fofa-Extractor.py](./附件/fofa-Extractor.py)  
## 【2-phpinfo.me收集子域】
[https://phpinfo.me/domain](https://phpinfo.me/domain)  
结果导出：可使用工具[phpinfo_me_extractor.py](./附件/phpinfo_me_extractor.py)  
## 【3-subDomainsBrute收集子域】
[https://github.com/lijiejie/subDomainsBrute](https://github.com/lijiejie/subDomainsBrute)  
## 【4-ksubdomain收集子域】
[https://github.com/knownsec/ksubdomain](https://github.com/knownsec/ksubdomain)  
## 【5-OneForAll收集子域】
[https://github.com/shmilylty/OneForAll](https://github.com/shmilylty/OneForAll)  
## 【6-subfinder收集子域】
[https://github.com/projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder)  
# 3、C段收集
## 【1-nmap收集C段】
查询到某个子域ip和目标组织位于同一城市，可考虑收集目标IP全端口、目标IP半个C段、目标IP整个C段  
坑1：上来就扫描整个C段，12小时候才发现，卡在第2台主机......  
经验1：扫描开始后要观察一下扫描进度，确实是否有防火墙，不要挂到VPS上就不管了  
# 4、目录收集
## 【1-dirsearch收集目录】
[https://github.com/maurosoria/dirsearch](https://github.com/maurosoria/dirsearch)  
# 5、优秀项目
https://github.com/ffuf/ffuf  
https://github.com/H4ckForJob/dirmap  
# 6、参考链接
红蓝对抗之企业对外根域名资产收集 by 举起手来_火线Zone：https://mp.weixin.qq.com/s/irX-cQ23Pzb0pS8K-EE38Q  
fofa api相关：https://blog.csdn.net/wuyou1995/article/details/105592102  
fofa api相关：https://classic.fofa.so/api  
