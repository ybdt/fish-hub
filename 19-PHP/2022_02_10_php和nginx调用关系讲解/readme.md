php和nginx中转是php-cgi.exe（php-cgi发展到现在变成php-fastcgi）

首先启动php-cgi.exe
```
php-cgi.exe -b 127.0.0.1:9999
```

nginx在配置文件中指定php-cgi监听的地址和端口
```
http {
    include       mime.types;
    default_type  application/octet-stream;

    server {
        listen       80;
        server_name  localhost;

		# Declares here, so that $document_root is able to find php files
		root www;
		
        location / {
            index  index.html index.htm;
        }

		# For PHP files, pass to 127.0.0.1:9999
		location ~ \.php$ {
			fastcgi_pass   127.0.0.1:9999;
			fastcgi_index  index.php;
			fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
			include        fastcgi_params;
		}

    }

}
```

nginx连接php-cgi，php-cgi调用php

参考链接：  
https://mkyong.com/nginx/nginx-php-on-windows/  
https://www.nginx.com/resources/wiki/start/topics/examples/phpfastcgionwindows/  