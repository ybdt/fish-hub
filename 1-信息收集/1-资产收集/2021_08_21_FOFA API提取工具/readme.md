### FOFA高级会员如何通过API获取结果
```
1、点击“使用API”后会生成一个链接，默认情况下，API只会显示前100条数据，需要在API后面添加：&size=10000，可显示前10000条数据
（FOFA规定，高级会员使用API查询数据每次最多10000条）
2、使用浏览器访问修改后的链接，ctrl+s可将当前页面内容保存到本地，默认命名为all.json
3、借助工具FOFO-Extractor.py，执行命令：python3.exe .\FOFO-Extractor.py -f all.json，可获取包含ip和url的文件ip.txt和url.txt
```
