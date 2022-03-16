$_POST 与 php://input
```
1、仅在取值为application/x-www-data-urlencoded和multipart/form-data时(文件上传时)，php会将http请求body相应数据会填入到数组$_POST，填入到$_POST数组中的数据是进行urldecode()解析的结果。
2、只要Content-Type不为multipart/form-data，php://input会填入post数据。
3、仅当Content-Type为application/x-www-form-urlencoded且提交方法是POST方法时，$_POST数据与php://input数据才是一致的。
```

$HTTP_RAW_POST_DATA 与 php://input
```
1、php://input可以读取没有处理过的POST数据。相较于$HTTP_RAW_POST_DATA而言，它给内存带来的压力较小。
2、$HTTP_RAW_POST_DATA（This feature has been DEPRECATED as of PHP 5.6.0. 被废弃了，查看官方文档）
```

1、php://input可以读取http entity body中指定长度的值，由Content-Length指定长度，不管是POST方式或者GET方法提交过来的数据。但是，一般GET方法提交数据时，http request entity body部分都为空。  
2、php://input与$HTTP_RAW_POST_DATA读取的数据是一样的，都只读取Content-Type不为multipart/form-data的数据。  
3、Content-Type仅在取值为application/x-www-data-urlencoded和multipart/form-data两种情况下，PHP才会将http请求数据包中相应的数据填入全局变量$_POST  
4、PHP不能识别的Content-Type类型的时候，会将http请求包中相应的数据填入变量$HTTP_RAW_POST_DATA  
5、只有Coentent-Type为multipart/form-data的时候，PHP不会将http请求数据包中的相应数据填入php://input，否则其它情况都会。填入的长度，由Content-Length指定。  
6、只有Content-Type为application/x-www-data-urlencoded时，php://input数据才跟$_POST数据相一致。  
7、php://input数据总是跟$HTTP_RAW_POST_DATA相同，但是php://input比$HTTP_RAW_POST_DATA更奏效，且不需要特殊设置php.ini  
8、PHP会将PATH字段的query_path部分，填入全局变量$_GET。通常情况下，GET方法提交的http请求，body为空。

参考链接：  
https://www.php.net/manual/zh/wrappers.php.php  
https://www.jianshu.com/p/14f7d3e9b362  
https://xiaoxiami.gitbook.io/phper/shu-zu/shu-ru-liu-php-input
