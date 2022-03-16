# 01-php session概念
```
服务端创建的一个东西（文件），保存在服务端，用于跟踪用户会话

客户端提交session值，可以是在cookie中提交，如：
Cookie: PHPSESSID=og6pv0a6qf5hca32gjdhklggn4; USER_NAME_COOKIE=admin; OA_USER_ID=admin; SID_1=e1ac5c7b; LOGIN_UID=1
对应的服务端获取：
if ( ($_SESSION["LOGIN_USER_ID"] == "") || ($_SESSION["LOGIN_UID"] == "") ) {

参考链接：
https://blog.csdn.net/weixin_39904587/article/details/111005741
```