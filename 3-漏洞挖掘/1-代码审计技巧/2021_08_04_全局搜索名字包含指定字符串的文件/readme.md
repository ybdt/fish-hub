当碰到内容很大的项目，例如通达OA项目达500多M，使用Seay源代码审计系统会卡死，使用fortify也半天没有反应，考虑直接定位敏感文件，可使用此技巧

借助everything，下载地址：https://www.voidtools.com/zh-cn/

在地址栏输入如下指令，即可搜索C:\Users\ybdt\Desktop\webroot\目录及其子目录下全部名字包含upload的php文件
```
C:\Users\ybdt\Desktop\webroot\ *upload*.php
```
如下图  
![image](./pic/1.png)  
可使用everything的导出功能：文件->导出  
导出后配合脚本copy_file_to_dst.py可批量将目标文件拷贝到桌面下的upload文件夹下，如下图  
![image](./pic/2.png)  
