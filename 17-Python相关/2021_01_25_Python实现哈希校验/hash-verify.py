#!/usr/bin/python3
'''
作者：ybdt
创建自：2017/05/21 22：16
更新自：2020/06/26 18：24
'''
import sys
import hashlib


def hash_calc(file_path):
    f = open(file_path, 'rb');
    index = input("please choose a encrypt method(0->md5,1->sha1,2->sha256): ");
    original_hash = input("please input the original hash: ");
    if index == "0":
        calced_hash = hashlib.md5( f.read() ).hexdigest();
    elif index == "1":
        calced_hash = hashlib.sha1( f.read() ).hexdigest();
    else:
        calced_hash = hashlib.sha256( f.read() ).hexdigest();
    print("The calced hash is: " + calced_hash);
    if calced_hash == original_hash.lower():
        print();
        print("It's ok");
    else:
        print();
        print("It's not ok");


def main():
    if len(sys.argv) != 2:
        print("Usage: python hash_verify.py verified_file");
        print();
        sys.exit(0);
    file_path = sys.argv[1];
    print("The hashing file is: " + file_path + ", waiting...");
    hash_calc(file_path);


if __name__ == "__main__":
    main();
