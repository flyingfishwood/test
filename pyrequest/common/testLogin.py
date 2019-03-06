import requests
import json
import hashlib

login_url = 'http://tpi.zhonju.cn/member/login/skey.json'


class Login:
    def __init__(self, username, password, member_id):
        self.username = username
        self.password = password
        self.member_id = member_id

    def get_cookie(self):
        s = requests.Session()
        payload = {'account': self.username}
        response = s.get(login_url, data=payload)
        cookies = response.cookies.get_dict()
        return json.dumps(cookies)

    def obtain_cookie(self):
        login_cookie = json.loads(self.get_cookie())
        return login_cookie

    def set_key(self):
        par1 = {'account': self.username}
        r = requests.get(login_url, params=par1)
        r.cookies.get_dict()  # 转换成字典
        key = json.loads(r.text)['data']['key']
        return key

    def set_hashlib(self):
        m_value = (self.username + self.password).encode("utf-8")
        return m_value

    def md5value(self):
        m = hashlib.md5()
        m.update(self.set_hashlib())
        md5_one_result = m.hexdigest()
        return md5_one_result

    def combination(self):
        m = hashlib.md5()
        m.update((self.member_id + self.md5value()).encode("utf-8"))
        md5_two_result = m.hexdigest()
        return md5_two_result

    def set_md5(self):
        m = hashlib.md5()
        m.update((self.combination() + self.set_key()).encode("utf-8"))
        md5_last_result = m.hexdigest()
        return md5_last_result

    def login_stmbuy(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://api2.zhonju.cn/'
        }
        login_in_url = "http://tpi.zhonju.cn/login/in.json"
        par2 = {'account': self.username, 'password': self.set_md5(), 'remember': 0}
        r = requests.put(login_in_url, params=par2, headers=headers, cookies=self.obtain_cookie(), verify=False)
        cookies = r.cookies.get_dict()
        return json.dumps(cookies)

    def keep_cookie(self):
        login_cookie = json.loads(self.login_stmbuy())
        return login_cookie


if __name__ == "__main__":
    print(Login('yu2020', 'a123456', '1k1scr1n76lz').keep_cookie())
    print(Login('yu2020', 'a123456', '1k1scr1n76lz').set_key())
