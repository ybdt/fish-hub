墨者学院中的一道题，地址如下：  
https://www.mozhe.cn/bug/detail/WTNpdGxUS3l4dG9uMFF6ZEs3OEJCdz09bW96aGUmozhe  
在使用burp的intruder时，返回数据包中发现提示“ip违法”，进一步查看，请求的ip地址“128.0.0.2”中的“.”被编码，变为“128%2e0%2e0%2e2”  
解决方式：  
Intruder->Payloads->Payload Encoding中的“.”去掉

参考链接：  
https://nocbtm.github.io/2018/07/27/BurpSuit%20%E6%9A%B4%E5%8A%9B%E7%A0%B4%E8%A7%A3%E5%8F%A3%E4%BB%A4/
