#!/usr/bin/python3

import argparse
import json

def banner():
    print("");
    print("*************************************************************************************");
    print("IP提取器针对ZoomEye-python生成的JSON文件");
    print("Author: ybdt");
    print("First Date: 2021/01/18");
    print("Last Date: 2021/04/14");
    print("Location: https://github.com/ybdt/web-hub/tree/main/2021_01_18_ZoomEye搜索结果提取工具");
    print("*************************************************************************************");
    print("");
    print("*************************警 告*****************************");
    print("本工具旨在帮助企业快速定位漏洞、修复漏洞,仅限授权安全测试使用!");
    print("请严格遵守《中华人民共和国网络安全法》,禁止未授权非法攻击站点!");
    print("***********************************************************");
    print("");
    print("");

def usage():
    parser = argparse.ArgumentParser(description="若文件名包含单引号，需用双引号扩起来，否则不能正确识别");
    parser.add_argument("file",
                        help="使用zoomeye-python生成的JSON文件");
    parser.add_argument("count", type=int,
                        help="指定JSON文件中设备的个数，用于传递给提取器函数");
    args = parser.parse_args();
    json_file = args.file;
    count = args.count;
    return json_file, count;

def extractor(json_file, count):
    with open(json_file, "r") as f_r:
        with open("ip.txt", "w") as f_w:
            json_content = f_r.read();
            dict_obj = json.loads(json_content);
            #print( dict_obj.keys() );
            #print( dict_obj["matches"][0].keys() );
            for i in range(count):
                ip = dict_obj["matches"][i]["ip"];
                port = dict_obj["matches"][i]["portinfo"]["port"];
                if dict_obj["matches"][i]["portinfo"]["service"] == "http":
                    service = "http";
                elif dict_obj["matches"][i]["portinfo"]["service"].startswith("https"):
                    service = "https";
                else:
                    service = dict_obj["matches"][i]["portinfo"]["service"];
                print( service + "://" + ip + ":" + str(port) );
                f_w.write(service + "://" + ip + ":" + str(port) + "\n");

def main():
    
    banner();

    json_file, count = usage();
    
    extractor(json_file, count);

main();