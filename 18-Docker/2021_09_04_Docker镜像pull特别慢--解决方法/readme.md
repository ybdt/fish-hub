在公司pull docker镜像，pull的超级慢，遂有此篇记录

### Ubuntu下
/etc/docker/daemon.json  
```
{
  "registry-mirrors": ["https://bbj143ni.mirror.aliyuncs.com", "http://hub-mirror.c.163.com", "https://registry.docker-cn.com", "https://docker.mirrors.ustc.edu.cn"]
}
```
需要注意，ubuntu下默认没有/etc/docker/daemon.json这个文件，centos下默认有这个文件  

### Windows下
针对安装了Docker for Windows的用户，您可以参考以下配置步骤：  
在系统右下角托盘图标内右键菜单选择 Settings，打开配置窗口后左侧导航菜单选择 Docker Daemon。编辑窗口内的JSON串，填写下方加速器地址：  
```
{
  "registry-mirrors": ["https://bbj143ni.mirror.aliyuncs.com"]
}
```
编辑完成后点击 Apply 保存按钮，等待Docker重启并应用配置的镜像加速器。  

### 参考链接
阿里云[https://cn.aliyun.com/](https://cn.aliyun.com/)->登录->搜索“容器镜像服务”->左侧导航栏中镜像工具->镜像加速器  
https://www.cnblogs.com/nhdlb/p/12567154.html -> Docker：docker国内镜像加速  