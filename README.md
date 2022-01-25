### 0x01-免责声明
该项目仅供授权下使用，禁止使用该项目进行违法操作，否则自行承担后果，请各位遵守《中华人民共和国网络安全法》！！！

# 0x02-项目介绍
红队评估中外网打点的技战术

# 0x03-思路整理
https://github.com/r0eXpeR/GetInfo

## 1.1、旁站
### 1.1.1、目标未使用CDN时，可通过nmap扫描目标全端口，查看开放哪些其他端口，通过其他端口切入
## 1.2、子域
### 1.2.1、通过fofa收集目标子域
提取证书里的关键字
domain="wps.cn"
host="wps.cn"
header="wps.cn"
cert="wps.cn"
cert="Zhuhai Kingsoft Office Software Co., Ltd."
cert="华为"
org="Zhuhai Kingsoft Office Software Co., Ltd."
### 1.2.2、通过hunter收集目标子域
https://phpinfo.me/domain/
### 1.2.4、OneForAll
## 1.3、网站证书资产收集
查看字段：使用者
查看字段：使用者可选名称
### C段
fofa收集目标子域，通过查看子域对应IP，可得知目标的大概C段
### ASN
当目标组织较大时，可考虑收集目标所在ASN的全部资产
### 历史IP
通过ip138.com查看目标域名解析过的历史IP


0x03-爆破工具+通用口令  
3.1、规律口令  
3.1.1、根据目标域名生成弱账户或弱口令，如：单位名称首字母小写@123、等  
3.2、弱口令自动化  
3.2.1、自动化检测Web弱口令  