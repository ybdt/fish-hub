参考链接：  
https://www.php.cn/dic/php/stripcslashes.html  
https://www.php.cn/dic/php/addcslashes.html

用法：
```
echo addcslashes("abc", "b"); // a\bc
echo stripcslashes("a\bc"); // abc
```

定义：  
为字符串添加反斜线、去掉字符串添加的反斜线

适用于php版本4、5、7、8

注意：  
无