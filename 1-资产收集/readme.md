# 1、子域旁站收集
【1-fofa子域收集】
```
[https://fofa.so](https://fofa.so)，用法：domain="wps.cn"  
```
【2-phpinfo.me子域收集】
```
[https://phpinfo.me/domain](https://phpinfo.me/domain)，用法：直接输入根域即可  
```
【3-subDomainsBrute子域收集】
```
[https://github.com/lijiejie/subDomainsBrute](https://github.com/lijiejie/subDomainsBrute)，用法：python3 ./subDomainsBrute.py -o wps.cn  
```
【4-ksubdomain子域收集】
```
[https://github.com/knownsec/ksubdomain](https://github.com/knownsec/ksubdomain)，用法：sudo ./ksubdomain -d wps.cn -full -o wps_subdomain.txt  
```
【5-OneForAll子域收集】
```
[https://github.com/shmilylty/OneForAll](https://github.com/shmilylty/OneForAll)，用法：sudo python3 ./oneforall.py --target wps.cn run  
```
【6-nmap旁站收集】
```
nmap扫描主域ip的全端口，用法：nmap -p1-65535  
```
【7-aizhan旁站收集】
```
[https://dns.aizhan.com](https://dns.aizhan.com)，用法：直接输入ip即可  
```

# 2、其他根域收集
【1-ICP备案收集根域】  
```
ICP备案查询地址：https://beian.miit.gov.cn  
输入域名如wps.cn，可查询所属公司，再通过所属公司查询所有根域名  
工具使用  
1、Chrome下F12，点击Network->All可查看全部请求及响应  
2、点击查询，可在右侧看到向/queryByCondition发起请求及对应的响应  
3、将响应保存到本地，通过脚本[ICP备案提取主域信息.py](./附件/1-ICP备案收集根域/ICP备案提取主域信息.py)提取根域  
```
【2-企查查收集控股子公司】
```
通过股权穿透图收集目标企业子公司  
```
【3-Whois收集关联根域及邮箱】  
【4-SSL证书收集关联根域】  
【5-DNS解析收集关联根域】  
【6-Web配置收集关联根域】  

# 3、全量资产收集
【1-fofa获取目标全量资产】
```
fofa获取目标全部资产，再通过[fofa-Extractor.py](./附件/2-全量资产收集/fofa-Extractor.py)提取出url和ip  
直接使用API的话，想显示全部数据，需要在API后面添加：&size=10000&full=true  
```
【2-masscan获取目标全量资产】
```
masscan快速扫描目标c段资产，再通过[masscan-Live-Detect.py](./附件/2-全量资产收集/masscan-Live-Detect.py)从扫描结果中提取出存活的端口资产  
```

# 参考链接
【红蓝对抗之企业对外根域名资产收集 by 举起手来_火线Zone】https://mp.weixin.qq.com/s/irX-cQ23Pzb0pS8K-EE38Q  
【fofa api相关】https://blog.csdn.net/wuyou1995/article/details/105592102  
【fofa api相关】https://classic.fofa.so/api  
