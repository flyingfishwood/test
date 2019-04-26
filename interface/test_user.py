import urllib.request
import requests
import unittest
import json
import utils
import hmac
import hashlib
import string
import random
from con_login import *





def getHtml(url):
    page =urllib.request.urlopen(url)
    html = "D:\/pyrequest\/common"
    for line in page.readlines():
        html = html+str(line)+"\n"
        return html
class Get_user(unittest.TestCase):
    def setUp(self):
        self.url = "http://119.27.167.20:8083/sms.json"
        self.url2 = "http://119.27.167.20:8083/member/register.json"
        self.url3 = "http://119.27.167.20:8083/member/thirdlogin.json"
        self.url4="http://119.27.167.20:8083/collection/modfavorite.json"
        self.url5="http://119.27.167.20:8083/collection/favoritecontents.json"
        self.url6="http://119.27.167.20:8083/upvote.json"
    
    def test_sms_bd(self):
        params = {'telephone':'15882481462','type':'9'}
        r= requests.post(self.url,params=params)   
        
        try:
            self.assertEqual(r.json()['msg'],'success','fail')
            print('百度验证码发送正常')
        except:
            print('发送失败',r.json())    
    def test_sms_re(self):
        params = {'telephone':'15882481462','type':'3'}
        r= requests.post(self.url,params=params)   
        
        try:
            self.assertEqual(r.json()['msg'],'success','fail')
            print('注册验证码发送正常')
        except:
            print('发送失败',r.json())     
        
    def test_sms_bind(self):
        params = {'telephone':'15882481462','type':'1'}
        r= requests.post(self.url,params=params)   
        
        try:
            self.assertEqual(r.json()['msg'],'success','fail')
            print('手机绑定验证码发送正常')
        except:
            print('发送失败',r.json())     
    def test_sms_findpd(self):
        params = {'telephone':'15882481462','type':'2'}
        r= requests.post(self.url,params=params)   
        
        try:
            self.assertEqual(r.json()['msg'],'success','fail')
            print('找回密码发送正常')
        except:
            print('发送失败',r.json())     
    def test_sms_changebind(self):
        params = {'telephone':'15882481462','type':'4'}
        r= requests.post(self.url,params=params,headers=common_header(self))   
        
        try:
            self.assertEqual(r.json()['msg'],'success','fail')
            print('修改绑定手机发送正常')
        except:
            print('发送失败',r.json())
    def test_sms_answer(self):
        params = {'telephone':'15882481462','type':'8'}
        r= requests.post(self.url,params=params)   
        
        try:
            self.assertEqual(r.json()['msg'],'success','fail')
            print('答题验证码发送正常')
        except:
            print('发送失败',r.json())         
            
    def test_sms_login(self):
        params = {'telephone':'15882481462','type':'6'}
        r= requests.post(self.url,params=params)   
        
        try:
            self.assertEqual(r.json()['msg'],'success','fail')
            print('登录验证码发送正常')
        except:
            print('发送失败',r.json())         
    def test_sms_tradepd(self):
        params = {'telephone':'15882481462','type':'10'}
        r= requests.post(self.url,params=params)   
        
        try:
            self.assertEqual(r.json()['msg'],'success','fail')
            print('交易验证码发送正常')
        except:
            print('发送失败',r.json())         
            
    def test_sms_changetradepd(self):
        params = {'telephone':'15882481462','type':'11'}
        r= requests.post(self.url,params=params)   
        
        try:
            self.assertEqual(r.json()['msg'],'success','fail')
            print('修改交易密码验证码发送正常')
        except:
            print('发送失败',r.json())        
            
    def test_register(self):
        strrandom=random.randint(12700000000,19900000001)
        params ={'telephone':strrandom,'captcha':'123456','invited_code':''}
        r= requests.post(self.url2, params=params)
        
        try:
            self.assertEqual(r.status_code,200,'fail')
            print('无邀请码注册成功')
        except:
            print('注册失败',r.json())    
        
              
    def test_register2(self):
        strrandom=random.randint(12700000000,19900000001)
        params ={'telephone':strrandom,'captcha':'123456','invited_code':'108811'}
        r= requests.post(self.url2, params=params)
        
        try:
            self.assertEqual(r.status_code,200,'fail')
            print('有邀请码注册成功')
        except:
            print('注册失败',r.json())         
            
    def test_register3(self):
        strrandom=random.randint(12700000000,19900000001)
        params ={'telephone':strrandom,'captcha':'123456','invited_code':'999'}
        r= requests.post(self.url2, params=params)
        
        try:
            self.assertEqual(r.json()['code'],200004,'fail')
            print('错误邀请码测试正确')
        except:
            print('注册失败',r.json())
    def test_thirdlogin(self):
#         strrandom=random.randint(12700000000,19900000001)
        params ={'telephone':'15882481462','qq_openid':'BA3F2D88EA4F1AB72C9BEDB3A877A689','type':'1'}
        r= requests.post(self.url3, params=params)
        
        try:
            self.assertEqual(r.json()['msg'],'success','fail')
            print('qq三方登录成功')
        except:
            print('登录失败',r.json())                 
    def test_thirdlogin2(self):
#         strrandom=random.randint(12700000000,19900000001)
        params ={'wx_openid':'oRbznw-scYQ3qMVKIMsPHBoIcXxI','type':'2'}
        r= requests.post(self.url3, params=params)
        
        
        try:
            self.assertEqual(r.json()['code'],200033,'fail')
            print('未注册微信三方登录成功')
        except:
            print("登录失败 ")  
            
    def test_thirdlogin3(self):
#         strrandom=random.randint(12700000000,19900000001)
        params ={'wb_openid':'5523464653','type':'3'}
        r= requests.post(self.url3, params=params)
        
        
        try:
            self.assertEqual(r.json()['msg'],'success','fail')
            print('微博登录成功')
        except:
            print("登录失败 ")        
            
            
            
            
            
            
            
                
if __name__ == '__main__':
    unittest.main()           