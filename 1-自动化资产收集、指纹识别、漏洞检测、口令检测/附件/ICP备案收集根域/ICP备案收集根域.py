import argparse
import json
import pandas as pd


def usage():
    parser = argparse.ArgumentParser(description="Example: python3 ICP备案提取主域信息.py -f page1-40个.json -m w");
    parser.add_argument("-f", "--file", help="保存后的json文件", required=True);
    parser.add_argument("-m", "--mode", help="指定写入csv的格式，w为覆盖，a为追加", required=True);
    args = parser.parse_args();
    json_file = args.file;
    mode = args.mode;
    return json_file, mode;


def json_Extractor(json_file):
    domain_list = [];
    website_list = [];
    address_list = [];
    serviceLicence_list = [];
    with open(json_file, "r", encoding='UTF-8') as fr:
        json_content = fr.read();
        dict_obj = json.loads(json_content);#将json内容转化为字典对象
        count = dict_obj["params"]["size"];
        for i in range(count):
            sub_dict_obj = dict_obj["params"]["list"][i];#此时element为包含主域、网站名称、网站地址等信息的字典对象
            domain = sub_dict_obj["domain"];
            website = sub_dict_obj["serviceName"];
            address = sub_dict_obj["homeUrl"];
            serviceLicence = sub_dict_obj["serviceLicence"];
            domain_list.append(domain);
            website_list.append(website);
            address_list.append(address);
            serviceLicence_list.append(serviceLicence);
    return domain_list, website_list, address_list, serviceLicence_list;


def write_CSV_w(domain_list, website_list, address_list, serviceLicence_list):
    dataframe = pd.DataFrame( {"网站名称": website_list, "网站地址": address_list, "根域": domain_list, "备案号": serviceLicence_list} );
    dataframe.to_csv("root-Domain.csv", mode="w", index=False, sep=",");


def write_CSV_a(domain_list, website_list, address_list, serviceLicence_list):
    dataframe = pd.DataFrame( {"网站名称": website_list, "网站地址": address_list, "根域": domain_list, "备案号": serviceLicence_list} );
    dataframe.to_csv("root-Domain.csv", mode="a", header=None, index=False, sep=",");


def main():
    json_file, mode = usage();
    domain_list, website_list, address_list, serviceLicence_list = json_Extractor(json_file);
    if mode == "w":
        write_CSV_w(domain_list, website_list, address_list, serviceLicence_list);
    elif mode == "a":
        write_CSV_a(domain_list, website_list, address_list, serviceLicence_list);


main();
