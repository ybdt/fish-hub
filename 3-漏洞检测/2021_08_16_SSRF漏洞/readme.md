https://portswigger.net/web-security/ssrf

SSRF漏洞原理：诱导服务端应用程序发起http请求到任何攻击者指定的地址

SSRF漏洞危害1：绕过本地服务端验证
对应利用方式：直接访问http://localhost/admin/
基于场景1：访问控制是独立于应用服务器，且位于应用服务器前端的一个模块
基于场景2：基于故障恢复考虑，从回环网卡发起的请求不需要验证
基于场景3：
（没明白）The administrative interface might be listening on a different port number than the main application, and so might not be reachable directly by users.

SSRF漏洞危害2：绕过后端服务端验证
对应利用方式：先扫描C段开放80、8080的ip，再访问http://ip:port/admin/


SSRF防护1：基于黑名单的过滤器
绕过思路1：尝试大小写和URL编码（有疑问，URL解码是在过滤器之前进行的吗？）
绕过思路2：尝试127.0.0.1的替代形式，如127.1、2130706433、017700000001、169.xxx.xxx.xxx
绕过思路3：注册自己的域名，指向127.0.0.1