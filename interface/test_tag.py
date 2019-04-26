#coding = UTF-8
import unittest

import sys

from requests import cookies
sys.path.append('D:\pyrequest')
sys.path.append('D:\pyrequest\common')


# from getlogin import Get_Login
import urllib.request
import requests

import json
import utils



def getHtml(url):
    page =urllib.request.urlopen(url)
    html = "D:\/pyrequest\/common"
    for line in page.readlines():
        html = html+str(line)+"\n"
        return html
        print("0")
class Get_Tags(unittest.TestCase):
    def setUp(self):
        self.url = "http://119.27.167.20:8083/member/membertags.json"
        self.url2 = "http://119.27.167.20:8083/member/login.json"
      
        
        
       
    def test_login2(self):
        parm={'telephone':'15882481462','captcha':'123456'}
        r = requests.post(self.url2,data=parm)
        token=r.json()['data']['token']
        
        return token
        

    def test_tags(self):
        
        token= Get_Tags.test_login2(self)
        
        print(token,"T")
        parm=None
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'token':Get_Tags.test_login2(self)
        }
        print(headers)
        
        k = requests.get(self.url,headers=headers,verify=False,data=parm)
        print(k.url)
        print(k.text)
        self.assertEqual(k.status_code, 200,'fail')


if __name__ == '__main__':
    unittest.main()   
       
    
