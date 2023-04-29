#### 01 RLO反转字符，可将zip.exe反转为exe.piz
```
经测试

文件名反转 -> 会被360和Defender查杀
```

#### 02 可执行文件其他后缀scr，利用scr+RLO反转字符，将xcod.scr反转成rcs.docx
```
scr是windows下屏幕保护程序的后缀，是可执行的
windows下将exe文件后缀改为scr仍然可以执行，对于多数人来说会起到一定的迷惑性

经测试

更改后缀为scr -> 会被360查杀，Defender会延迟查杀（提示报毒仍能上线）
更改后缀为scr+文件名反装 -> 这个技术会被360和Defender查杀
```

#### 03 可执行文件其他后缀pif（学习自twitter下的评论），利用pif+RLO反转字符，将xcod.pif反转成fip.docx，注意：pif会有快捷方式的箭头
```
更改后缀为pif -> 会被360和Defender查杀
```

#### 04 文件a.docx.lnk由于windows自动省略.lnk，会显示a.docx，但会有快捷方式的箭头
```
快捷方式目前不会被查杀
```