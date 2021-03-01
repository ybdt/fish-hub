burp每次在新机器上安装的时候，都需要激活，故记录此文

首先执行密钥生成器：  
./jdk-11.0.7-for-linux/bin/java -jar ./burp-loader-keygen-2020_2_1.jar  
并拷贝显示的密钥

再通过载入器执行burp：  
./jdk-11.0.7-for-linux/bin/java -Dfile.encoding=utf-8 -noverify -javaagent:BurpSuiteLoader.jar -jar burpsuite_pro_v2020.5.1.jar  
选择“手动激活”，将上述拷贝的密钥粘贴到此处，此处会返回一个“激活响应”，将生成的“激活响应”拷贝到之前的密钥生成器界面处，激活完成

启动时，在“载入配置文件界面”选择配置文件，并勾选“Default to the above in the future”

启动后，选择Extender->Add，添加Extender文件夹下的burp扩展
