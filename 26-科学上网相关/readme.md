先说一句，搞定之后，相比之前能更稳定的科学上网，好舒服~

# 0x01 服务器选择
服务器开启bbr plus加速：https://github.com/Chikage0o0/Linux-NetSpeed  
经测评，linux内核5.5以上自带的bbr速度最佳，我这边使用ubuntu20.04.4，内核5.11.0

# 0x02 域名购买
namesilo购买域名，选择偏门域名，基本多是0.99$  
将域名添加到cloudflare后，将namesilo的dns改为cloudflare提供的dns  

# 0x03 安装trojan-go
使用一键安装脚本：https://github.com/Jrohy/trojan  
参考：https://5best1s.com/trojan-go/  
备份：./bak/超便宜的VPS上安装Trojan-Go，配合使用CDN+Websocket，保护VPS永不被墙 _ 5BestOnes.html  

# 0x04 其他
上述配置完后，需要注意的是：  
01、开启cloudflare的CND后，由于每次连接的节点不同导致网络速度会不稳定，我这边选择关闭cloudflare的CDN  
02、文中提到的客户端Trojan-QT5安装完启动后会报错，我这边用的是QV2RAY，具体配置方式参见下述链接  
参考：https://www.osuix.com/2021/01/12/qv2ray-trojan-go-%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE-for-win10-macos/  
备份：./bak/Qv2ray Trojan-Go 安装配置 For win10 & MacOS - Asura & OSUIX.html  