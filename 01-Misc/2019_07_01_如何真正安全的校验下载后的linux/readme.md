# 如何真正安全的校验下载后的linux
## 前言
通常，想要下载一个安全的iso镜像，都会在下载后校验iso镜像的md5，但是对搞攻防的我们是远远不够的，我们会担心，黑客入侵了iso镜像的官网，并且替换了md5，于是有了这篇文章

## debian
从官网（https://cdimage.debian.org/debian-cd/current/amd64/bt-dvd/）下载种子文件，当前最新稳定版是9.8.0
通过迅雷下载ios文件，首先通过python脚本和官方校验文件（https://cdimage.debian.org/debian-cd/current/amd64/bt-dvd/SHA256SUMS）检查SHA256SUMS校验值，没有问题
55476054b4f70cf23b8d504de5069698236e55db5822653d4f76abd02766d546 debian-9.8.0-amd64-DVD-1.iso
公钥指纹ID：6294BE9B（https://www.debian.org/CD/verify）
win10下通过ubuntu中的gpg校验签名
gpg2 –verify ./ SHA256SUMS.sign ./SHA256SUMS
没问题

## kali
公钥指纹ID：7D8D0BF6（https://www.kali.org/downloads/）
win10中的ubuntu下gpg校验
gpg2 –verify ./ SHA256SUMS.gpg ./SHA256SUMS
gpg签名没有问题
f86b3c6cc98af2d2d86e829fb8a3b08b4d5c4f376d6b8b1e108c58fcfdb46229 kali-linux-xfce-2019.1-amd64.iso
python脚本hash验证
hash没有问题

## kali校验从头操作
windows下的linux子系统ubuntu之前被我卸载了，重新安装ubuntu18.04
安装后更新系统：sudo apt update && sudo apt upgrade
由于没有gpg2，执行：sudo apt install gnup2
伴随系统镜像下载的只有kali-linux-2019.4-amd64.iso.txt.sha256sum和种子文件，从http://cdimage.kali.org/kali-2019.4/下载SHA256SUMS.gpg以及SHA256SUMS，执行：
gpg2 –verify ./SHA256SUMS.gpg ./SHA256SUMS
提示：
gpg: Signature made Tue Nov 26 01:13:21 2019 CST
gpg: using RSA key 44C6513A8E4FB3D30875F758ED444FF07D8D0BF6
gpg: Can’t check signature: No public key

尝试执行
gpg –keyserver hkp://keys.gnupg.net –recv-key 7D8D0BF6
下载公钥失败
尝试执行
gpg2 –recv-keys 0x7D8D0BF6
下载公钥失败
尝试执行
wget -q -O - https://www.kali.org/archive-key.asc | gpg –import
下载公钥成功

gpg2 –verify ./SHA256SUMS.gpg ./SHA256SUMS
提示
gpg: Signature made Tue Nov 26 01:13:21 2019 CST
gpg: using RSA key 44C6513A8E4FB3D30875F758ED444FF07D8D0BF6
gpg: Good signature from “Kali Linux Repository devel@kali.org“ [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg: There is no indication that the signature belongs to the owner.
Primary key fingerprint: 44C6 513A 8E4F B3D3 0875 F758 ED44 4FF0 7D8D 0BF6
签名校验成功

使用自己编写的python脚本校验hash
python .\hash_verify.py .\kali-linux-2019.4-amd64.iso bad0d602a531b872575e23cc025b45fee475523b51378a035928b733ca395ac5
哈希校验成功

## ubuntu
下载torrent文件从官方站点（https://www.ubuntu.com/download/alternative-downloads）

下载iso文件通过迅雷

使用python脚本和官方校验文件（http://releases.ubuntu.com/xenial/SHA256SUMS）检查SHA256SUMS校验值，有问题
（第一次校验失败，然后过段时间当我看到官方的校验文件对应的是*ubuntu-16.04.6-desktop-amd64.iso时，还怀疑之前是不是错把16.04.6的校验值用来校验16.04.5了，但幸亏之前特意记录的一份16.04.5的校验值，如下：
6b505fd3b6f816f8ff058710f127a9900e9233e496783ce08a0022814d224810 *ubuntu-16.04.5-desktop-amd64.iso
所以，很可能之前的16.04.5版本的iso是损坏的）

从官网（http://releases.ubuntu.com/16.04.6/）直接下载iso文件
使用python脚本和官方校验文件（http://releases.ubuntu.com/16.04.6/SHA256SUMS）检查SHA256SUMS校验值，没问题
e27d13d089a027601099b050fd6080785aae99c1a8eb7848774b8d44f1f679b9 *ubuntu-16.04.6-desktop-amd64.iso

公钥指纹ID：ubuntu中，下载公钥时只需指定公钥服务器即可，ubuntu会定期检查公钥服务器中的公钥指纹（https://tutorials.ubuntu.com/tutorial/tutorial-how-to-verify-ubuntu?_ga=2.135184498.2142261077.1551772618-1953445124.1550581087#2）
然后在win10下，通过ubuntu中的gpg2进行校验
gpg2 –verify ./SHA256SUMS.gpg ./SHA256SUMS
校验失败，后经排查发现，即使文件名和文件内容全都拷贝，然后创建文件后再粘贴，仍然会失败，只有将官网（http://releases.ubuntu.com/16.04.6/）上的这两个文件通过迅雷下载下来，才能校验成功