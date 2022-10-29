参考链接：  
https://www.php.net/manual/zh/function.intval.php  
https://www.php.net/manual/zh/language.types.integer.php#language.types.integer.casting

用法：
```
$var = "abc";
$var = intval($var);
```

定义：  
将（整数、浮点数、字符串、数组、对象、布尔值、null）值转换为整数  
空数组返回0，非空数组返回1  
对象抛出E_NOTICE 错误并返回1  
false返回0，true返回1  
字符串为数字或前导数字时，转换为相应的整数，否则为0  
null转换为0

适用于php版本4、5、7、8

注意：  
无

```
echo intval(420000000000000000000);   // 0
echo intval(42, 8);                   // 42
echo intval('42', 8);                 // 34
上述3个不懂为什么
```