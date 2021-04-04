#### 代码审计时
如果是需要回显的漏洞，则需要寻找是否有回显的代码，如任意文件读取  
如果是不需要回显的漏洞，则直接查看过滤代码即可，如SSRF、SQL盲注，等

#### 使用grep进行php代码审计，包含7种常见的web漏洞：命令执行、代码执行、SQLi、XSS、远程/本地文件包含、目录遍历、杂项
https://github.com/dustyfresh/PHP-vulnerability-audit-cheatsheet
