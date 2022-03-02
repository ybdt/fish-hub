### 实战下来最有效的还是增加发送延时
```
--scan-delay 500ms
```
### 其他IPS绕过方式
1、数据包分片
```
-f; --mtu <val>: fragment packets (optionally w/given MTU)

nmap --mtu 16 192.168.1.1
需要注意：--mtu的值需要是8的整数倍，以及太小的话有些路由会丢弃
```
2、附加随机16进制字符串
```
--data <hex string>: Append a custom payload to sent packets

nmap --data 79626474
需要注意：不能结合其他两个--data选项一起使用
```
3、附加随机ASCII字符串
```
--data-string <string>: Append a custom ASCII string to sent packets

nmap --data-string "ybdt"
需要注意：不能结合其他两个--data选项一起使用
```
4、附加随机数据
```
--data-length <num>: Append random data to sent packets

nmap --data-length 25 192.168.1.1
需要注意：不能结合其他两个--data选项一起使用
```
5、随机顺序
```
nmap命令帮助中没看到此选项

nmap --randomize-hosts 192.168.1.1
```
6、诱饵扫描（使用会报错）
```
-D <decoy1,decoy2[,ME],...>: Cloak a scan with decoys

nmap –D RND:10 192.168.1.1
或
nmap –D 100.100.100.100,200.200.200.200 192.168.1.1
```

7、空闲扫描（使用会报错）
```
nmap命令帮助中没看到此选项

nmap –P0 -sI zombie(僵尸) 192.168.1.1
```

参考链接：  
http://www.safe6.cn/article/41  
https://www.freebuf.com/articles/system/233678.html  
http://www.2cto.com/article/201604/498533.html  
