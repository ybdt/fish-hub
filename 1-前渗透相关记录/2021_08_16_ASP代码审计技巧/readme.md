# ASP知识点补充
1、使用语言VBScript，VBScript可以看作是Visual Basic的简化版  
2、结尾不能有分号，否则报错
```
Microsoft VBScript 编译器错误 错误 '800a0401'

语句未结束
```
3、VBScript中单引号是注释符，想要表示单引号，需要在双引号中，因此，双引号中的单引号不作为注释符  
4、VBScript中，想要表示双引号，需要连续的两个双引号，如下所示
```
reponse.write "hello"", ybdt!"
输出为
hello", ybdt!
```
参考链接：  
https://bbs.csdn.net/topics/30425539  
5、Access中如何执行SQL语句
```
点击对象中的查询->双击“在设计视图创建查询”，点击关闭->在空白处点击右键，选择SQL视图->输入SQL语句，点击上面的红色叹号执行
```
参考链接：  
https://blog.csdn.net/asanscape/article/details/18228273
