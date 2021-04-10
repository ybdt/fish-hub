1、array_walk_recursive特性
```
<?php

class Y {
    public function test($value, $key) {
        echo $value."and";
        echo $key;
    }
}

$y = new Y();
$arr = array("jing", "xin");
array_walk_recursive($arr, '$y->test');#此种调用无效，理论解释暂无，经过测试确实如此
array_walk_recursive($arr, 'Y::test');#此种调用才有效
```

2、宽字节注入特性
```
目标使用addslashes进行防护时，如果数据库使用的字符集不是UTF-8，需考虑是否存在宽字节注入，宽字节注入不仅限于GBK，还可以是GB2312等
```

3、过滤单引号
```
使用16进制代替字符串
```
参考链接：  
https://xz.aliyun.com/t/9367
