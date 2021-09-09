#!/usr/bin/python3


import argparse
import json
import requests


requests.packages.urllib3.disable_warnings();


def banner():
    print('''

    ***************************************************************
    FOFA API提取工具
    Author: ybdt
    First Date: 2021/01/18
    Last  Date: 2021/08/21
    ***************************************************************
    
    *************************警 告*********************************
    本工具旨在帮助企业快速定位漏洞、修复漏洞，仅限授权安全测试使用！
    请严格遵守《中华人民共和国网络安全法》，禁止未授权非法攻击站点！
    ***************************************************************

    ''');


def usage():
    parser = argparse.ArgumentParser(description="当前工具提取url和ip到对应的文件中");
    parser.add_argument("-f", "--file", help="FOFA API保存到本地后的json文件", required=True);
    args = parser.parse_args();
    json_file = args.file;
    
    return json_file;


def json_Extractor(json_file):
    ip_list = [];
    url_list = [];
    
    with open(json_file, "r", encoding='UTF-8') as f_r:
        json_content = f_r.read();
        dict_obj = json.loads(json_content);
        print( dict_obj.keys() );
        print( "error: " + str(dict_obj["error"]) );
        print("mode: " + dict_obj["mode"]);
        print( "page: " + str(dict_obj["page"]) );
        print( "results count: " + str( len(dict_obj["results"]) ) );
        print( "size: " + str(dict_obj["size"]) );
        count = len(dict_obj["results"]);
        for i in range(count):
            url = dict_obj["results"][i][0];#ip地址结合端口号看作url
            ip = dict_obj["results"][i][1];#单独的ip地址即为ip
            port = dict_obj["results"][i][2];#端口号即为端口号
            ip_list.append(ip);
            full_url = "http://" + url;
            url_list.append(full_url);
    
    return ip_list, url_list;


def main():
    
    banner();

    json_file = usage();

    ip_list, url_list = json_Extractor(json_file);
    
    with open("url.txt", "w") as f_w:
        for line in url_list:
            f_w.write(line + "\n");

    ip_list = list( dict.fromkeys(ip_list) );
    with open("ip.txt", "w") as f_w:
        for line in ip_list:
            f_w.write(line + "\n");


main();
