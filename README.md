# Web打点
## 1、攻击面收集
### 1.1 子域名收集  
https://fofa.so/  
https://phpinfo.me/domain/  
https://www.yunsee.cn/  
https://fp.shuziguanxing.com/#/  
### 1.2 旁站收集
解析出子域名的ip，使用nmap对每一个ip进行全端口扫描
### 1.3 web文件目录收集
[dirsearch](https://github.com/maurosoria/dirsearch)或[ffuf](https://github.com/ffuf/ffuf)结合[字典项目dict-hub](https://github.com/ybdt/dict-hub)  
## 2、目标信息收集
### 2.1 乌云历史漏洞库  
https://wooyun.x10sec.org/  
http://wy.zone.ci/

目标组织IP段收集  
https://www.robtex.com/




待尝试思路记录
1、身份隐藏，可参考：  
https://mp.weixin.qq.com/s/-DqGsjqgxC5MUf4poqC5XQ

```
用过的较好的Web安全学习资源：
[https://portswigger.net/web-security](https://portswigger.net/web-security)（包含原理讲解和动手实验，完全免费）
[https://www.w3schools.com/](https://www.w3schools.com/)（包含知识讲解和动手实验，完全免费）
```

```
学习一个漏洞的原理时，要考虑这个漏洞通常出现在什么样的开发架构中，这样的开发架构通常出现在什么样的业务中，每次积累一
点，日积月累，最终成长为看到一个业务大概就知道存在什么漏洞
```
