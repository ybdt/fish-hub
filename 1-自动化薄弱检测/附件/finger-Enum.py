import argparse
import requests
from bs4 import BeautifulSoup
import pandas as pd


requests.packages.urllib3.disable_warnings()


def usage():
    parser = argparse.ArgumentParser(description="Example: python3 finger-Print.py -f live.txt");
    parser.add_argument("-f", "--file", help="包含协议、IP、端口，每行一个，Example: http://111.111.111.111:8080", required=True);
    args = parser.parse_args();
    ip_file = args.file;
    return ip_file;


class Scanner(object):
    
    def __init__(self, ip_file):
        self.ip_file = ip_file;

    def file_parse(self, ip_file):
        with open(ip_file, "r") as fr:
            lines = fr.readlines();
        return lines;

    def get_title_and_server_info(self, lines):
        url_list = [];
        title_list = [];
        server_list = [];
        for line in lines:
            line = line.strip("\n");#去掉结尾的换行符
            
            #先发起一个http请求，根据返回的内容判断目标使用的协议是http还是https
            r_http = requests.get(url=line, timeout=3, verify=False, allow_redirects=True);
            if "The plain HTTP request was sent to HTTPS port" in str(r_http.content):
                line = "https://" + line.strip("http://");
                r_https = requests.get(url=line, timeout=3, verify=False, allow_redirects=True);
                r = r_https;
            else:
                r = r_http;

            print( "Detecting {}".format(line) );
            
            #获取title
            if BeautifulSoup(r.content, "lxml").title == None:
                title = "";
            else:
                title = BeautifulSoup(r.content, "lxml").title.text.strip("\n").strip();
            
            #获取server信息
            if "Server" in r.headers.keys():
                server = r.headers['Server'].split()[0] if 'Server' in str(r.headers) else '';
            else:
                server = "";
            
            url_list.append(line);
            title_list.append(title);
            server_list.append(server);
        return url_list, title_list, server_list;
    
    def write_to_csv(self, url_list, title_list, server_list):
        dataframe = pd.DataFrame( {"url": url_list, "title": title_list, "server": server_list} );
        dataframe.to_csv("finger.csv", index=False, sep=',');

    def run(self):
        self.lines = self.file_parse(self.ip_file);
        self.url_list, self.title_list, self.server_list = self.get_title_and_server_info(self.lines);
        self.write_to_csv(self.url_list, self.title_list, self.server_list);


def main():
    ip_file = usage();

    scanner = Scanner(ip_file);
    scanner.run();


main();
