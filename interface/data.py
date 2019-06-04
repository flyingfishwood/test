import urllib.request
import requests
import unittest
import json
import utils
import con_login

    
def set(self,url2):
    self.url='http://119.27.167.20:8083/member/dynamiclists.json?user_id=f4bf401bc5c89ff1&sort=itime&page=1&row=10'    
    url2='http://119.27.167.20:8083/comment.json'
def test_get_list(self):
    
    
        
    
    r = requests.get('http://119.27.167.20:8083/dynamic/lists.json')
#         print(r.json())
    page_list = r.json()['data']['data'][0]['_id']
        
    
    return page_list
def test_get_comment_first(self):
    relationid=test_get_list(self);
    data = {'content':'测试接口评论',
                 'parent_id':'',
                 'relation_id':relationid,
                 'replied_user_id':'',
                 'voice_content':'',
                 'type':'1'}
    r=requests.post('http://119.27.167.20:8083/comment.json',params=data,headers=con_login.common_header(self))
    rel=r.json()['data']['_id']
    
    return rel
       

    
        
        
    
    
    
    
    
    
    
    
    
