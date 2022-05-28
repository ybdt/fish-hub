apt update
apt upgrade
apt autoremove

apt install python3.8
cd /usr/bin
rm python3
ln -s python3.8 python3
apt install python3-pip

执行python、pip、apt update报错：ModuleNotFoundError: No module named 'apt_pkg'
cd /usr/lib/python3/dist-packages/
ln -s apt_pkg.cpython-36m-x86_64-linux-gnu.so apt_pkg.so
执行上述即可解决
参考链接：https://www.itbulu.com/py-apt-pkg.html

python3 -m pip install --upgrade pip

apt install openjdk-8-jdk