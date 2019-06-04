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
class post_dynamic(unittest.TestCase):
#     def __init__(self,key,value):
#         unittest.TestCase.__init__(self,key,value)
#         self.key = key
#         self.value = value

    def setUp(self):
        self.url = "http://119.27.167.20:8083/dynamic.json"
        self.url2 = "http://119.27.167.20:8083/member/login.json"
        
    def login_dynamic(self):
        parm={'telephone':'15882481462','captcha':'123456'}
        r = requests.post(self.url2,data=parm)
        token=r.json()['data']['token']
       
        return token
    def dynamic_header(self):
        
        
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'token':post_dynamic.login_dynamic(self)
        }
        return headers
    def test_dynamic(self):
        
        parms = {'content':'#findyou#123','access_type':'0','images':'/dynamic/20190226/1551173819_3227a4a0e7734815a032a4a17903f8ad.jpg'}
        r = requests.post(self.url,data=parms,headers=post_dynamic.dynamic_header(self)) 
        code=r.status_code
        print(r.json())
        
        if    self.assertEqual(code, 200, 'Fail'):
            print('圈圈发布结果正确')
            
            
        else:
            print('圈圈发布失败')
            print(r.json())
        
        
    def test_dynamic_er1(self):    
        parms = {'content':'123','access_type':'0','images':'/dynamic/20190226/1551173819_3227a4a0e7734815a032a4a17903f8ad.jpg'}
        
        r2 = requests.post(self.url,data=parms,headers=post_dynamic.dynamic_header(self)) 
        
        string  = r2.json()['msg']
        
        if    self.assertEqual(string, '圈圈至少带一个话题哦', 'Fail'):
            print('无话题测试结果正确')
            
            
        else:
            print('无话题测试结果失败')
        
        

    
    
if __name__ == '__main__':
    unittest.main()    