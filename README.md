# 0x00 项目介绍
本项目专注于实战中打点思路的总结

# 0x01 思路汇总
## 1、Web打点
### 1.1、攻击面收集
#### 1.1.1、子域名收集  
https://fofa.so/  
https://phpinfo.me/domain/  
https://www.yunsee.cn/  
https://fp.shuziguanxing.com/#/  

#### 1.1.2、旁站收集
解析出子域名的ip，使用nmap对每一个ip进行全端口扫描

#### 1.1.3、web文件目录收集
[dirsearch](https://github.com/maurosoria/dirsearch)或[ffuf](https://github.com/ffuf/ffuf)结合[字典项目dict-hub](https://github.com/ybdt/dict-hub)  

### 1.2、目标信息收集
#### 1.2.1、通过乌云漏洞库收集账号密码    
https://wooyun.x10sec.org/  
http://wy.zone.ci/  

## 2、社工钓鱼

## 3、近源渗透

# 0x02 免责声明
该项目仅供授权下使用或学习使用，禁止使用该项目进行违法操作，请各位遵守《中华人民共和国网络安全法》以及相应地方的法律法规，否则自行承担相关责任！
