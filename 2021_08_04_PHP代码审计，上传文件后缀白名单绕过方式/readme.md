如下代码段：上传后缀白名单，摘自通达OA
```
function check_filetype($s_name)
{
	$p = strrpos($s_name, ".");

	if ($p !== false) {
		$postfix = strtolower(substr($s_name, $p + 1));

		if (in_array($postfix, array("php", "exe", "js"))) {
			return false;
		}
	}

	return true;
}
```
如上只限制了php、exe、js，绕过方式：
```
php5或者php.或者php::$DATA
```
