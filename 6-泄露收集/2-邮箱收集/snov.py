# -*- coding: utf-8 -*-
# @Time : 2021年08月04日:14时34分
# @File : snov.py
import requests
import re
import json
from urllib.parse import unquote
from math import ceil
from optparse import OptionParser  #用于生成帮助文档
from os.path import exists
import warnings
warnings.filterwarnings('ignore')

class Snov:
    def __init__(self):
        self.domain="https://app.snov.io"
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'
        }
        self.session=requests.session()


    def _login(self,username,password):  #自动登录功能
        session=requests.session() #定义session
        url=self.domain+"/login"
        response=session.get(url=url,headers=self.headers)
        data=response.content.decode()
        pattern="name=\"_token\"\s?value=\"(.*?)\"" #获取登录使用的token
        result=re.findall(pattern,data)
        try:
            _token=result[0]
        except:
            return False
        param={
            "email":username,
            "password":password,
            "_token":_token,
            "remember":"off"
        }
        response=session.post(url=url,data=param,headers=self.headers,verify=False)
        XSRF_TOKEN=session.cookies.get("XSRF-TOKEN")
        self.headers['X-XSRF-TOKEN']=unquote(XSRF_TOKEN)  #将XSRF_TOKEN复制
        self.session=session
        return True

    def _getDomainSearch(self,searchDomain):
        param={"domain":searchDomain,"isGreen":"true","lastId":0,"perPage":20}
        url=self.domain+"/domain-search"
        headers = self.headers
        headers['Content-Type'] = "application/json"
        response=self.session.post(url=url,headers=headers,data=json.dumps(param),verify=False)
        data=response.content.decode()
        print(data);
        data=json.loads(data)
        try:
            id=data.get("companyInfo",None).get('id',None)
            return id  #返回公司id
        except:
            return False

    def _getTotal(self,id):  #获取邮箱和联系人总个数
        url=self.domain+"/companies/"+str(id)
        headers = self.headers
        headers['Content-Type'] = "application/json"
        response=self.session.post(url=url,data=None,headers=headers,verify=False)
        data=response.content.decode()
        data=json.loads(data)
        try:
            emailsTotal=data.get("emailsTotal",0)
            contactsTotal=data.get("contactsTotal",0)
            return (emailsTotal,contactsTotal)
        except:
            return (0,0)
    def _getMail(self,total,id,target):  #获取全部邮箱
        url = self.domain + "/companies/" + str(id) + "/" + "emails"
        headers = self.headers
        headers['Content-Type'] = "application/json"
        headers['Referer'] = "https://app.snov.io/domain-search?name={}&tab=emails".format(target)
        headers['X-Requested-With'] = "XMLHttpRequest"
        #total=452
        count=ceil(total/200)
        print("{}一个有{}个邮箱，分{}次获取".format(target,total,count))
        lastId=None
        for i in range(1,count+1,1):
            if not lastId:
                param={"isGreen":True,"lastId":0,"perPage":200,"page":i}
                response=self.session.post(url=url,data=json.dumps(param),headers=headers,timeout=50,verify=False)
                data=response.content.decode()
                data=json.loads(data)
                lists=data.get("list",None)
                lastId=data.get("lastId",1)
                self._storeMail(lists,target)
            elif lastId:
                param={"isGreen":True,"lastId":lastId,"perPage":200,"domain":""}
                response = self.session.post(url=url, data=json.dumps(param), headers=headers, timeout=50, verify=False)
                data = response.content.decode()
                data = json.loads(data)
                lists = data.get("list", None)
                lastId = data.get("lastId", 1)
                self._storeMail(lists,target)

    def _storeMail(self,lists,target):
        storage="./"+target+"_mails.txt"
        if lists:
            with open(storage,"a",encoding="utf-8") as fp:
                for list in lists:
                    email=list.get('email',None)
                    if email:
                        fp.write(email)
                        fp.write("\n")

    def run(self,username,password,targets):
        if self._login(username=username,password=password):
            for target in targets:
                print("开始查询{}。".format(target))
                id=self._getDomainSearch(target.strip())
                emailsTotal, contactsTotal = self._getTotal(id)
                self._getMail(emailsTotal,id,target)
        else:
            exit("登录出错！")



if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-u", "--user", dest="username", default=None, help="用户名")
    parser.add_option("-p", "--pass", dest="password", default=None, help="登录密码")
    parser.add_option("-t", "--target", dest="target", default=None, help="要查询的域名，多个目标使用,隔开")
    parser.add_option("-f", "--file", dest="file", default=None,  help="可以使用文件输入目标，一行一个")
    (options, args) = parser.parse_args()  # 取值并且存入options
    if (options.username and options.password):
        if options.target:
            targets=options.target.split(",")
            print(targets)
        elif exists(options.file):
            targets=list()
            with open(options.file,"r",encoding='utf-8') as fp:
                line=fp.readline()
                while line:
                    line=line.strip()
                    targets.append(line)
                    line=fp.readline()
        else:
            targets=None
        if targets:
            snov=Snov()
            snov.run(options.username.strip(),options.password.strip(),targets)
    else:
        exit("输入有误，滚啊！！！")