import argparse
import requests
import threading


def usage():
    parser = argparse.ArgumentParser(description="Example: python3 masscan-Live-Detect.py -f wps-120.92.124.txt");
    parser.add_argument("-f", "--file", help="Masscan扫描以-oL（文本格式）输出的结果", required=True);
    args = parser.parse_args();
    ip_file = args.file;
    return ip_file;


def txt_Extractor(txt_file):
    url_list = [];
    with open(txt_file, "r") as fr:
        lines = fr.readlines();
        for line in lines:
            line_list = line.split();
            if len(line_list) != 5:
                continue;
            else: 
                url = "{0}:{1}".format(line_list[3], line_list[2]);
                print(url);
                url_list.append(url);
    return url_list;


def live_Detect(url_list):
    with open("live.txt", "w", encoding='UTF-8') as fw_s:
        with open("read-Timeout.txt", "w", encoding='UTF-8') as fw_r:
            with open("waf.txt", "w", encoding='UTF-8') as fw_w:
                for line in url_list:
                    url = "http://{0}".format(line);
                    print( "Detecting {0}".format(url) );
                    try:
                        r = requests.get(url=url, timeout=3, verify=False);#超时设置太短，可能会报读取超时异常
                        fw_s.write(url + "\n");
                        print( "[+]Target {0} respond successfully，add to success.txt\n".format(url) );
                    except requests.exceptions.ConnectionError as e1:
                        fw_w.write(url + "\n");
                        print( "[-]Target {0} refused or reset，maybe WAF intercept\n".format(url) );
                    except requests.exceptions.ReadTimeout as e2:
                        fw_r.write(url + "\n");
                        print( "[-]Target {0} readtimeout，add to read-Timeout.txt\n".format(url) );


def main():
    txt_file = usage();
    url_list = txt_Extractor(txt_file);
    live_Detect(url_list);
    '''
    thread_num = 10;
    for i in thread_num:
        thread = threading.Thread( target=live_Detect, args=(url_list) );
        thread.start();
    '''


main();