如何发现Spring Boot Actuator的/env等未授权访问漏洞，可尝试发现mysql密码信息，具体如下
```
尝试下载heapdump
用工具Eclipse Memory Analyzer（MAT）（下载地址：https://www.eclipse.org/mat/downloads.php）加载文件
获取配置信息：select * from org.springframework.web.context.support.StandardServletEnvironment
通过字符串匹配查找用户session：select * from java.lang.String s WHERE toString(s) LIKE ".SESSION."
也可通过模糊搜索，寻找密码信息：
```
![image](./pic/1.png)  
![image](./pic/2.png)  
