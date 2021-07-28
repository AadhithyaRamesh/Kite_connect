from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import urllib.parse as urlparse
from selenium.webdriver.chrome.options import Options
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import pandas as pd
import datetime
import joblib
import pdb
import logging
logging.basicConfig(level=logging.ERROR)

# pip3 install selenium
# pip3 install urllib3

class ZerodhaRequestToken:
    def __init__(self):
        self.apiKey = '9d0gkan3mpw88evk'
        self.apiSecret = 'a6ypingsg5omsltkw9bgy6la3d0znsna'
        self.accountUserName = 'YX0113'
        self.accountPassword = 'aadhithya9z'
        self.securityPin = '283003'

    def getrequesttoken(self):
        try:
            login_url = "https://kite.trade/connect/login?v=3&api_key={apiKey}".format(apiKey=self.apiKey)

            chrome_driver_path = "D:/py36/lib/site-packages/chromedriver_win32/chromedriver.exe"
            options = Options()
            options.add_argument('--headless') #for headless
            driver = webdriver.Chrome(chrome_driver_path, options=options)
            # driver = webdriver.Chrome(options = options)
            driver.get(login_url)
            wait = WebDriverWait(driver, 35)
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="text"]')))\
                .send_keys(self.accountUserName)
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))\
                .send_keys(self.accountPassword)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))\
                .submit()
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))).click()
            time.sleep(35)
            driver.find_element_by_xpath('//input[@type="password"]').send_keys(self.securityPin)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).submit()
            wait.until(EC.url_contains('status=success'))
            tokenurl = driver.current_url
            parsed = urlparse.urlparse(tokenurl)
            driver.close()
            print("Getting request")
            print(urlparse.parse_qs(parsed.query)['request_token'][0])
            return urlparse.parse_qs(parsed.query)['request_token'][0]
        except Exception as ex:
            print(ex)

_ztoken = ZerodhaRequestToken()
actual_token = _ztoken.getrequesttoken()
print('request token : '+str(actual_token))
kite = KiteConnect(api_key=_ztoken.apiKey)
data = kite.generate_session(actual_token,api_secret=_ztoken.apiSecret)

with open('access_token.txt', 'w') as f:
    f.write(data['access_token'])

# kite.set_access_token(data["access_token"])
# print('request token : '+str(data["access_token"]))
# joblib.dump(kite,'kitefile.p')
# kws = KiteTicker(_ztoken.apiKey, data["access_token"])
#
# def auto_login():
#     global kite,kws,data,_ztoken,actual_token
#     _ztoken = ZerodhaAccessToken()
#     actual_token = _ztoken.getaccesstoken()
#     print('access token : '+str(actual_token))
#     kite = KiteConnect(api_key=_ztoken.apiKey)
#     data = kite.generate_session(actual_token,api_secret=_ztoken.apiSecret)
#     kite.set_access_token(data["access_token"])
#     print('request token : '+str(data["access_token"]))
#     joblib.dump(kite,'kitefile.p')
#     kws = KiteTicker(_ztoken.apiKey, data["access_token"])
