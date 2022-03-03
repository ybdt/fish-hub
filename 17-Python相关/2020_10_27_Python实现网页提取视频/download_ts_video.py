#!/usr/bin/python3
# -*- coding: utf-8

'''
Date     : 2020/04/02
Author   : ybdt
FileName : download_ts_video.py
'''

import requests
import sys
import os

def verbose(var):
    var = int(var) + 1;
    if 1 <= var <= 9:
        return "00" + str(var);
    elif 10 <= var <= 99:
        return "0" + str(var);
    else:
        return str(var); 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 download_ts_video.py url");
        print("Example: python3 download_ts_video.py https://www.ybdt.com/a.txt");
        exit();
    url = sys.argv[1];
    tail = url.split("/")[7].split("_")[1];
    print("The tail is: " + tail);
    body = url.split("/")[7].split("_")[0];
    print("The body is: " + body);
    head = url.strip(body + "_" + tail);
    print("The head is: " + head);
    var = 0;
    if not os.path.exists("ybdt_tmp"):
        os.system("mkdir ybdt_tmp");
    cwd = os.path.join(os.getcwd(), "ybdt_tmp");
    while True:
        new_url = head + body + "_" + str(var) + ".ts";
        print(new_url);
        r = requests.get(new_url);
        if r.status_code == 404:
            print("404 not found");
            print("Exiting...");
            print("Exit Finished");
            exit();
        filename = body + "_" + str(var) + ".ts";
        full_filename = os.path.join(cwd, filename)
        with open(full_filename, "wb") as f:
            f.write(r.content);
        print("Downloading...");
        print("Download Finished");
        var = var + 1;

if __name__ == "__main__":
    main();
