import urllib.request
import requests
import unittest
import json
import utils
import hmac
import hashlib
import string
import random
from data import  *
def getHtml(url):
    page =urllib.request.urlopen(url)
    html = "D:\/pyrequest\/common"
    for line in page.readlines():
        html = html+str(line)+"\n"
        return html
class test_praise(unittest.TestCase):
#     def __init__(self,key,value):
#         unittest.TestCase.__init__(self,key,value)
#         self.key = key
#         self.value = value

    def setUp(self):
        self.url = "http://119.27.167.20:8083/collection/favorite.json"
        self.url2 = "http://119.27.167.20:8083/member/login.json"
        self.url3 = "http://119.27.167.20:8083/collection/lists.json"
        self.url4="http://119.27.167.20:8083/collection/modfavorite.json"
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
    def test_creatcollection(self):
        
        
        str = ''.join(random.sample(string.ascii_letters + string.digits, 5))
      
        parms = {'name':str}
        r = requests.post(self.url,params=parms,headers=test_praise.common_header(self))
        code=r.json()['code']
        msg=r.json()['msg']
        
        
        
        print('创建收藏夹')
       
        if    self.assertEqual(code,200, 'Fail'):
            print('创建成功')
            
            
        else:
            if msg == "该名称收藏夹已经存在":
                print('收藏夹名字重复')
            else:
                print('创建失败')
                print(r.json())
                
           
                
            
    def test_getcollectionlist(self):
        r= requests.get(self.url3, headers=test_praise.common_header(self))
       
        self.assertEqual(r.status_code, 200 , 'fail')
              
    def test_changecollectionname(self):
        strrandom = ''.join(random.sample(string.ascii_letters + string.digits, 5))
       
        
        params={'name':strrandom,'id':'26hjgyech5ha'}
        r = requests.post(self.url4,data=params,headers=test_praise.common_header(self))
        
        msg = r.json()['msg']
       
        if r.status_code == 200:
            print("修改成功")
            
        if msg=='该收藏夹已经存在':
                
                
            print('修改失败',r.json())
        else:
            print('修改失败')        
    def test_singelcollectionlist(self):
        
        params={'page':'1','row':'20','id':'26j2fn2xlq96'}
        r =requests.get(self.url5,params=params,headers=test_praise.common_header(self))
        
        try :
            self.assertEqual(r.status_code,200)
            print('查询成功')
        except:
            
            print('查询失败',r.json())
    def test_praise(self):
        id =test_get_list(self)
        print(id)
        
        params={'relation_id':id,'type':'1'}
        r=requests.post(self.url6,params=params,headers=test_praise.common_header(self))
        
        tag=r.json()['data']['tag']
        try:
            if tag==1:
                
                
                print('点赞成功')
            if tag==0:
                print('取消点赞成功') 
        except:
            print('点赞失败',r.json())    
               
    def test_coverpraise(self):
        url='http://119.27.167.20:8083/upvote/cover.json' 
        params={'user_id':'f4bf401bc5c89ff1'}  
        r=requests.post(url,params=params,headers=test_praise.common_header(self)) 
        
        try:
            self.assertEqual(r.json()['msg'],'不能给自己封面点赞，快去邀请好友来帮你赞赞吧！','fail')
            print('自身点赞封面测试成功')
        except:
            print('测试失败')
            print(r.json())
            
    
    
if __name__ == '__main__':
    unittest.main()    