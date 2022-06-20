有时作者并未发布最新版编译后的二进制，需要自己编译
```
查看当前 GOOS 环境变量
set GOOS

设置操作系统、CPU架构以及禁用CGO
GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -ldflags="-s -w " -trimpath main.go

设置操作系统、CPU架构以及禁用CGO
GOOS=windows GOARCH=amd64 CGO_ENABLED=0 go build -ldflags="-s -w " -trimpath main.go
```

参考链接  
[https://blog.frytea.com/archives/607/](https://blog.frytea.com/archives/607/)  
[https://www.zhangbj.com/p/657.html](https://www.zhangbj.com/p/657.html)  