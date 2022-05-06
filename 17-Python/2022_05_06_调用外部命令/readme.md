调用外部命令有一个不错的第三方库sh，可惜的是只支持*nix

# subprocess
windows下建议使用库subprocess，参数可以是数组形式，也可以是字符串形式
```
subprocess.run(["python3.exe", "oneforall.py", "--target", "mnr.gov.cn", "run"])

subprocess.run("python3.exe oneforall.py --target mnr.gov.cn run")
```
字符串的形式更方便，我更喜欢字符串的形式

不过需要注意，如果执行cmd内的命令，如echo，需要指定shell=True，否则会报错，如果执行单独的可执行文件，则不用

# 调用cmd命令时遇到中文出现乱码的解决方法
```
import os
os.system('chcp 65001')
```
参考：https://blog.csdn.net/caviar126/article/details/114122792