### 请求方法替换
将GET改为POST，可能会返回：HTTP/1.1 411 Length Required，这个时候需要填充一些数据
将GET改为PUT，可能会返回：HTTP/1.1 411 Length Required，这个时候需要填充一些数据
### GET垃圾数据填充
```
abc=123&abc=123&abc=123&abc=123&abc=123&abc=123&abc=123&abc=123&abc=123&abc=123&abc=123&
```
### GET URL编码
### POST垃圾数据填充
```
with open("post-trash.txt", "w", encoding="UTF-8") as fw:
    fw.write("abc=123&" * 3000)
```
# ip换为域名

大并发