# 查看支持哪些系统和架构
```
go tool dist list
```
# 在Windows下通过Powershell编译Windows、Linux、MacOS
```
# 编译linux下的可执行文件
$Env:GOOS = "linux"; $Env:GOARCH = "amd64"
go build -o example_linux_amd64

# 编译windows下的可执行文件
$Env:GOOS = "windows"; $Env:GOARCH = "amd64"
go build -o example_windows_amd64.exe

# 编译macos下的可执行文件
$Env:GOOS = "darwin"; $Env:GOARCH = "amd64"
go build -o example_darwin_amd64
```
# 在Linux下通过Bash编译Windows、Linux、MacOS
```
# 编译linux下的可执行文件
env GOOS=linux GOARCH=amd64 go build -o example_linux_amd64

# 编译windows下的可执行文件
env GOOS=windows GOARCH=amd64 go build -o example_windows_amd64.exe

# 编译macos下的可执行文件
env GOOS=darwin GOARCH=amd64 go build -o example_darwin_amd64
```