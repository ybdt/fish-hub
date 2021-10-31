# 1、根域收集
## 【1-ICP备案根域收集】
ICP备案查询地址：https://beian.miit.gov.cn  
输入域名如wps.cn，可查询所属公司，再通过所属公司查询所有根域名  
如果根域较多，可使用如下方式快速获取  
1、Chrome下F12，点击Network->All可查看全部请求及响应  
2、点击查询，可在右侧看到向/queryByCondition发起请求及对应的响应  
3、将响应保存到本地，通过脚本[ICP备案收集根域.py](./附件/ICP备案收集根域/ICP备案收集根域.py)批量提取  
## 【2-天眼查根域收集】
查看“股权穿透图”，收集目标企业的全资子公司  
# 2、子域收集
## 【1-fofa子域收集】  
[https://fofa.so](https://fofa.so)  
子域收集用法：domain="wps.cn"  
结果导出：可使用工具：[https://github.com/wgpsec/fofa_viewer](https://github.com/wgpsec/fofa_viewer)，不过发现导出的结果不完整，改用自己工具：[fofa-Extractor.py](./附件/fofa-Extractor.py)  
导出工具用法：访问API并在链接后面添加：&size=10000&full=true，保存到本地后，通过工具提取出url.txt和ip.txt  
## 【2-phpinfo.me子域收集】  
[https://phpinfo.me/domain](https://phpinfo.me/domain)  
子域收集用法：直接输入根域即可  
结果导出：可使用工具[phpinfo_me_extractor.py](./附件/phpinfo_me_extractor.py)  
导出工具用法：  
## 【3-subDomainsBrute子域收集】  
[https://github.com/lijiejie/subDomainsBrute](https://github.com/lijiejie/subDomainsBrute)  
子域收集用法：python3 ./subDomainsBrute.py -o subdomain.txt wps.cn  
## 【4-ksubdomain子域收集】  
[https://github.com/knownsec/ksubdomain](https://github.com/knownsec/ksubdomain)  
子域收集用法：sudo ./ksubdomain -d wps.cn -full -o wps_subdomain.txt  
## 【5-OneForAll子域收集】  
[https://github.com/shmilylty/OneForAll](https://github.com/shmilylty/OneForAll)  
子域收集用法：sudo python3 ./oneforall.py --target wps.cn run  
结果导出：工具会自动导出结果到OneForAll-master/results/下  
## 【6-subfinder子域收集】  
[https://github.com/projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder)  
子域收集用法：subfinder -dL domain.txt -v -o subDomain.txt  
结果导出：结果会输出到控制台及subDomain.txt中  

# 3、C段收集
【1-fofa获取目标全量资产】
```
fofa获取目标全部资产，再通过[fofa-Extractor.py](./附件/2-全量资产收集/fofa-Extractor.py)提取出url和ip  
直接使用API的话，想显示全部数据，需要在API后面添加：&size=10000&full=true  
```
【2-masscan获取目标全量资产】masscan快速扫描目标c段资产，再通过[masscan-Live-Detect.py](./附件/2-全量资产收集/masscan-Live-Detect.py)从扫描结果中提取出存活的端口资产  

# 4、参考链接
红蓝对抗之企业对外根域名资产收集 by 举起手来_火线Zone：https://mp.weixin.qq.com/s/irX-cQ23Pzb0pS8K-EE38Q  
fofa api相关：https://blog.csdn.net/wuyou1995/article/details/105592102  
fofa api相关：https://classic.fofa.so/api  
