rem 参考链接：https://blog.csdn.net/hacker_Lees/article/details/118296294

rmdir /s /q C:\Users\ybdt\AppData\Local\JetBrains\IntelliJIdea2021.1
rmdir /s /q C:\Users\ybdt\AppData\Roaming\JetBrains\IntelliJIdea2021.1
reg.exe delete HKEY_CURRENT_USER\SOFTWARE\JavaSoft\Prefs\jetbrains /f