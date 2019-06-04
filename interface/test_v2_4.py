import urllib.request
import requests
import unittest
import json
import utils
import hmac
import hashlib
import string
import random
import  data
import con_login
def getHtml(url):
    page =urllib.request.urlopen(url)
    html = "D:\/pyrequest\/common"
    for line in page.readlines():
        html = html+str(line)+"\n"
        return html
class test_v2_4(unittest.TestCase):
#     def __init__(self,key,value):
#         unittest.TestCase.__init__(self,key,value)
#         self.key = key
#         self.value = value

    def setUp(self):
        self.url = "http://119.27.167.20:8083/member/loginout.json"
        self.url2 = "http://119.27.167.20:8083/common/praise.json"
        self.url3 = "http://119.27.167.20:8083/comment/del.json"
        self.url4="http://119.27.167.20:8083/comment/barrage.json"
        self.url5="http://119.27.167.20:8083/collection/favoritecontents.json"
        self.url6="http://119.27.167.20:8083/upvote.json"
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
            'token':test_praise.login_common(self)
        }
        return headers
    def test_loginout(self):
        r= requests.get(self.url,headers=con_login.common_header(self))
        msg=r.json()['msg']
        self.assertEqual(msg, '退出成功', 'FALSE')
    def test_praise_comment(self):
      
        r = requests.get(self.url2,headers=con_login.common_header(self)) 
        msg=r.json()['msg']
        self.assertEqual(msg, '操作成功','FALSE')    
    
    def test_del_comment(self):
        pa=data.test_get_comment_first(self)
        
        params={'relation_id':data.test_get_comment_first(self),'type':'1'}
        r = requests.post(self.url3,data=params,headers=con_login.common_header(self))
        msg=r.json()['msg']
        self.assertEqual(msg, '删除成功', 'failed')
    def test_get_Barrage(self):
        datas_1={'type':'1','relation_id':data.test_get_list(self)}   
        r = requests.get(self.url4,params=datas_1)
        msg=r.json()['msg']
        self.assertEqual(msg, 'success','failed')
          
    
    
if __name__ == '__main__':
    unittest.main()    