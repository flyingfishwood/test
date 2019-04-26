import urllib.request
import requests
import unittest
import json
import utils
import hmac
import hashlib
import string
from data import *
from _ast import Try

def getHtml(url):
    page =urllib.request.urlopen(url)
    html = "D:\/pyrequest\/common"
    for line in page.readlines():
        html = html+str(line)+"\n"
        return html
class test_search(unittest.TestCase):
#     def __init__(self,key,value):
#         unittest.TestCase.__init__(self,key,value)
#         self.key = key
#         self.value = value

    def setUp(self):
        self.url = "http://119.27.167.20:8083/search/lists.json"
        self.url2 = "http://119.27.167.20:8083/member/login.json"
        self.url3 = "http://119.27.167.20:8083/search/recommends.json"
        self.url4="http://119.27.167.20:8083/common/bannerlists.json"
        self.url5="http://119.27.167.20:8083/common/shareinfo.json"
        
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
            'token':test_search.login_common(self)
        }
        return headers
    def test_search(self):
        
        key = str(123)
        
        parms = {'page':'1','row':'21','id':'','m':'1','kw':key}
        r = requests.get(self.url,params=parms)
        code=r.json()['code']
    
        
        print('搜索列表')
        
        if    self.assertEqual(code,200, 'Fail'):
            print('搜索结果正确')
            
            
        else:
            print('搜索列表查询失败')
    def test_recommends(self):
        
        
        r = requests.get(self.url3)
        code=r.json()['code']
        print('推荐列表')
        
        if    self.assertEqual(code,200, 'Fail'):
            print('推荐结果正确')
            
            
        else:
            print('推荐列表查询失败') 
    def test_banner(self):
        params = {'cate':'1'}
        r = requests.get(self.url4,params=params)
        
        if r.status_code == 200:
            print('banner获取成功')
        else:
            print('获取失败')
    def test_share(self):
        id = test_get_list(self)
        params = {'type':'1','relation_id':id,'target':'1'} 
        r = requests.get(self.url5, params=params,headers = test_search.common_header(self))
        print(r.json())
        code = r.json()['code']
        print('分享内容')
        
        if  self.assertEqual(code,200, 'Fail'):
            print('分享成功') 
        else:
            print('分享获取失败')     
       
    
    
if __name__ == '__main__':
    unittest.main()    