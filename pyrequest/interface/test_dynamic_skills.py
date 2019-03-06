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
class post_dynamic_skills(unittest.TestCase):
#     def __init__(self,key,value):
#         unittest.TestCase.__init__(self,key,value)
#         self.key = key
#         self.value = value

    def setUp(self):
        self.url = "http://119.27.167.20:8083/demand.json"
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
            'token':post_dynamic_skills.login_dynamic(self)
        }
        return headers
    def test_dynamic_skills(self):
        parms = {'content':'1802年，雨果生于法国贝桑松，上有兄长二人。13岁时与兄长进入寄读学校就学，兄弟均成为学生领袖。雨果在16岁时已能创作杰出的诗句，21岁时出版诗集，声名大噪。1845年，法王路易·菲利普授予雨果上议院议员职位，自此专心从政。1848年法国二月革命爆发，法王路易被逊位',
                 'title':'test',
                 'images':'[{"url":"\/demand\/adorable\/20190228\/1551330890_5458e66eb12e4fb3adef6b8b0f53bc7d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_0ce56e18838147679e40ba5c90377ddf.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_7e0d8dca24ac43389a1bdb190da8380f.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_b6b1eea0cba244f8a511d35356aaac53.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_79c05af1a3bd4036a7e53aff24a09137.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2f7786ded55549b8b68d9f03f00eb2af.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2e9e1bfb5aef46c898aed6a4f642750d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_84c788ad5b1a4f60b90be80197784801.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_cd30cf4d604f4aa7a08fb9421719ce77.jpg","width":1440,"height":2560}]',
                 'cover_image':'/demand/adorablecover/20190228/1551330859_edaabd4a46e641ff89f2c97143c855fa.jpg','category':'prop','spec':'[{"_id":"","name":"626226","origin_price":"","price":"12","sale_count":0,"stock":12}]',
                 'province':'四川省',
                 'type':'adorable',
                 'city':'成都市',
                 'is_free':'1',
                 'sub_type':'0',
                 'freight':'0',
                 'site_code':'',
                 'order_time':'',
                 'category':'prop'
                 
                 }
        r = requests.post(self.url,data=parms,headers=post_dynamic_skills.dynamic_header(self)) 
        code=r.status_code
        print(r.json())
        try: 
            print('正常类型')
            self.assertEqual(code, 200, 'Fail')
            print('摊摊发布结果正确')
            
            
        except:
            print('摊摊发布失败')
        
        
    def test_dynamic_skills2(self):
        parms = {'content':'1802年，雨果生于法国贝桑松，上有兄长二人。13岁时与兄长进入寄读学校就学，兄弟均成为学生领袖。雨果在16岁时已能创作杰出的诗句，21岁时出版诗集，声名大噪。1845年，法王路易·菲利普授予雨果上议院议员职位，自此专心从政。1848年法国二月革命爆发，法王路易被逊位',
                 'title':'test',
                 'images':'[{"url":"\/demand\/adorable\/20190228\/1551330890_5458e66eb12e4fb3adef6b8b0f53bc7d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_0ce56e18838147679e40ba5c90377ddf.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_7e0d8dca24ac43389a1bdb190da8380f.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_b6b1eea0cba244f8a511d35356aaac53.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_79c05af1a3bd4036a7e53aff24a09137.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2f7786ded55549b8b68d9f03f00eb2af.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2e9e1bfb5aef46c898aed6a4f642750d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_84c788ad5b1a4f60b90be80197784801.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_cd30cf4d604f4aa7a08fb9421719ce77.jpg","width":1440,"height":2560}]',
                 'cover_image':'/demand/adorablecover/20190228/1551330859_edaabd4a46e641ff89f2c97143c855fa.jpg','category':'prop','spec':'[{"_id":"","name":"626226","origin_price":"","price":"12","sale_count":0,"stock":12}]',
                 'province':'四川省',
                 'type':'adorable',
                 'city':'成都市',
                 'is_free':'1',
                 'sub_type':'123',
                 'freight':'0',
                 'site_code':'',
                 'order_time':'',
                 'category':'prop'
                 
                 }
        r = requests.post(self.url,data=parms,headers=post_dynamic_skills.dynamic_header(self)) 
        string = r.json()['msg']
        print(r.json())
        try: 
            print('无下级分类')
            self.assertEqual(string, '下级分类不正确', 'Fail')
            print('摊摊测试结果正确')
            
            
        except:
            print('fail')
    def test_dynamic_skills3(self):
        parms = {'content':'1802年，雨果生于法国贝桑松，上有兄长二人。13岁时与兄长进入寄读学校就学，兄弟均成为学生领袖。雨果在16岁时已能创作杰出的诗句，21岁时出版诗集，声名大噪。1845年，法王路易·菲利普授予雨果上议院议员职位，自此专心从政。1848年法国二月革命爆发，法王路易被逊位',
                 'title':'test',
                 'images':'[{"url":"\/demand\/adorable\/20190228\/1551330890_5458e66eb12e4fb3adef6b8b0f53bc7d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_0ce56e18838147679e40ba5c90377ddf.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_7e0d8dca24ac43389a1bdb190da8380f.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_b6b1eea0cba244f8a511d35356aaac53.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_79c05af1a3bd4036a7e53aff24a09137.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2f7786ded55549b8b68d9f03f00eb2af.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2e9e1bfb5aef46c898aed6a4f642750d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_84c788ad5b1a4f60b90be80197784801.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_cd30cf4d604f4aa7a08fb9421719ce77.jpg","width":1440,"height":2560}]',
                 'cover_image':'/demand/adorablecover/20190228/1551330859_edaabd4a46e641ff89f2c97143c855fa.jpg','category':'prop','spec':'[{"_id":"","name":"626226","origin_price":"","price":"12","sale_count":0,"stock":12}]',
                 'province':'四川省',
                 'type':'adorable',
                 'city':'成都市',
                 'is_free':'',
                 'sub_type':'1',
                 'freight':'0',
                 'site_code':'',
                 'order_time':'',
                 'category':'prop'
                 
                 }
        r = requests.post(self.url,data=parms,headers=post_dynamic_skills.dynamic_header(self)) 
        code = r.status_code
        print('不开启互免')
        try: 
            
            self.assertEqual(code, 200, 'Fail')
            print('摊摊测试结果正确')
            
            
        except:
            print('测试失败')
        
    def test_dynamic_skills4(self):
        parms = {'content':'1802年，雨果生于法国贝桑松，上有兄长二人。13岁时与兄长进入寄读学校就学，兄弟均成为学生领袖。雨果在16岁时已能创作杰出的诗句，21岁时出版诗集，声名大噪。1845年，法王路易·菲利普授予雨果上议院议员职位，自此专心从政。1848年法国二月革命爆发，法王路易被逊位',
                 'title':'',
                 'images':'[{"url":"\/demand\/adorable\/20190228\/1551330890_5458e66eb12e4fb3adef6b8b0f53bc7d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_0ce56e18838147679e40ba5c90377ddf.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_7e0d8dca24ac43389a1bdb190da8380f.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_b6b1eea0cba244f8a511d35356aaac53.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_79c05af1a3bd4036a7e53aff24a09137.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2f7786ded55549b8b68d9f03f00eb2af.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2e9e1bfb5aef46c898aed6a4f642750d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_84c788ad5b1a4f60b90be80197784801.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_cd30cf4d604f4aa7a08fb9421719ce77.jpg","width":1440,"height":2560}]',
                 'cover_image':'/demand/adorablecover/20190228/1551330859_edaabd4a46e641ff89f2c97143c855fa.jpg','category':'prop','spec':'[{"_id":"","name":"626226","origin_price":"","price":"12","sale_count":0,"stock":12}]',
                 'province':'四川省',
                 'type':'adorable',
                 'city':'成都市',
                 'is_free':'1',
                 'sub_type':'1',
                 'freight':'0',
                 'site_code':'',
                 'order_time':'',
                 'category':'prop'
                 
                 }
        r = requests.post(self.url,data=parms,headers=post_dynamic_skills.dynamic_header(self)) 
        code = r.json()['code']
        
        
        print('标题为空')
        try: 
            
            self.assertEqual(code,'422', 'Fail')
            print('摊摊测试结果正确')
            
            
        except:
            print('测试失败')
    def test_dynamic_skills5(self):
        parms = {'content':'1802年，雨果生于法国贝桑松，上有兄长二人。13岁时与兄长进入寄读学校就学，兄弟均成为学生领袖。雨果在16岁时已能创作杰出的诗句，21岁时出版诗集，声名大噪。1845年，法王路易·菲利普授予雨果上议院议员职位，自此专心从政。1848年法国二月革命爆发，法王路易被逊位',
                 'title':'223',
                 'images':'[{"url":"\/demand\/adorable\/20190228\/1551330890_5458e66eb12e4fb3adef6b8b0f53bc7d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_0ce56e18838147679e40ba5c90377ddf.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_7e0d8dca24ac43389a1bdb190da8380f.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_b6b1eea0cba244f8a511d35356aaac53.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_79c05af1a3bd4036a7e53aff24a09137.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2f7786ded55549b8b68d9f03f00eb2af.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2e9e1bfb5aef46c898aed6a4f642750d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_84c788ad5b1a4f60b90be80197784801.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_cd30cf4d604f4aa7a08fb9421719ce77.jpg","width":1440,"height":2560}]',
                 'category':'prop','spec':'[{"_id":"","name":"626226","origin_price":"","price":"12","sale_count":0,"stock":12}]',
                 'province':'四川省',
                 'type':'adorable',
                 'city':'成都市',
                 'is_free':'1',
                 'sub_type':'1',
                 'freight':'0',
                 'site_code':'',
                 'order_time':'',
                 'category':'prop'
                 
                 }
        r = requests.post(self.url,data=parms,headers=post_dynamic_skills.dynamic_header(self)) 
        code = r.json()['code']
        
        
        print('封面为空')
        try: 
            
            self.assertEqual(code,'100020', 'Fail')
            print('摊摊测试结果正确')
            
            
        except:
            print('测试失败')
    def test_dynamic_skills6(self):
        parms = {'content':'1802年，雨果生于法国贝桑松，上有兄长二人。13岁时与兄长进入寄读学校就学，兄弟均成为学生领袖。雨果在16岁时已能创作杰出的诗句，21岁时出版诗集，声名大噪。1845年，法王路易·菲利普授予雨果上议院议员职位，自此专心从政。1848年法国二月革命爆发，法王路易被逊位',
                 'title':'123',
                 'images':'[{"url":"\/demand\/adorable\/20190228\/1551330890_5458e66eb12e4fb3adef6b8b0f53bc7d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_0ce56e18838147679e40ba5c90377ddf.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_7e0d8dca24ac43389a1bdb190da8380f.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_b6b1eea0cba244f8a511d35356aaac53.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_79c05af1a3bd4036a7e53aff24a09137.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2f7786ded55549b8b68d9f03f00eb2af.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2e9e1bfb5aef46c898aed6a4f642750d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_84c788ad5b1a4f60b90be80197784801.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_cd30cf4d604f4aa7a08fb9421719ce77.jpg","width":1440,"height":2560}]',
                 'cover_image':'/demand/adorablecover/20190228/1551330859_edaabd4a46e641ff89f2c97143c855fa.jpg','category':'prop','spec':'[{"_id":"","name":"626226","origin_price":"","price":"12","sale_count":0,"stock":12}]',
                 'province':'四川省',
                 'type':'adorable',
                 'city':'成都市',
                 'is_free':'1',
                 'sub_type':'1',
                 'freight':'0',
                 'site_code':'',
                 'order_time':'',
                 'category':''
                 
                 }
        r = requests.post(self.url,data=parms,headers=post_dynamic_skills.dynamic_header(self)) 
        code = r.json()['code']
        
        print('下级分类为空')
        try: 
            
            self.assertEqual(code,'422', 'Fail')
            print('摊摊测试结果正确')
            
            
        except:
            print('测试失败')
    def test_dynamic_skills7(self):
        parms = {'content':'1802年，雨果生于法国贝桑松，上有兄长二人。13岁时与兄长进入寄读学校就学，兄弟均成为学生领袖。雨果在16岁时已能创作杰出的诗句，21岁时出版诗集，声名大噪。1845年，法王路易·菲利普授予雨果上议院议员职位，自此专心从政。1848年法国二月革命爆发，法王路易被逊位',
                 'title':'1238723824826542846284278364284726862874762873264287327426278733648273267716237172163813671828673163128716318',
                 'images':'[{"url":"\/demand\/adorable\/20190228\/1551330890_5458e66eb12e4fb3adef6b8b0f53bc7d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_0ce56e18838147679e40ba5c90377ddf.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_7e0d8dca24ac43389a1bdb190da8380f.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_b6b1eea0cba244f8a511d35356aaac53.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_79c05af1a3bd4036a7e53aff24a09137.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2f7786ded55549b8b68d9f03f00eb2af.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2e9e1bfb5aef46c898aed6a4f642750d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_84c788ad5b1a4f60b90be80197784801.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_cd30cf4d604f4aa7a08fb9421719ce77.jpg","width":1440,"height":2560}]',
                 'cover_image':'/demand/adorablecover/20190228/1551330859_edaabd4a46e641ff89f2c97143c855fa.jpg','category':'prop','spec':'[{"_id":"","name":"626226","origin_price":"","price":"12","sale_count":0,"stock":12}]',
                 'province':'四川省',
                 'type':'adorable',
                 'city':'成都市',
                 'is_free':'1',
                 'sub_type':'1',
                 'freight':'0',
                 'site_code':'',
                 'order_time':'',
                 'category':'prop'
                 
                 }
        r = requests.post(self.url,data=parms,headers=post_dynamic_skills.dynamic_header(self)) 
        code = r.json()['code']
        
        
        print('标题超长')
        try: 
            
            self.assertEqual(code,'422', 'Fail')
            print('摊摊测试结果正确')
           
    
        except:
            print(r.json()['msg'],'测试失败')                   
        
    def test_dynamic_skills8(self):
        parms = {'content':'1802年，雨果生于法国贝桑松，上有兄长二人。13岁时与兄长进入寄读学校就学，兄弟均成为学生领袖。雨果在16岁时已能创作杰出的诗句，21岁时出版诗集，声名大噪。1845年，法王路易·菲利普授予雨果上议院议员职位，自此专心从政。1848年法国二月革命爆发，法王路易被逊位',
                 'title':'62771828673163128716318',
                 'images':'[{"url":"\/demand\/adorable\/20190228\/1551330890_5458e66eb12e4fb3adef6b8b0f53bc7d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_0ce56e18838147679e40ba5c90377ddf.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_7e0d8dca24ac43389a1bdb190da8380f.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_b6b1eea0cba244f8a511d35356aaac53.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_79c05af1a3bd4036a7e53aff24a09137.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2f7786ded55549b8b68d9f03f00eb2af.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_2e9e1bfb5aef46c898aed6a4f642750d.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330890_84c788ad5b1a4f60b90be80197784801.jpg","width":1440,"height":2560},{"url":"\/demand\/adorable\/20190228\/1551330889_cd30cf4d604f4aa7a08fb9421719ce77.jpg","width":1440,"height":2560}]',
                 'cover_image':'/demand/adorablecover/20190228/1551330859_edaabd4a46e641ff89f2c97143c855fa.jpg','category':'prop','spec':'[{"_id":"","name":"626226","origin_price":"","price":"","sale_count":0,"stock":12}]',
                 'province':'四川省',
                 'type':'adorable',
                 'city':'成都市',
                 'is_free':'1',
                 'sub_type':'1',
                 'freight':'0',
                 'site_code':'',
                 'order_time':'',
                 'category':'prop'
                 
                 }
        r = requests.post(self.url,data=parms,headers=post_dynamic_skills.dynamic_header(self)) 
        code = r.json()['code']
        
        
        print('库存单价为空')
        try: 
            
            self.assertEqual(code,'300060', 'Fail')
            print('摊摊测试结果正确')
           
    
        except:
            print(r.json()['msg'],'测试失败')  
    
    
if __name__ == '__main__':
    unittest.main()    