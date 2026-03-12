# 01-Information-Gather
```
```

# 02-Gateway-Evasion-And-File-Masquerade
```
https://filesec.io/
https://www.wietzebeukema.nl/blog/trust-me-im-a-shortcut
https://github.com/wietze/lnk-it-up
https://github.com/Matmaus/LnkParse3
```

# 03-Click-Masquerade
```
```


# 01-案例学习
```
【红蓝对抗：钓鱼演练资源汇总&备忘录】https://github.com/tib36/PhishingBook
【实战｜记一次企业钓鱼演练】https://mp.weixin.qq.com/s/4ilYuK7jbg5xfU2l3x1Sbw
【记一次钓鱼邮件演练】https://mp.weixin.qq.com/s/R5zvtEKvxQdXLpP4tI9opQ
【邮件钓鱼新思路】https://mp.weixin.qq.com/s/a4nqyKPzACYbsJAIqDrgow
【干货 | 红队渗透中钓鱼tips总结】https://mp.weixin.qq.com/s/RDvakryfe_5oQ656AVIJsA
【钓鱼邮件（上）】https://mp.weixin.qq.com/s/YR6DFvDAP_gn96K3zaQtAQ

# LNK钓鱼
    https://mp.weixin.qq.com/s/-sGRCSoOxP2a9aR0vNoZVw

    https://www.cybereason.com/blog/threat-analysis-taking-shortcuts-using-lnk-files-for-initial-infection-and-persistence

    https://github.com/Maldev-Academy/ExecutePeFromPngViaLNK


# SVG钓鱼
    钓鱼邮件中通过SVG附件，来钓Victim的凭证
    https://www.seqrite.com/blog/unmasking-the-svg-threat-how-hackers-use-vector-graphics-for-phishing-attacks/


https://mp.weixin.qq.com/s/OrIb-yXj2wMd5LF9kAbjsw【浅谈钓鱼捆绑技术--coleak】
https://mp.weixin.qq.com/s/_bD_-MbNujn6P_y18xUk0g【黑客(红队)攻防中内网利用chm文件进行getshell上线--Flowers aq】

https://redsiege.com/blog/2024/04/sshishing-abusing-shortcut-files-and-the-windows-ssh-client-for-initial-access/
```

# 02-PC端钓鱼
```
0x01 图标
    1.1 前言
        可通过BeCyIconGrabber抓取图标，下载地址：https://jarlpenguin.github.io/BeCyIconGrabberPortable/
        也可通过iconsext抓取图标，下载地址：https://www.nirsoft.net/utils/iconsext.html
        抓取后，通过ResourceHacker替换图标，下载地址：http://www.angusj.com/resourcehacker/
        CS生成的马不能使用ResourceHacker修改图标，可通过Restorator修改图标
        Restorator下载地址：https://www.sqlsec.com/tools.html

0x02 图标 + 偏门PE后缀
    2.1 前言
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


0x03 图标 + LNK
    3.1 前言
    3.2 BAT
    3.3 PowerShell
    3.4 FTP
        

0x04 CHM钓鱼
    4.1 前言

0x05 HTA钓鱼
    5.1 前言

0x06 Office宏
    6.1 前言
        由于世界各国都在推广自己国家的Office套件，研究MS Office宏钓鱼并不能应用到WPS Office中，所以不那么流行

0x07 文档解析器0day
    MS Office的0day、WPS Office的0day、各种PDF阅读器的0day

    7.1 参考文章
        https://mp.weixin.qq.com/s/QxiBbSRdfKvEwhKDeCx2LQ
        https://github.com/George-boop-svg/Chinese-hackers-use-WPS-to-attack
        https://www.welivesecurity.com/en/eset-research/analysis-of-two-arbitrary-code-execution-vulnerabilities-affecting-wps-office/
```

# 03-凭证钓鱼
```
社交平台
https://www.whatsapp.com/
https://www.instagram.com/
https://www.linkedin.com/
https://www.facebook.com/
https://x.com/
https://maimai.cn/
https://telegram.org/
https://github.com/
https://www.4shared.com/

https://www.smtp2go.com/

【A Domain Name & Email Address Collection Tool】https://github.com/bit4woo/teemo
【Python在线验证邮箱真实性，支持批量验证】https://github.com/Tzeross/verifyemail


之前测试，spf欺骗可以将邮件发送到qq邮箱的收件箱中

【SMTP 邮件伪造发送钓鱼邮件】https://mp.weixin.qq.com/s/ra750vDMFKcVcLPWYni3ow?poc_token=HDn3_mejtxTj3GaQKiI4KmrEq8W30i1vQxbp_Qxj
【邮件安全之发件人伪造】https://anchorety.github.io/2020/10/18/邮件安全之发件人伪造/
【Validate_email verify if an email address is valid and really exists】https://github.com/syrusakbary/validate_email



01、针对vps厂商封禁25端口的问题，可在本地部署，然后通过frp转发到vps的其他端口
02、多换一换映射的ip和域名，不然容易被拦截
03、速度调慢一些，不然容易被拦截
```