参考链接：  
https://www.php.net/manual/zh/function.strpos.php

用法：
```
if ( strpos("abc", "a") ) {
    echo "return 0"
}
```

定义：  
返回第2个参数在第1个参数中首次出现的位置，位置从0开始计数，没找到返回false

适用于php版本4、5、7、8

注意：  
用到strpos函数需要关注是否使用===或!==，否则可能会有意外结果，就像下述第一个例子一样

```
<?php
if (strpos("abc", "b") ) {
    echo "strpos('abc', 'b') return pos";
}
else {
    echo "strpos('abc', 'b') return false";
}

echo "<br>";

if (strpos("abc", "a") ) {
    echo "strpos('abc', 'a') return pos";
}
else {
    echo "strpos('abc', 'a') return false";
}

echo "<br>";

if (strpos("abc", "d") ) {
    echo "strpos('abc', 'd') return pos";
}
else {
    echo "strpos('abc', 'd') return false";
}
```