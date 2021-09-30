php中序列化与反序列化分别对应函数serialize() 和unserialize()

## serialize()
当在php中创建一个对象或数组后，可以通过serialize()将这个对象或数组序列化成一个字符串，方便之后的传递与使用，测试代码如下
```
<?php
class ybdt {
    private $a = "aaa";
    protected $b = "bbb";
    public $c = "ccc";

    public function foo() {
        echo "function foo";
    }
}
$obj = new ybdt();

print_r("Below is the original string of object: " . "<br>");
print_r($obj);
print_r("<br>");

print_r("<br>");

$obj_ser = serialize($obj);
print_r("Below is the serialized string of object: " . "<br>");
print_r($obj_ser . "<br>");

print_r("<br>");

$arr = array("aaa", "bbb");

print_r("Below is the original string of array: " . "<br>");
print_r($arr . "<br>");

print_r("<br>");

$arr_ser = serialize($arr);
print_r("Below is the serialized string of array: " . "<br>");
print_r($arr_ser . "<br>");
?>
```

结果如下图  
![image](./0.png)

解释如下：
```
O:4:"ybdt":3:{s:7:"ybdta";s:3:"aaa";s:4:"*b";s:3:"bbb";s:1:"c";s:3:"ccc";}
其中
O表示：这是一个对象序列化后的字符串（a表示这是一个数组序列化后的字符串，见上图）
4表示：对象名长度是4个字节
"ybdt"表示：对象名即类名
3表示：对象中有3个元素
第1个元素的键值对：键是字符串类型，private属性序列化的时候格式是%00类型%00成员名，所以长度是7个字节，所以名字是"ybdta"
第2个元素的键值对：键是字符串类型，protected属性序列化的时候格式是%00*%00成员名，所以长度是4个字节，所以名字是"*b"
第3个元素的键值对：键是字符串类型，public属性序列化后就是正常的形式
```

## unserialize()
与serialize()对应的，unserialize()可以从已存储的表示中创建PHP的值，这是官方的介绍，简单说，就是从序列化后的字符串恢复对象、数组，测试代码如下
```
<?php
class ybdt {
    public $test = "123";
}

$obj_ser = 'O:4:"ybdt":1:{s:4:"test";s:3:"123";}';

print_r("Below is the serialized object: " . "<br>");
print_r($obj_ser . "<br>");

print_r("<br>");

$obj_unser = unserialize($obj_ser);
print_r("Below is the unserialized object: " . "<br>");
print_r($obj_unser);
print_r("<br>");

print_r("<br>");

$arr_ser = 'a:2:{i:0;s:3:"aaa";i:1;s:3:"bbb";}';

print_r("Below is the serialized array: " . "<br>");
print_r($arr_ser . "<br>");

print_r("<br>");

$arr_unser = unserialize($arr_ser);
print_r("Below is the unserialized array: " . "<br>");
print_r($arr_unser . "<br>");
?>
```

结果如下图  
![image](./1.png)

说明如下：
```
1、经测试，如果当前php文件中没有类ybdt的定义，直接对序列化后的字符串进行反序列化，会提示“__PHP_Incomplete_Class Object ...”
2、经测试，当类定义中出现protected或private类型的属性时，反序列化时返回空值
```
