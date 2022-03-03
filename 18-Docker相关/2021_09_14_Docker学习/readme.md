### 1、docker部署CTF题目
最简单的方式：下载别人的docker镜像，修改后打包成tar包  
参考链接：  
1、https://blog.csdn.net/q20010619/article/details/108587879  
2、https://www.v0n.top/2020/05/01/如何正确使用Docker出一道CTF题目/  
3、https://jwt1399.top/posts/50751.html  

### 2、docker镜像加速
参考链接：https://www.cnblogs.com/nhdlb/p/12567154.html  

### 3、使用Dockerfile快速创建docker环境
原理：将“下载别人的docker镜像”、“修改镜像”等动作写入Dockerfile文件中  
参考链接：https://blooddark.github.io/blog/docker/3.html  

### 4、docker中export和save的区别
export类似于创建快照，导出后，直接import即可使用，不需要做任何修改，缺点是文件体积较大  
save保存后是镜像，需要结合Dockerfile配置镜像，以及拷贝需要的文件，优点是文件体积较小  

### 5、构建自己的镜像
说明：即使想构建全新的镜像，也要基于官方的空镜像
参考连接：  
1、https://itbilu.com/linux/docker/E1-k4FW_M.html  
2、https://cloud.tencent.com/developer/article/1367035  

常用命令：
```
#1、搜索包含指定名字的镜像
docker search lamp

#2、下载镜像到本地
docker pull tutum/lamp

#3、查看本地的镜像
docker images

#4|查看全部的（包括启动和未启动的）容器
docker ps -a

#启动容器，其中-p选项，主机端口:容器端口
docker run --name 容器名 -d -p 8080:8080 -p 22222:22222 镜像名

#进入容器
docker exec -it 容器名 /bin/bash

#开始容器
docker start 容器id
#停止容器
docker stop 容器id

#删除容器
docker rm 容器名/容器id
#删除镜像
docker rmi 镜像名/镜像id

#保存镜像
docker save nginx:v1 > ./nginx_v1.tar
#载入镜像
docker load < ./nginx_v1.tar

#导出容器
docker export lamp > /home/ybdt/Desktop/ctf1.tar
#导入容器
docker import ./ctf1.tar ctf1
#导入后运行
docker run --name ctf-1-c -d -p 10001:80 -p 23306:3306 ctf-1 /run.sh
参考连接：https://www.cnblogs.com/wish123/p/6573899.html

#基于Dockerfile构建镜像
mkdir mynginx
cd ./mynginx
vim ./Dockerfile
docker build -t nginx:v1 .

#基于commit创建新镜像
docker commit 容器名 镜像名

#查看容器启动命令
docker inspect drupal_8.5.0
#其中开头部分的path即为command，如："Path": "docker-php-entrypoint",

#查看内置的mysql密码
docker logs lamp
```
