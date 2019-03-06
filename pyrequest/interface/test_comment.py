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
class post_comment(unittest.TestCase):
#     def __init__(self,key,value):
#         unittest.TestCase.__init__(self,key,value)
#         self.key = key
#         self.value = value

    def setUp(self):
        self.url = "http://119.27.167.20:8083/comment.json"
        self.url2 = "http://119.27.167.20:8083/member/login.json"
        self.url3 = "http://119.27.167.20:8083/comment.json"
        self.url4="http://119.27.167.20:8083/collection/lists.json"
        
    def login_comment(self):
        parm={'telephone':'15882481462','captcha':'123456'}
        r = requests.post(self.url2,data=parm)
        token=r.json()['data']['token']
       
        return token
    def comment_header(self):
        
        
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'token':post_comment.login_comment(self)
        }
        return headers
    def test_comment(self):
        parms = {'content':'测试接口评论','parent_id':'','relation_id':'26d6eleaiagt',
                 'replied_user_id':'',
                 'type':'1'}
        r = requests.post(self.url,data=parms,headers=post_comment.comment_header(self))
        code=r.status_code
        print('正常评论')
        
        try: 
            self.assertEqual(code, 200, 'Fail')
            print('评论发布结果正确')
            
            
        except:
            print('评论发布失败')
      
    def test_comment2(self):
        parms = {'content':'','parent_id':'','relation_id':'26d6eleaiagt',
                 'replied_user_id':'',
                 'type':'1'}
        r = requests.post(self.url,data=parms,headers=post_comment.comment_header(self))
        
        code=r.json()['code']
        print('评论内容为空')
        
        try: 
            self.assertEqual(int(code), 300104, 'Fail')
            print('评论发布结果正确')
            
            
        except:
            print('评论发布失败')
    def test_get_commentlist(self):
        parm={'ID':'26d6eleaiagt','type':'1'} 
        print(parm)
        
        r = requests.get(self.url3,data=parm,headers=post_comment.comment_header(self)) 
        
        print(r.json())      
    def test_get_collectionlist(self):
       
        print('获取收藏夹')
        r = requests.get(self.url4,headers=post_comment.comment_header(self)) 
        print( r.status_code)
        if r.status_code==200:
            print('结果正确')
        else: 
            print('结果错误')
        
        
    
    
if __name__ == '__main__':
    unittest.main()    