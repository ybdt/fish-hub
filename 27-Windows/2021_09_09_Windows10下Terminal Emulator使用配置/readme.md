# 使用Cmder
1、修改命令提示符
```
打开文件\vendor\clink.lua，定位到51行，将"λ"修改为"$"
```
2、修改启动路径  
```
Settings -> Startup -> Tasks -> 选择对应的Shell（cmd或powershell），修改右边的值为：
*cmd /k ""%ConEmuDir%\..\init.bat" -new_console:d:C:\Users\ybdt\Desktop"
```

# （2021/09/09）改用ConEmu
ConEmu更酷，改用ConEmu  

01、修改启动路径
```
Settings -> Startup -> Tasks -> 选择对应的Shell（cmd或powershell），修改右边的值为：
cmd.exe /k "%ConEmuBaseDir%\CmdInit.cmd" -new_console:a -new_console:d:C:\Users\ybdt\Desktop
```
02、修改默认字体
```
Settings -> General -> Fonts -> Size改为18
```
03、修改界面语言
```
Settings -> General -> Interface language（简体中文）
```
04、修改为默认启动管理员权限的cmd
```
设置 -> 通用 -> 选择你的启动任务（cmd:Admin）
```
05、修改默认颜色
```
设置 -> 通用 -> 选择颜色方案（Default Windows scheme）
```
06、设置中文乱码
```
设置 -> 启动 -> 环境 -> 右侧空白处添加如下
chcp utf8（chcp 65001）
```
07、分屏
```
ctrl+shift+e（纵向切割）
ctrl+shift+o（横向切割）
终端切换，点击对应屏幕即可

快捷键查看可在：设置 -> 按键 & 宏
```

还可以设置代理、等等（待探索）