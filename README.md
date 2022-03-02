# 01 项目介绍
红队评估中外网打点的技战术

# 02 思路整理

### 资产收集
0x01-父子公司
```
通过天眼查等收集目标父子公司，可通过ENScan自动化收集目标父子公司
```
0x02-根域
```
通过ICP/IP地址/域名信息备案管理系统（https://beian.miit.gov.cn/#/Integrated/index）收集目标根域
```
0x03-子域
```
通过OneForAll等工具收集子域
```
0x04-C段
```
fofa收集目标子域，通过查看子域对应IP，可得知目标的大概C段
```
0x05-旁站
```
目标未使用CDN时，可通过nmap扫描目标全端口，查看开放哪些其他端口，通过其他端口切入
```
0x06-ASN
```
当目标组织较大时，可考虑收集目标所在ASN的全部资产
```
0x07-历史IP
```
通过ip138.com查看目标域名解析过的历史IP
```

```
https://github.com/r0eXpeR/GetInfo
```
### 指纹识别
```

```

### 漏洞检测
见项目：https://github.com/ybdt/poc-hub

### 口令检测
见项目：https://github.com/ybdt/dict-hub

### 钓鱼攻击
```
Flash钓鱼弹窗版：https://github.com/r00tSe7en/Flash-Pop
```

### 0day漏洞
```

```