# 0x01-Spring全家桶简介
Spring发展到现在，全家桶所包含的内容非常庞大，这里主要介绍其中关键的5个部分，分别是Spring Framework、 Spring Boot、 Spring Cloud、Spring Security、Spring MVC

其中的Spring Framework就是大家常常提到的Spring， 这是所有Spring内容最基本的底层架构，其包含Spring MVC、Spring Boot、Spring Core、IOC和AOP等等

Spring MVC就是Spring中的一个MVC框架，主要用来开发web应用和网络接口，但是其使用之前需要配置大量的xml文件，比较繁琐，所以出现Spring Boot，其内置tomcat并且内置默认的xml配置信息，从而方便了用户的使用

下图就直观表现了他们之间的关系  
![image](./image/01.jpg)  

# 0x02-Spring组件简介
Spring Security：主要是用来做鉴权，保证安全性的

Spring Cloud：基于Spring Boot，简化了分布式系统的开发，集成了服务发现、配置管理、消息总线、负载均衡、断路器、数据监控等各种服务治理能力

Spring Websocket：Spring内置的简单消息代理，这个代理处理来自客户端的订阅请求，将它们存储在内存中，并将消息广播到具有匹配目标的连接客户端

Spring Data：是一个用于简化数据库访问，并支持云服务的开源框架，其主要目标是使数据库的访问变得方便快捷

Spring Data Commons：是Spring Data下所有子项目共享的基础框架，Spring Data家族中的所有实现都是基于Spring Data Commons

Spring Data REST：是把我们需要编写的大量REST模版接口做了自动化实现，并符合HAL的规范

Spring Web Flow：是Spring MVC的扩展，它支持开发基于流程的应用程序，可以将流程的定义和实现流程行为的类和视图分离开来

# 0x03-Spring SpEL表达式简介

# 0x04-Sprig 历史漏洞
```
漏洞名称                             漏洞编号            影响版本                              披漏日期
Spring Websocket 远程代码执行漏洞    CVE-2018-1270       Spring Framework 5.0 - 5.0.5          2018/4/5
                                                        Spring Framework 4.3 - 4.3.15
Spring Data 远程代码执行漏洞         CVE-2018-1273       Spring Data Commons 1.13 - 1.13.10    2018/4/10
                                                        Spring Data REST 2.6 - 2.6.10
                                                        Spring Data Commons 2.0 - 2.0.5
                                                        Spring Data REST 3.0 - 3.0.5
Spring Boot 远程代码执行漏洞          CNVD-2016-04742    SpringBoot 1.1.0-1.1.12               2016/7/15
                                                        SpringBoot 1.2.0-1.2.7
                                                        SpringBoot 1.3.0
Spring Data REST 远程代码执行漏洞    CVE-2017-8046       Spring Data REST prior to 3.0.1       2017/9/21
                                                        Spring Boot versions prior to 1.5.9
                                                        Spring Data REST prior to 2.6.9
Spring Web Flow 远程代码执行漏洞     CVE-2017-4971       Spring Web Flow 2.4.0 - 2.4.4         2017/5/31
                                                        Spring Web Flow 2.4.4 - 2.4.8
Spring Boot 远程代码执行漏洞          CNVD-2019-11630    Spring Boot 1-1.4                     2019/4/22
                                                        Spring Boot 2.x 
```

# 参考链接
https://paper.seebug.org/1422/  