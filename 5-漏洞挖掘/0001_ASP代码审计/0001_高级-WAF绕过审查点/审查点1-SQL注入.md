1、可尝试大小写绕过，或关键字不出现在字符串首位，对应如下代码
```
if Instr(Username,"or")<>0 or Instr(Password,"or")<>0 or Instr(Username,"and")<>0 or Instr(Password,"and")<>0 then
    response.write "<br><br><br><br><font size=2><center>没事别搞人家后台，谢谢！<br>否则一切后果自负！</font>"
else
    ...
```
