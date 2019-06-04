import urllib.request
import requests
import unittest
import json
import utils
import hmac
import hashlib
import string

def getHtml(url):
    page =urllib.request.urlopen(url)
    html = "D:\/pyrequest\/common"
    for line in page.readlines():
        html = html+str(line)+"\n"
        return html
class test_init(unittest.TestCase):
#     def __init__(self,key,value):
#         unittest.TestCase.__init__(self,key,value)
#         self.key = key
#         self.value = value

    def setUp(self):
        self.url = "http://119.27.167.20:8083/app.json"
        self.url2 = "http://119.27.167.20:8083/member/login.json"
        self.url3 = "http://119.27.167.20:8083/comment.json"
        self.url4="http://119.27.167.20:8083/collection/lists.json"
        
    def login_common(self):
        parm={'telephone':'15882481462','captcha':'123456'}
        r = requests.post(self.url2,data=parm)
        token=r.json()['data']['token']
       
        return token
    def common_header(self):
        
        
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'token':test_init.login_common(self)
        }
        return headers
    def test_init(self):
        
        params={'device-version':'2.4.0','device-type':'IOS','version':'2.4.0'}
        r = requests.get(self.url,params=params,headers=test_init.common_header(self))
        code =r.json()['code']
        print('app初始化',r.json())
        
        
        if self.assertEqual(code, 200, 'Fail'):
            
           print('初始化结果正确')
            
            
        
        else :print('初始化失败',r.json())
      
    
        
    
    
if __name__ == '__main__':
    unittest.main()    