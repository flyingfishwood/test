import urllib.request
import requests
import unittest
import json
import utils
import hmac
import hashlib
import string
import xlrd
import data
import con_login
from asyncio.tasks import sleep
import read
import random

def getHtml(url):
    page =urllib.request.urlopen(url)
    html = "D:\/pyrequest\/common"
    for line in page.readlines():
        html = html+str(line)+"\n"
        return html
class v_2_2(unittest.TestCase):
#     def __init__(self,key,value):
#         unittest.TestCase.__init__(self,key,value)
#         self.key = key
#         self.value = value

    def setUp(self):
        self.url = "http://119.27.167.20:8083/award_gift.json"
        self.url2 = "http://119.27.167.20:8083/member/login.json"
        self.url3 = "http://119.27.167.20:8083/dynamic/recentaward.json"
        self.url4="http://119.27.167.20:8083/member/expinfo.json"
        self.url5="http://119.27.167.20:8083/task/sign.json"
        self.url6="http://119.27.167.20:8083/reward/ranks.json"
        self.url7="http://119.27.167.20:8083/member/addinvitedcode.json"
        self.url8="http://119.27.167.20:8083/activity/actrank.json"
    def login_common(self):
        parm={'telephone':'15882481462','captcha':'123456'}
        r = requests.post(self.url2,data=parm)
        token=r.json()['data']['token']
       
        return token
    def commom_header(self):
        
        
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'token':v_2_2.login_common(self)
        }
        return headers
    def test_awardgift(self):
        parms = {'type':'2'}
     
        r = requests.get(self.url,params=parms,headers=v_2_2.commom_header(self))
        msg=r.json()['msg']
        print('积分列表')
        
        try: 
            self.assertEqual(msg,'success', 'Fail')
            print('获取成功')
            
            
        except:
            print('获取失败',r.json())
    def test_awardgift2(self):
        parms = {'type':'1'}
     
        r = requests.get(self.url,params=parms,headers=v_2_2.commom_header(self))
        msg=r.json()['msg']
        print('药丸列表')
        
        try: 
            self.assertEqual(msg,'success', 'Fail')
            print('获取成功')
            
            
        except:
            print('获取失败',r.json()) 
    def test_recentawardgiftlist(self):
        params={'id':data.test_get_list}
        r= requests.get(self.url3, params=params)
        msg=r.json()['msg']
        print('单个圈圈最近打赏列表')
        try:
            self.assertEqual(msg,'success','fail')
            print('获取成功')
        except:
            print('获取失败',r.json())
    def test_expinfo(self):
        r= requests.get(self.url4,headers=con_login.common_header(self))
    
        print('打卡及经验显示') 
        try:
            self.assertEqual(r.json()['msg'],'success','fail')
            print('查询成功')
        except:
            print('查询失败',r.json())
            sleep(3)
    def test_sign(self):
        r=requests.post(self.url5,headers=con_login.common_header(self))
        print('签到：')
        try:
            tag=r.json()['data']
            
            msg=r.json()['msg']
            if tag == True:
                print('已经签到过了')
            
            if tag !=True:
                print('签到成功')
            
        except:
            print('签到失败',r.json())
    def test_rewardranks(self):
        r=requests.get(self.url6, headers=con_login.common_header(self)) 
        msg=r.json()['msg']
        print('奖励详情')
        try:
            self.assertEqual(msg,'success','fail')
            print('获取奖励详情成功')
        except:
            print('获取失败',r.json())                    
    def test_addinvitedcode(self):
        sheetName = 'Sheet1'
#         print(read.get_excel_data('/pyrequest/source/testinvitedcode.xlsx',sheetName))
        list=[108811,None,122342]
        value = random.sample(list,1)
        
        params={' invited_code':value}
        
        r= requests.post(self.url7, params=params, headers=con_login.common_header(self))
      
        try:
            if r.json()['msg']=='已经填写过邀请码了，不能重复填写':
                print('已经填写过邀请码了，不能重复填写,pass')
            if r.json()['code']==100020:
                print('邀请码不能为空,pass')
            if r.json()['msg']=='邀请码错误啦！怎么肥四' :
                print('邀请码错误,pass')
            if r.json()['code']==200:
                print('添加成功')
        except:
                print('invite系统异常',r.json())       
                
#         r= requests.get(url, params)
    def test_getrankact(self):
        r= requests.get(self.url8)
        try:
            self.assertEqual(r.json()['msg'],'success','fail')
            print('获取人气榜活动排行成功')
        except:
            print('获取异常',r.json())    
                                         
   
        
    
    
if __name__ == '__main__':
    unittest.main()
        