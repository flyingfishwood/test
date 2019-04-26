import urllib.request
import requests
import unittest
import json
import utils


    
    
def test_get_list(self):
    
    
        
    
    r = requests.get('http://119.27.167.20:8083/dynamic/lists.json')
#         print(r.json())
    page_list = r.json()['data']['data'][0]['_id']
        
    
    return page_list
     
    
    
    
    
    
    
    
    
    
