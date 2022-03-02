如题，在一次渗透测试中，发现每次构造sql语句都要手动将空格改为%20，太麻烦了，而且burp中暂时没找到将空格转化为%20的功能，于是写了一个python脚本
```
#!/usr/bin/python3

def main():
    var = input("Please input the string: ");
    str = "";
    for i in var:
        if i == " ":
            i = "%20";
        str += i;
    print(str);

main();
```

# 2021/03/11更新
burp下repeater中正常就是不能对空格进行自动编码的，浏览器能对空格进行自动编码
