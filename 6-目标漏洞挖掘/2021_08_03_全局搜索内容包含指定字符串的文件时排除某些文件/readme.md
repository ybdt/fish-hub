当全局搜索使用指定函数的文件，结果出现大量无关文件时，可考虑使用此技巧

使用工具：VSCode v1.58.2  
文件->首选项->设置，如下图  
![image](./pic/1.png)  
在用户类别下，文本编辑器->文件，如下图  
![image](./pic/2.png)  
下拉到Exclude处，当想排除全部的js文件时，添加  
```
**/*.js
```
如下图  
![image](./pic/3.png)  

参考链接：  
https://blog.csdn.net/ArisKing/article/details/84038430
