import urllib.request
import requests
import unittest
import json
import utils
import hmac
import hashlib
# from  base64 import b64decode
# from base64 import b64encode
# from Crypto import Random
# from Crypto.Cipher import AES





def getHtml(url):
    page =urllib.request.urlopen(url)
    html = "D:\/pyrequest\/common"
    for line in page.readlines():
        html = html+str(line)+"\n"
        return html
class Get_Order(unittest.TestCase):
#     def __init__(self,key,value):
#         unittest.TestCase.__init__(self,key,value)
#         self.key = key
#         self.value = value

    def setUp(self):
        self.url = "http://119.27.167.20:8083/order.json"
        self.url2 = "http://119.27.167.20:8083/member/login.json"
        self.url3 = "http://119.27.167.20:8083/member/randstr.json"
        self.url4 = "http://119.27.167.20:8083/order/pay.json"
    def test_login_order(self):
        parm={'telephone':'15882481462','captcha':'123456'}
        r = requests.post(self.url2,data=parm)
        token=r.json()['data']['token']
       
        
        
        return token
    
    def get_user_id(self): 
        parm={'telephone':'15882481462','captcha':'123456'}
        r = requests.post(self.url2,data=parm)
        user_id=r.json()['data']['_id']
        print(user_id,'yonghu')
        return  user_id
          
    def jm_sha256(self):
        
        key = Get_Order.get_user_id(self)
       
        value = '123456'
        
        
        hsobj = hashlib.sha256(key.encode("utf-8"))
        hsobj.update(value.encode("utf-8"))
        
        return hsobj.hexdigest().upper()
        
    
#         h4 = hashlib.sha256('123456')
# 
#         h1.hexdigest()
    def test_hmac_sha256(self):
        key = Get_Order.get_user_id(self)
        print(key)
       
        value = '123456'
        message = value.encode('utf-8')
        print(hmac.new(key.encode('utf-8'), message, digestmod=hashlib.sha256).hexdigest().upper(),'T')
        return hmac.new(key.encode('utf-8'), message, digestmod=hashlib.sha256).hexdigest().upper()
        
        
        
        
    
    def jm_md5(self):
        key2 = Get_Order.get_randstr(self)
        
        
        value2 = Get_Order.test_hmac_sha256(self)
      
        
        
        hsobj = hashlib.md5(key2.encode("utf-8"))
        hsobj.update(value2.encode("utf-8"))
        
        return hsobj.hexdigest().upper()
    def test_hmac_md5(self):
        
        key3 = Get_Order.get_randstr(self)
        
        
        value3 = Get_Order.test_hmac_sha256(self)
        
        message = value3.encode('utf-8')
        print(hmac.new(key3.encode('utf-8'), message, digestmod=hashlib.md5).hexdigest().upper(),'zuizhong')
        return hmac.new(key3.encode('utf-8'), message, digestmod=hashlib.md5).hexdigest().upper()
        
        
        
#     def _password(self):
#         par = '123456'
# #         userid=Get_Order.get_user_id(self)
#         
#         
# #         str ='%s,%s'%(par,userid)
#         str = par+userid
#         
#         basic_pd = Get_Order.jm_sha256(str)
#         print(basic_pd,'b')
#         str2 = Get_Order.get_randstr(self)+basic_pd
#         print(str2)
#         finally_pd =Get_Order.jm_md5(Get_Order.get_randstr(self)+basic_pd)
#         
#         
#         
#         
#         return finally_pd
#     
        
        
        
    def test_header(self):
        
        
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://119.27.167.20/',
            'token':Get_Order.test_login_order(self)
        }
        
        
        return headers
    
#     def test_buy(self):
#         token= Get_Order.test_login_order(self)
#         header = Get_Order.test_header(self)
# #         print(token,"T")
# #         print(header)
#           
#          
#           
#         parm={'dem_spec_id':'24gvxnasy8k8','num':'1','adr_id':'23i1q25yi1ez','note':'','buy_type':'1','reserve_time':''}
#         r = requests.post(self.url,headers=header,data=parm,verify=False)
#           
#         print(token)
#         print(r.json())
#         order_id = r.json()['data']['_id']
#         self.assertEqual(r.status_code, 200,'fail')
#         return order_id
    def get_randstr(self):
        token= Get_Order.test_login_order(self)
        header = Get_Order.test_header(self)
        s = requests.get(self.url3, headers = header )
        id=s.json()['data']
        print(id)
        
        return id
#     def test_pay_order(self):
#         par2 ={'order_id':Get_Order.test_buy(self),'pay_way':'balance','pay_password':Get_Order.hmac_md5(self)}    
#           
#         print(par2)
#         token= Get_Order.test_login_order(self)
#         header = Get_Order.test_header(self)
#           
#         r = requests.post(self.url4, data=par2,headers=header,verify=False)
#           
#           
#         print(r.json())                        
#       

       

  
        
   

if __name__ == '__main__':
    unittest.main()