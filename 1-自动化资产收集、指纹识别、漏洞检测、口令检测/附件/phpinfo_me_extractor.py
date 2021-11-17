def phpinfo_me_extractor():
    with open("all.txt", "r", encoding="UTF-8") as fr:
        with open("url.txt", "w", encoding="UTF-8") as fw_url:
            with open("ip.txt", "w", encoding="UTF-8") as fw_ip:
                lines = fr.readlines()
                for line in lines:
                    url = line.strip("查询成功：").split("-")[0]
                    ip = line.strip("查询成功：").split("-")[1].strip("\n")
                    fw_url.write(url + "\n")
                    fw_ip.write(ip + "\n")

phpinfo_me_extractor()