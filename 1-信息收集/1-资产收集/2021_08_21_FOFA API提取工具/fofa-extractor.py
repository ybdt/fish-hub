#!/usr/bin/python3


import argparse
import json
import requests


requests.packages.urllib3.disable_warnings();


def banner():
    print("");
    print("");
    print("****************************************************");
    print("FOFA API提取工具");
    print("Author: ybdt");
    print("First Date: 2021/01/18");
    print("Last  Date: 2021/06/22");
    print("****************************************************");
    print("");
    print("*************************警 告*****************************");
    print("本工具旨在帮助企业快速定位漏洞、修复漏洞，仅限授权安全测试使用!");
    print("请严格遵守《中华人民共和国网络安全法》，禁止未授权非法攻击站点!");
    print("***********************************************************");
    print("");
    print("");


def usage():
    parser = argparse.ArgumentParser(description="若文件名包含单引号，需用双引号扩起来，否则不能正确识别");
    parser.add_argument("-f", "--file", help="FOFA API保存到本地后的文件", required=True);
    parser.add_argument("-c", "--count", type=int, help="指定JSON文件中结果的个数，用于传递给提取器函数", required=True);
    args = parser.parse_args();
    json_file = args.file;
    count = args.count;
    
    #domain_file = json_file.strip(".\\").strip(".json") + "-域名.txt";
    domain_file = "域名.txt";
    #ip_file = json_file.strip(".\\").strip(".json") + "-ip.txt";
    ip_list = [];
    
    return json_file, count, domain_file, ip_list;


def extractor(json_file, count, domain_file, ip_list):
    with open(json_file, "r", encoding='UTF-8') as f_r:
        with open(domain_file, "w") as f_w_domain:
                json_content = f_r.read();
                dict_obj = json.loads(json_content);
                #print( dict_obj.keys() );
                #print( dict_obj["matches"][0].keys() );
                for i in range(count):
                    url = dict_obj["results"][i][0];
                    ip = dict_obj["results"][i][1];
                    ip_list.append(ip);
                    if url.startswith("https"):
                        final_url = url;
                    else:
                        if dict_obj["results"][i][2] == "443":
                            final_url = "https://" + url;
                        else:
                            final_url = "http://" + url;
                    print(final_url);
                    f_w_domain.write(final_url + "\n");
    return ip_list;


def live_detect(domain_file):
    with open(domain_file, "r") as f_r:
        output_name = domain_file.strip(".txt");
        with open(output_name + "-存活.txt", "w") as f_w:
            lines = f_r.readlines();
            for line in lines:
                line = line.strip("\n");
                try:
                    r = requests.get(line, verify=False);
                    print( line + "-----" + str(r.status_code) );
                    f_w.write(line + "\n");
                except requests.exceptions.ConnectionError:
                    print(line + "-----ConnectionError");
                except:
                    print(line + "-----Unknown");


def ip_cut_repeat(ip_list):
    new_lines = [];
    for line in ip_list:
        if line not in new_lines:
            new_lines.append(line);
    with open("ip.txt", "w") as f_w:
        for i in new_lines:
            print(i);
            f_w.write(i + "\n");


def main():
    
    banner();

    json_file, count, domain_file, ip_list = usage();
    
    print("JSON提取结果：");
    ip_list = extractor(json_file, count, domain_file, ip_list);
    print("");
    print("");
    print("存活检测结果：");
    live_detect(domain_file);
    print("");
    print("");
    print("IP提取结果：");
    ip_cut_repeat(ip_list);


main();
