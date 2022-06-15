AWVS版本发布：[https://www.acunetix.com/support/build-history/](https://www.acunetix.com/support/build-history/)

AWVS最新版可使用其他师傅打包好的docker镜像，感谢这些师傅：），地址：[https://hub.docker.com/r/secfa/awvs](https://hub.docker.com/r/secfa/awvs)

docker安装问题可参考：[https://github.com/ybdt/front-hub/tree/main/13-Docker](https://github.com/ybdt/front-hub/tree/main/13-Docker)

之前破解AWVS的方式是改host什么的，可是对于最新版14.7.220401065，各种方式都尝试了均不行，最后发现通过docker安装别人破解好的是可行的，还得是docker啊（多亏各位爱分享的师傅）

使用经验1：  
若收集的url结尾是http://www.xxx.com/index.php?login.do ，不是http://www.baidu.com 或 http://www.baidu.com/ 或 http://www.baidu.com/pinyin/ ，AWVS会提示检验错误，可使用脚本beijixing-to-awvs-auxiliary.py处理一下

使用经验2：  
默认情况下，一次最多扫描100个目标，想要扫描超过100个目标，可通过AWVS中的分组，创建一个组，将目标添加到组中，我这边将452个目标分为2个组，然后将2个组同时扫描，452个目标在8核14G的配置下，扫描耗时约8h

使用经验3：  
导入1000个目标会提示校验失败，导入500个不会提示

使用经验4：  
windows下通过docker跑，资源占用特别高，导致特别卡，还是要迁移到linux下