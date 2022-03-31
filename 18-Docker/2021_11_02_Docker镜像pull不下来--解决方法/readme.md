docker pull bodsch/docker-jolokia  
报错：Get https://registry-1.docker.io/v2/: net/http: request canceled while waiting  

### 第1步
添加8.8.8.8到/etc/resolv.conf  
### 第2步
dig @8.8.8.8 registry-1.docker.io  
添加解析后的其中一个ip到/etc/hosts中  
### 第3步
/etc/docker/daemon.json
```
{
  "registry-mirrors": ["https://bbj143ni.mirror.aliyuncs.com", "http://hub-mirror.c.163.com", "https://registry.docker-cn.com", "https://docker.mirrors.ustc.edu.cn"]
}
```

### 参考链接
https://www.codenong.com/cs106532452/  
https://stackoverflow.com/questions/60766682/docker-error-response-from-daemon-get-https-registry-1-docker-io-v2-net-ht  
