调试环境：apache + mysql + vscode + xdebug

解决方案：  
在httpd.conf的最后增加
```
FcgidIOTimeout 6000#seconds
FcgidConnectTimeout 60#seconds
```

参考链接：  
https://stackoverflow.com/questions/33561552/phpstorm-xdebug-interrupts-after-a-while-with-500-internal-server-error  
https://zend18.zendesk.com/hc/en-us/articles/204110723-A-Server-Error-Appears-During-a-Long-Debug-Session  
https://httpd.apache.org/mod_fcgid/mod/mod_fcgid.html  
https://httpd.apache.org/mod_fcgid/mod/mod_fcgid.html#fcgidiotimeout  
https://httpd.apache.org/mod_fcgid/mod/mod_fcgid.html#fcgidconnecttimeout
