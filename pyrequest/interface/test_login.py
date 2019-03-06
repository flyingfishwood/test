import urllib.request
import requests
import unittest
import json
import utils





def getHtml(url):
    page =urllib.request.urlopen(url)
    html = "D:\/pyrequest\/common"
    for line in page.readlines():
        html = html+str(line)+"\n"
        return html
class GetLogin(unittest.TestCase):

    def setUp(self):
        self.url = "http://119.27.167.20:8083/member/login.json"
       
    def testlogin(self):
        parm={'telephone':'15882481462','captcha':'123456'}
        r = requests.post(self.url,data=parm)
        token=r.json()['data']['token']
        print(token)
        print(r.json())
        self.assertEqual(r.status_code, 200,'fail')
     
    

       

  
        
   

if __name__ == '__main__':
    unittest.main()