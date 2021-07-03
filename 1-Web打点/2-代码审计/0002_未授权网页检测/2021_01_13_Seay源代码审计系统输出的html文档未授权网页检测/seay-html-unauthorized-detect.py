#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

def output_sort(id,vuln_category,filepath,vuln_detail):
    sort = {};
    for i in vuln_category:
        for j in filepath:
            for k in vuln_detail:
                if i in sort:
                    pass:
                else:
                    sort[i] = j + "和" + k;

def html_parse(html_doc):
    soup = BeautifulSoup(html_doc, features="lxml");
    element = soup.find_all("font")[1];
    count = element.string;
    print("一共漏洞数" + count + "个");
    id = [];
    vuln_category = [];
    filepath = [];
    vuln_detail = [];
    counter = 0;#用于去掉前4个td的内容
    for td in soup.find_all("td"):
        if counter < 4:
            counter += 1;
            continue;
        else:
            if td.get("width") == "30%":
                filepath.append(td.string);
            elif td.get("width") == "5%":
                id.append(td.string);
            elif td.get("width") == "20%":
                vuln_category.append(td.string);
            elif td.get("width") == "45%":
                vuln_detail.append(td.string);
    return id,vuln_category,filepath,vuln_detail;

def http_request(url, file_path):
    r = requests.get(url + file_path, allow_redirects=False);
    return r.status_code;

def main():
    url = "http://10.0.10.101/fbyCMS-master";
    f = open("fbyCMS.html", "r");
    html_doc = f.read();
    f.close();
    filepath = html_parse(html_doc);
    
    front_files = [];
    backend_files = [];
    unknown_files = [];
    for filename in filepath:
        status_code = http_request(url, filename);
        if status_code == 200:
            front_files.append(filename);
        elif status_code == 302:
            backend_files.append(filename);
        else:
            unknown_files.append(filename);
    print("前台漏洞" + str( len(front_files) ) + "个，文件如下");
    for i in front_files:
        print(i);
    print("后台漏洞" + str( len(backend_files) ) + "个，文件如下");
    for j in backend_files:
        print(j);
    print("非前台和后台漏洞" + str( len(unknown_files) ) + "个，文件如下");
    for k in unknown_files:
        print(k);

main();
