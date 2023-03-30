# 0x01 Go安装及配置
```
下载并安装goland 2021.1系列：https://www.jetbrains.com/go/download/other.html
goland 2021.1无限试用方式：https://ybdt.me/2022/01/13/如何放心的白嫖四大主流语言IDE/
下载go语言编译器：https://go.dev/dl/

Windows下
配置GOROOT=C:\Program Files\Go
配置GOPATH=C:\Users\admin\go
配置GOPROXY=https://goproxy.cn,direct
配置Path，添加%GOROOT%\bin
通过命令行设置GO111MODULE的值
go env -w GO111MODULE=on
go env -u GO111MODULE

Mac下
在~/.zshrc中添加
export GOROOT=/usr/local/go
export GOPATH=/Users/ybdt/go
export GOPROXY="https://goproxy.cn,direct"
export PATH=$PATH:$GOROOT/bin
通过命令行设置GO111MODULE的值
go env -w GO111MODULE=on
go env -u GO111MODULE

参考文章：
https://www.cnblogs.com/yunfan1024/p/13497686.html
https://www.cnblogs.com/hi3254014978/p/15172691.html
```

# 0x02 Go跨平台编译
查看支持哪些系统和架构
```
go tool dist list
```

## Windows下通过Powershell编译Windows、Linux、MacOS
编译windows下的可执行文件
```
$Env:GOOS = "windows"; $Env:GOARCH = "amd64"
go build -o windows_amd64.exe main.go
```

编译linux下的可执行文件
```
$Env:GOOS = "linux"; $Env:GOARCH = "amd64"
go build -o linux_amd64 main.go
```

编译macos下的可执行文件
```
$Env:GOOS = "darwin"; $Env:GOARCH = "amd64"
go build -o darwin_amd64 main.go
```

# Mac/Linux下通过Bash编译Windows、Linux、MacOS
编译macos下的可执行文件
```
env GOOS=darwin GOARCH=amd64 go build -o darwin_amd64 main.go
```

编译linux下的可执行文件
```
env GOOS=linux GOARCH=amd64 go build -o linux_amd64 main.go
```

编译windows下的可执行文件
```
env GOOS=windows GOARCH=amd64 go build -o windows_amd64.exe main.go
```