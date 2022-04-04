# 01-读取txt，写入txt
```
def txt_to_txt():
    with open("target.txt", "r", encoding="UTF-8") as fr:
        with open("legal-target.txt", "w", encoding="UTF-8") as fw:
            lines = fr.readlines()
            for line_ in lines:
                line = line_.strip()
                arr = line.split("/")
                if len(arr) > 3:
                    line = arr[0] + "/" + arr[1] + "/" + arr[2]
                    fw.write(line + "\n")
                else:
                    fw.write(line + "\n")
```

# 02-读取txt，写入csv
```
import pandas as pd
xuehao = []
xingming = []
yuanxi = []
def txt_to_csv():
    with open("学号 - 北京物资学院.txt", "r", encoding="UTF-8") as fr:
        lines = fr.readlines()
        for line_ in lines:
            line = line_.strip()
            chunks = line.split(" ")
            i = 0
            for chunk in chunks:
                if i % 3 == 0:
                    print(chunk)
                    xuehao.append(chunk)
                elif i % 3 == 1:
                    print(chunk)
                    xingming.append(chunk)
                elif i % 3 == 2:
                    print(chunk)
                    yuanxi.append(chunk)
                i += 1
txt_to_csv()
dataframe = pd.DataFrame( {"学号":xuehao, "姓名":xingming, "院系":yuanxi} )
dataframe.to_csv("result.csv", mode="w", index=False, sep=",")
```

# 03-分隔字符串生成手机号
```
def split_int():
    with open("a.txt", "r", encoding="UTF-8") as fr:
        with open("new-a.txt", "w", encoding="UTF-8") as fw:
            content = fr.read()
            phone = ""
            for i in content:
                if i == " ":
                    phone += "\n"
                    continue
                phone += i
            fw.write(phone)
```


# 04-json文件解析
```
def json_Extractor(json_filename):
    ip_list = []
    url_list = []
    with open(json_filename, "r", encoding='UTF-8') as fr:
        json_content = fr.read()
        dict_obj = json.loads(json_content)
        count = len(dict_obj["results"])
        for i in range(count):
            url = dict_obj["results"][i][0] # # 获取url
            ip = dict_obj["results"][i][1] # 获取ip
            ip_list.append(ip)

            #FOFA有一个特点，对于http协议的地址不会自动加上“http://”，故需要手动加上
            if url.startswith("https"):
                full_url = url
            else:
                full_url = "http://" + url
            
            url_list.append(full_url)
    return ip_list, url_list
```


# 05-生成指定B段及C段下的全部IP
```
def fun_1():
    with open("ip.txt", "w") as fw:
        for i in range(176, 192):
            for j in range(1, 256):
                ip = "172.24." + str(i) + "." + str(j)
                fw.write(ip + "\n")
```