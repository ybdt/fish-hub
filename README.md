# 0x01 案例学习
```
【红蓝对抗：钓鱼演练资源汇总&备忘录】https://github.com/tib36/PhishingBook
【实战｜记一次企业钓鱼演练】https://mp.weixin.qq.com/s/4ilYuK7jbg5xfU2l3x1Sbw
【记一次钓鱼邮件演练】https://mp.weixin.qq.com/s/R5zvtEKvxQdXLpP4tI9opQ
【邮件钓鱼新思路】https://mp.weixin.qq.com/s/a4nqyKPzACYbsJAIqDrgow
【干货 | 红队渗透中钓鱼tips总结】https://mp.weixin.qq.com/s/RDvakryfe_5oQ656AVIJsA
【钓鱼邮件（上）】https://mp.weixin.qq.com/s/YR6DFvDAP_gn96K3zaQtAQ
```

# 0x02 经验技巧
```
01、针对vps厂商封禁25端口的问题，可在本地部署，然后通过frp转发到vps的其他端口
02、多换一换映射的ip和域名，不然容易被拦截
03、速度调慢一些，不然容易被拦截
```

# 0x03 邮箱收集及校验
```
【A Domain Name & Email Address Collection Tool】https://github.com/bit4woo/teemo
【Python在线验证邮箱真实性，支持批量验证】https://github.com/Tzeross/verifyemail
```

# 0x04 邮箱伪造
```
之前测试，spf欺骗可以将邮件发送到qq邮箱的收件箱中

【SMTP 邮件伪造发送钓鱼邮件】https://mp.weixin.qq.com/s/ra750vDMFKcVcLPWYni3ow?poc_token=HDn3_mejtxTj3GaQKiI4KmrEq8W30i1vQxbp_Qxj
【邮件安全之发件人伪造】https://anchorety.github.io/2020/10/18/邮件安全之发件人伪造/
【Validate_email verify if an email address is valid and really exists】https://github.com/syrusakbary/validate_email
```

# 0x05 后缀伪造
```
# RLO
RLO反转字符，可将zip.exe反转为exe.piz
经测试，会被360和Defender查杀

# SCR
可执行文件其他后缀scr，利用scr+RLO反转字符，将xcod.scr反转成rcs.docx
scr是windows下屏幕保护程序的后缀，是可执行的
windows下将exe文件后缀改为scr仍然可以执行，对于多数人来说会起到一定的迷惑性
更改后缀为scr -> 会被360查杀，Defender会延迟查杀（提示报毒仍能上线）
更改后缀为scr+文件名反装 -> 这个技术会被360和Defender查杀

# PIF
后缀为pif的文件在windows下也可执行，注意会有快捷方式的箭头
经测试，会被360和Defender查杀
```

# 0x06 图标伪装
```
可通过BeCyIconGrabber抓取图标，下载地址：https://jarlpenguin.github.io/BeCyIconGrabberPortable/
也可通过iconsext抓取图标，下载地址：https://www.nirsoft.net/utils/iconsext.html
抓取后，通过ResourceHacker替换图标，下载地址：http://www.angusj.com/resourcehacker/

CS生成的马不能使用ResourceHacker修改图标，可通过Restorator修改图标
Restorator下载地址：https://www.sqlsec.com/tools.html
```

# 0x07 OA挂马
```
# 通达OA
CSS路径：D:\MYOA\webroot\static\theme\9\ipanel.css
JS路径：D:\MYOA\webroot\static\js\ba\agent.js

# 泛微OA
CSS路径：D:\WEAVER\ecology\cloudstore\dev\init.css
JS路径：D:\WEAVER\ecology\js\timeZone\timeZone.js

# 万户OA
CSS路径：d:\jboss\jboss-as\server\oa\deploy\defaultroot.war\scripts\desktop\popwin.css
JS路径：d:\jboss\jboss-as\server\oa\deploy\defaultroot.war\desktop.jsp
上面的JS是在JSP页面中插入<script>代码块，所以需要在</body>标签前面插入
```