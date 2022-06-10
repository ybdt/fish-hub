#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Date     : 2020/04/02
Author   : ybdt
FileName : generate_filelist.py
'''

def verbose(var):
    if 0 <= var <= 9:
        return "00" + str(var);
    elif 10 <= var <= 99:
        return "0" + str(var);
    else:
        return str(var); 

def main():
    with open("filelist.txt", "w") as f:
        count = 0;
        while True:
            if count > 177:
                exit();
            var = verbose(count);
            f.write("file '4af3c40fab06bf660fd74ac57453e295_" + var + ".ts'");
            f.write("\n");
            count = count + 1;

if __name__ == "__main__":
    main();
