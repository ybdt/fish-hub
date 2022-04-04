### ubuntu20.04安装步骤
```
root用户登录
apt update && apt upgrade # 更新源、更新软件
apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common # 允许apt从https源获取包
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - # 添加gpg密钥
apt-key fingerprint 0EBFCD88 # 验证gpg密钥
add-apt-repository "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable" # 添加源
apt update
apt install docker-ce docker-ce-cli containerd.io
配置一下镜像加速

参考链接：
ubuntu 20.04 LTS 安装docker -> https://www.1024sou.com/article/440450.html
Ubuntu20安装Docker详细步骤 -> https://blog.csdn.net/qq_36335426/article/details/111308213
```