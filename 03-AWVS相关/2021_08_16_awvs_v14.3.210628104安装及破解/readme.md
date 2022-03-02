截止到2021/08/16，AWVS v14.3.210628104是最新版  
参考：https://www.acunetix.com/support/build-history/  

还可尝试docker版本  
参考链接：https://blog.zygd.site/AWVS14%20Docker.html#AWVS14-Docker  

### 0x01 安装过程
```
1、安装包下载地址：https://www.fahai.org/index.php/archives/126/
2、我下载的linux版，安装在kali虚拟机中，执行：sudo bash ./acunetix_14.3.210628104_x64.sh
3、接下来按照提示操作即可
```
### 0x02 破解过程
```
1、破解补丁下载地址：https://www.fahai.org/index.php/archives/132/
2、解压缩并拷贝内容到指定目录下：sudo cp /home/kali/Desktop/Aw14_Patch/* /home/acunetix/.acunetix/data/license
```
访问[https://127.0.0.1:3443/](https://127.0.0.1:3443/)，点击About，界面如下  
![image](./pic/1.png)  
### 0x03 破解过程补充
```
问题（只看了版本界面，没执行扫描任务，就以为破解成功，大意了~）如下：
1、执行完上述破解过程后，添加目标->开始扫描会报错
2、关闭后再次打开会显示破解之前的界面

解决（经排查发现/home/acunetix/.acunetix/data/license/下的license_info.json被删除后会自动创建）如下：
1、破解补丁下载地址：https://www.fahai.org/index.php/archives/132/
1、断开网络并关闭Acunetix服务：sudo systemctl stop Acunetix
2、解压缩并拷贝内容到指定目录下：sudo cp /home/kali/Desktop/Aw14_Patch/* /home/acunetix/.acunetix/data/license
4、修改文件属主：sudo chown acunetix:acunetix /home/acunetix/.acunetix/data/license/*
```
访问[https://127.0.0.1:3443/](https://127.0.0.1:3443/)，能够成功执行扫描任务，界面如下  
![image](./pic/2.png)  
注：直接扫到了一个比较隐蔽的时间盲注，如下
```
/index.php?a=index&c=search&keyword=1&m=&p=2&type=if(now()=sysdate(),sleep(7),0)
```
牛逼！！！
### 0x04 升级内容
```
1、我之前的版本是v13.0.200217097，从之前的版本到v14.3.210628104涉及大量的新增功能、bug修复、功能更新、新增漏洞检查，其中漏洞检查新增高达142个，如下：

New check for Weak key used to sign cookie in Play framework
JavaScript Library Audit now supports TinyMCE
New check for BigIP iRule command injection
New check for XSS in .NET session in URL
New check for Remote Code Execution (RCE) in Ruby on Rails (CVE-2019-5420)
New Check for Oracle E-Business Suite Deserialisation RCE
New Check for Oracle E-Business Suite SSRF (CVE-2017-10246)
New Check for Oracle E-Business Suite SSRF (CVE-2018-3167)
New Check for Oracle E-Business Suite SQL Injection (CVE-2017-3549)
New checks for WordPress Core and plugins, Joomla and Drupal
New check for Server-Side Template Injection (SSTI) in ASP.NET Razor
New check for Oracle BI AMF Deserialization RCE (CVE-2020-2950)
New check for Possible Cross Site Scripting via jquery.htmlPrefilter() (CVE-2020-11023)
New check for Stored XSS in WP theme Onetone (CVE-2019-17230 and CVE-2019-17231)
Updated detection of phpinfo pages
New checks in WordPress Core and WordPress plugins
New checks for default credentials in over 65 web applications
New check for vBulletin 5.6.1 (and earlier) nodeId SQL injection
New check for Cmd hijack vulnerability
New check for PHP opcache-gui publicly accessible
New check for Laravel debug mode enabled
New check for Laravel Health Monitor publicly accessible
New check for Laravel Health Horizon publicly accessible
New check for Laravel Health LogViewer publicly accessible
New check for Laravel Health Telescope publicly accessible
New check for Laravel Ignition Reflected Cross-Site Scripting
New check for Laravel framework weak secret key
New check for HTML Attribute Injection
New check for Clockwork PHP dev tool enabled
New check for PHP Debug Bar enabled
New check for Broken Link Hijacking
New checks for Cookie misconfigurations leading to security issues
New vulnerabilities for WordPress Core, WordPress plugins, Joomla and Drupal
New test for F5 BIG-IP Traffic Management User Interface (TMUI) RCE [CVE-2020-5902]
New test for Composer installed.json publicly accessible
New test for Symfony debug mode enabled
New test for Symfony Profiler open
New test for Directory Traversal with spring-cloud-config-server [CVE-2020-5410]
New test for Grafana avatar SSRF [CVE-2020-13379]
New test for rack-mini-profiler environment variables disclosure
New test for Telerik Web UI RadAsyncUpload Deserialization [CVE-2019-18935]
New check for Insecure Inline Frames
New check for Remote code execution of user-provided local names in Rails
New check for SAP NetWeaver RECON auth bypass vulnerability
New check for H2 console publicly accessible
New check for PHP version disclosure
New check for Atlassian JIRA ServiceDesk misconfiguration
New test for Jolokia XML External Entity (XXE) vulnerability
New checks for WordPress core, WordPress themes, WordPress plugins, Joomla and Drupal
New check for SAP NetWeaver RECON (CVE-2020-6287)
New check for DNN (DotNetNuke) CMS Cookie Deserialization RCE (CVE-2017-9822)
New check for Insecure Referrer Policy
New check for Remote code execution of user-provided local names in Rails
New check for Cisco Adaptive Security Appliance (ASA) Path Traversal (CVE-2020-3452)
New check for Total.js Directory Traversal (CVE-2019-8903)
New check for Envoy Metadata disclosure
New checks for WordPress Core / Plugins / Themes, Drupal and Joomla vulnerabilities
New test for Apache OFBiz XMLRPC Deserialization RCE (CVE-2020-9496)
New test for No HTTP Redirection
Numerous tests related to TLS / SSL, including:
Added support for 200 new cipher suites, bringing the total number of supported cipher suites to 360
New test for TLS/SSL Diffie-Hellman Key Reuse (prerequisite for Raccoon Attack)
New test for TLS/SSL LOGJAM attack (CVE-2015-4000)
New test for TLS/SSL Sweet32 attack (CVE-2016-2183 and CVE-2016-6329
Alert if server offers cipher suites with symmetric encryption key length <128
Alert if server offers cipher suites using symmetric encryption algorithms RC2, DES (insecure), IDEA
Alert if server offers cipher suites using ANON, NULL, SHA-1 for authentication
Alert if server offers cipher suites using MD5 for HMAC
New vulnerability checks for WordPress plugins and Drupal core
New check for JavaScript Source map detected
New check for Unauthenticated Remote Code Execution via JSONWS in Liferay 6.1 (LPS-88051)
New check for Oracle WebLogic Server unauthenticated remote code execution (CVE-2020-14882)
Updated WordPress plugin checks
New test for Zabbix authentication bypass / guest user
New test for Typo3 Admin publicly accessible
New test for Typo3 debug mode enabled
New test for Oracle WebLogic Remote Code Execution via IIOP
New test for Web Cache Poisoning DoS
New test for client-side prototype pollution
Improved web cache poisoning test
New test for SAP IGS XXE (CVE-2018-2392, CVE-2018-2393)
New test for Odoo LFI (CVE-2019-14322)
New test for Unrestricted access to Odoo DB manager
New test for Apache Unomi MVEL RCE (CVE-2020-13942)
New test for Unrestricted access to Prometheus Interface
New test for Unrestricted access to Prometheus Metrics
New test for Unrestricted access to Golang expvar
New test for Unrestricted access to Node.js status-monitor page
New test for Unrestricted access to HAProxy stats page
New test for Unrestricted access to Nginx stub_status page
New test for Unrestricted access to Nginx nginx-module-vts status page
New test for Unrestricted access to Traefik Dashboard
New test for Unrestricted access to Kafka monitoring
New test for Unrestricted access to Netdata Dashboard
New test for Typo3 Admin publicly accessible
New test for Typo3 sensitive files
Updated WordPress Plugin checks
Updated Drupal core checks
New test for SonicWall SSL-VPN 8.0.0.0 RCE via ShellShock exploit
New test for Node.js Debugger Unauthorized Access Vulnerability
New test for Node.js Inspector Unauthorized Access Vulnerability
New test for Apache Shiro authentication bypass (CVE-2020-17523)
New test for Reflected Cross-Site Scripting (XSS) vulnerability in PAN-OS management web interface (CVE-2020-2036)
New test for Missing Authentication Check in SAP Solution Manager (CVE-2020-6207)
New test for VMware vCenter Server Unauthorized Remote Code Execution (CVE-2021-21972)
New test for Delve Debugger Unauthorized Access Vulnerability
New check for HTTP response splitting with cloud storage
New tests for WordPress plugins
New check for Hashicorp Consul API is accessible without authentication [https://www.consul.io/docs/security]
Multiple new checks for Unrestricted access to a monitoring system
Improvements to JavaScript Library Audit checks
New check for Cisco RV Series Authentication Bypass (CVE-2021-1472)
New check for ntopng Authentication Bypass (CVE-2021-28073)
New check for Agentejo Сockpit CMS resetpassword NoSQLi (CVE-2020-35847)
New check for AppWeb Authentication Bypass (CVE-2018-8715)
New check for Apache OFBiz SOAPService Deserialization RCE (CVE-2021-26295)
New check for F5 iControl REST unauthenticated remote command execution vulnerability (CVE-2021-22986)
New check for Python Debugger Unauthorized Access Vulnerability
New check for Virtual Host locations misconfiguration
New check for Request Smuggling
New check for SSRF via logo_uri in MITREid Connect (CVE-2021-26715)
New check for Oracle E-Business Suite Information Disclosure
New check for Unauthorized Access to a web app installer
New check for SAML Consumer Service XML entity injection (XXE)
New check for Grav CMS Unauthenticated RCE (CVE-2021-21425)
New check for Outsystems Upload Widget Arbitrary File Uploading (RPD-4310)
New check for Django Debug Toolbar
New check for Joomla Debug Console enabled
New check for Joomla J!Dump extension enabled
New check for Request Smuggling
New check for Unrestricted access to Caddy API interface
New check for Pyramid framework weak secret key
New check for Apache Tapestry Unauthenticated RCE (CVE-2019-0195 and CVE-2021-27850)
New check for Unrestricted access to Spring Eureka dashboard
New check for Unrestricted access to Yahei PHP Probe
New check for Unrestricted access to Envoy Dashboard
New check for Unrestricted access to Traefik2 Dashboard
New check for Dragonfly Arbitrary File Read/Write (CVE-2021-33564)
New check for Oracle E-Business Suite Frame Injection (CVE-2017-3528)
New check for Gitlab CI Lint SSRF
New check for Gitlab open user registration
New check for Gitlab user disclosure via GraphQL
```

### 0x05 参考链接：  
https://www.fahai.org/index.php/archives/126/  
https://www.fahai.org/index.php/archives/132/  
