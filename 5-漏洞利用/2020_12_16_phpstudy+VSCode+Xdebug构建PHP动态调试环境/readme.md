# 0x00 php环境搭建
安装phpstudy、vscode、kkcms

# 0x01 下载xdebug
从[https://xdebug.org/download/historical](https://xdebug.org/download/historical)下载符合当前环境的xdebug  
当前环境可从phpinfo中查看，下图展示了当前的php.exe是32位还是64位、Zend扩展版本、PHP扩展版本  
![image](./pic/0.png)  
将下载下来的php_xdebug-2.5.5-5.6-vc11-nts.dll放到php的扩展目录下，即php对应的ext文件夹下，我这里是C:\phpStudy\PHPTutorial\php\php-5.6.27-nts\ext下

# 0x02 配置xdebug  
在php.ini文件末尾中添加如下部分
```
[XDebug]
zend_extension = php_xdebug-2.5.5-5.6-vc11-nts-x86_64.dll ; 如果没将php_xdebug-2.5.5-5.6-vc11-nts.dll放到ext目录下，需要指定全路径
xdebug.remote_enable = 1 ; 开启远程调试功能
xdebug.remote_autostart = 1 ; 这个配置是比较重要的一个配置
xdebug.remote_port = "9000" ; 默认端口号是9000
```
重启环境，重新打印phpinfo()，如果phpinfo()中带有xdebug部分，则安装成功，如下所示  
![image](./pic/1.png)

# 0x03 配置vscode
进入扩展，搜索“php debug”，选择发布者为“Robert Lu”的PHP Debug（发布者为“Robert Lu”的PHP Debug相比发布者为“Felix Becker”的PHP Debug，多了一个运行时改变变量值的功能）  
进入调试，点击“create a launch.json file”，如下图  
![image](./pic/2.png)  
点击后会生成一个配置文件，此时可通过vscode动态调试kkcms
