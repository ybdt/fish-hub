1、当通过命令执行漏洞在一台无法获知系统具体类型的*nix系统上拿到命令执行权限，想要查看ip地址，但是ifconfig、ip addr都无效时，可执行netstat -antup，从输出中查看ip地址出现最多的即为本机ip

2、测试*nix系统下有哪些可用于下载的工具
```
curl -V
wget -V
ftp -h
perl --version
python --version
ruby --version
```
