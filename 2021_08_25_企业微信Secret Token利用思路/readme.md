### 1、利用前提
需要拿到如下信息
```
<add name="CorpId" connectionString="wxxxxxxxxxxxx" />
<add name="CorpSecret" connectionString="xxxxxxxxxxx" />
<add name="CorpToken" connectionString="xxxxxxxxxx" />
```
### 2、利用过程
1、传入获取到的id和secrect到如下的API地址，可获取AccessToken  
```
https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=id&corpsecret=secrect
```
2、企微中会分为一个个的部分，通过企微的API我们可以获取到企业的架构和部门ID，这个在添加成员的时候用的到，在如下API中查询ak权限，就能查询到部门名称以及部门ID  
```
https://open.work.weixin.qq.com/devtool/query?e=301002
```
3、向如下API  
```
https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
```
传入如下信息  
```
{
   "userid": "zhangsan",
   "name": "张三",
   "department": [6],
   "mobile":"1388888888"
}
```
调用成功后，即可通过手机号登录目标企业的企业微信。  
### 3、参考连接
https://mp.weixin.qq.com/s/LMZVcZk7_1r_kOKRau5tAg  
https://qydev.weixin.qq.com/wiki/index.php?title=%E7%AE%A1%E7%90%86%E6%88%90%E5%91%98#.E6.9B.B4.E6.96.B0.E6.88.90.E5.91.98  
