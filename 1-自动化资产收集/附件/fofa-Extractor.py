import argparse
import json
import requests


requests.packages.urllib3.disable_warnings();

'''
使用API的话，想要显示全部数据，需要在API后面添加：&size=10000&full=true
'''

def banner():
    print(
    '''
    ***************************************************************
    FOFA结果提取工具
    Author: ybdt
    First Date: 2021/01/18
    Last  Date: 2021/10/21
    ***************************************************************
    
    *************************警 告*********************************
    本工具旨在帮助企业快速定位漏洞、修复漏洞，仅限授权安全测试使用！
    请严格遵守《中华人民共和国网络安全法》，禁止未授权非法攻击站点！
    ***************************************************************
    '''
    )


def usage():
    parser = argparse.ArgumentParser(description="Example: python3 fofa-Extractor.py -f all.json");
    parser.add_argument("-f", "--file", help="FOFA API保存到本地后的json文件", required=True);
    args = parser.parse_args();
    json_file = args.file;
    return json_file;


def json_Extractor(json_file):
    ip_list = [];
    url_list = [];
    
    with open(json_file, "r", encoding='UTF-8') as fr:
        json_content = fr.read();
        dict_obj = json.loads(json_content);
        '''
        # debug
        print( dict_obj.keys() );
        print( "error: " + str(dict_obj["error"]) );
        print("mode: " + dict_obj["mode"]);
        print( "page: " + str(dict_obj["page"]) );
        print( "results count: " + str( len(dict_obj["results"]) ) );
        print( "size: " + str(dict_obj["size"]) );
        '''
        count = len(dict_obj["results"]);
        for i in range(count):
            url = dict_obj["results"][i][0];#url = ip + port
            ip = dict_obj["results"][i][1];#获取ip地址
            port = dict_obj["results"][i][2];#获取端口号
            ip_list.append(ip);
            if url.startswith("https"):
                full_url = url
            else:
                full_url = "http://" + url;
            url_list.append(full_url);
    return ip_list, url_list;


def main():
    banner();

    json_file = usage();

    ip_list, url_list = json_Extractor(json_file);
    
    with open("url.txt", "w") as fw_u:
        for line in url_list:
            fw_u.write(line + "\n");

    ip_list = list( dict.fromkeys(ip_list) );
    with open("ip.txt", "w") as fw_i:
        for line in ip_list:
            fw_i.write(line + "\n");


main();