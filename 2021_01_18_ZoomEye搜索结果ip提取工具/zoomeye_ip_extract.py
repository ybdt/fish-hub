#!/usr/bin/python3

import json
import sys
import platform

'''
Author: ybdt
Date: 2021/01/18
'''

def extract(file, count):
    with open(file, "r") as f0:
        json_content = f0.read();
        dict_obj = json.loads(json_content);
        #print( dict_obj.keys() );
        #print( dict_obj["matches"][0].keys() );
        with open("zoomeye_ip_output.txt", "w") as f1:
            for i in range(count):
                ip = dict_obj["matches"][i]["ip"];
                print(ip);
                if platform.system() == "Linux":
                    f1.write(ip + "\n");
                elif platform.system() == "Windows":
                    f1.write(ip + "\r\n");

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 zoomeye_ip_extract.py \"app:'飞致云堡垒机'_160_1610893510.json\" 160");#参数值有单引号，需用双引号扩起来，否则不能正确识别
        exit();
    else:
        file = sys.argv[1];
        #print(file);
        count = int(sys.argv[2]);
    
    extract(file, count);
    print("The output file is zoomeye_ip_output.txt");

main();
