rem 参考连接：https://blog.csdn.net/baidu_33864675/article/details/120668484

rem 第一步：windows services 服务管理中关闭 Windows Update 服务
sc stop wuauserv
sc config wuauserv start= /disabled

rem 第二步：关闭任务计划中的WindowsUpdate
schtasks /Change /tn "\Microsoft\Windows\WindowsUpdate\Scheduled Start" /disable

rem 第三步：修改windows update 可执行程序的注册表
reg add "HKLM\SYSTEM\CurrentControlSet\Services\wuauserv" /v "ImagePath" /t REG_EXPAND_SZ /d "%systemroot%\system32\no.exe -k netsvcs -p" /f

rem 第四步：禁止 Windows Update Medic Service
sc stop WaaSMedicSvc
sc config WaaSMedicSvc start= /disabled
reg add "HKLM\SYSTEM\CurrentControlSet\Services\WaaSMedicSvc" /v "Start" /t REG_DWORD /d "4" /f

rem reg add "HKLM\SYSTEM\CurrentControlSet\Services\WaaSMedicSvc" /v "FailureActions" /t REG_BINARY /d "8051" /f