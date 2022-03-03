参考链接：  
https://www.php.net/manual/zh/function.isset.php

用法：
```
if isset($var) {
    echo "$var has been set and value is not null"
}
```

定义：  
判断（一个或多个）变量是否被声明且值不为null

适用于php版本4、5、7、8

注意：  
无

```
<?php
$a = "";
if ( isset($a) ) {
    echo "'' value is true";
}
else {
    echo "'' value is false";
}

echo "<br>";

$b = null;
if ( isset($b) ) {
    echo "null variable is true";
}
else {
    echo "null variable is false";
}

echo "<br>";

$c = "\0";
if ( isset($c) ) {
    echo "null value is true";
}
else {
    echo "null value is false";
}   
```