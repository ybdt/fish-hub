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
