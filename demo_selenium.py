from seleniumbase import DriverContext
from selenium.common.exceptions import (
    ElementNotInteractableException,
    ElementClickInterceptedException,
)

import requests as rq
from datetime import datetime
from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc

def getcookies():
    print('Browser Started')
    capabilities = DesiredCapabilities.CHROME
    # capabilities["loggingPrefs"] = {"performance": "ALL"}  # chromedriver < ~75
    capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
    with DriverContext(uc=True,locale_code='en-US',cap_string=capabilities,headless2=True ) as driver:
        try:
            driver.get('https://www.papara.com/')
            print('At The Browser')
            cookies = driver.get_cookies()
            driver.quit()   
            for cookie in cookies:
                if cookie['name'] == "__cflb":
                    cflb = cookie['value']
                if cookie['name'] == "__cfruid":
                    cfruid = cookie['value']
                if cookie['name'] == "__cf_bm":
                    cfbm = cookie['value']
            informations = {
                    "__cflb": cflb,
                    "__cfruid": cfruid,
                    "__cf_bm": cfbm,
                    "success": "true"
                }
            return informations
        except Exception as e:
                informations = {
                    "success": "false"
                }
                return informations

def bytedance(email,password,token,cflb,cfruid,cfbm):
    
            headers = {
            "cookie": f"cookie: __cflb={cflb}; __cfruid={cfruid}; __cf_bm={cfbm}",
            "Accept": "application/json",
            "Authorization": "Bearer po9h0JSSPXdptNdTwuBHSqgA1itiZw6W_yjDN-2OBKSi_dRup6loVoyq1wPQHVbowSUuCQZ9K13nJD6gWuRf059CawWdFZUA7MgM_C07ZMfVFMAyxlzolrGTf2QObPNw5HKS6jMa5DgIJqmFm-jUOyR83CbybRB_lDgn_QT_MZxCDLFwLOwY46juR2dSZSJ0EPEs_-61Ih4G_9qVwiSuWxDK_Ch4VyQXQQhUfg-v3-DzI0TrLxsAwDd_QwrF0W0jAwDJihKjURYNvzezQpMO6CTviSotW8rvUdLkPIKgq1EAK_2w1xSobRiVZtlbSFqIZqE0egT9kN_Z3MBY5e0gatIDnEMiIMCpBaSWWyvYJWysa-_fVng9VNtoVfwgmC-8cL2LsfO6x3ZdqbyG0_NezdOn_jLzq9mG04AbjXBiiVxgjAF1TNJHre5TiJyLQktLcRQVtRfgnpVXWMHs6OflHrygrTSfsaqdVWmpXb_n1q5nI7b3",
            "Content-Type": "application/json; charset=utf-8",
            "Referer": "https://www.papara.com/personal/auth/login/sms-code",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            "access-control-allow-origin": "https://www.papara.com",
            "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "x-papara-app-dark-mode-enabled": "true",
            "x-resource-language": "tr-TR"
            }
            json2 = {"phoneNumber":f"{email}","humanVerificationToken":f"{token}","platform":0}
            generateUniqueID = rq.post(url="https://webapi.papara.com/login/phone",headers=headers,json=json2)
            passwordtoken = generateUniqueID.json()         
            print(passwordtoken)
            accesstoken = passwordtoken['data']['access_token']
            headers2 = {
                "cookie": f"cookie: __cflb={cflb}; __cfruid={cfruid}; __cf_bm={cfbm}",
                "Accept": "application/json",
                "Authorization": "Bearer "+accesstoken,
                "Content-Type": "application/json; charset=utf-8",
                "Referer": "https://www.papara.com/personal/auth/login/sms-code",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                "access-control-allow-origin": "https://www.papara.com",
                "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "x-papara-app-dark-mode-enabled": "true",
                "x-resource-language": "tr-TR"
            }
            json3 = {
                "password": str(password)
            }
            generateUniqueID = rq.post(url="https://webapi.papara.com/login/password",headers=headers2,json=json3)
            passwordtoken = generateUniqueID.json()
            accesstoken = passwordtoken['data']['access_token']
            if accesstoken != 'data':
                informations = {
                    "__cflb": cflb,
                    "__cfruid": cfruid,
                    "__cf_bm": cfbm,
                    "accesstoken": accesstoken,
                    "success": "true"
                }
            else:
                informations = {
                    "success": "is_false"
                }
            return informations    
        
def write_Verification(cflb,cfruid,cfbm,accesstoken,code):
    headers3 = {
                "cookie": f"cookie: __cflb={cflb}; __cfruid={cfruid}; __cf_bm={cfbm}",
                "Accept": "application/json",
                "Authorization": "Bearer "+accesstoken,
                "Content-Type": "application/json; charset=utf-8",
                "Referer": "https://www.papara.com/personal/auth/login/sms-code",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                "access-control-allow-origin": "https://www.papara.com",
                "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "x-papara-app-dark-mode-enabled": "true",
                "x-resource-language": "tr-TR"
            }
    json4 = {"tfaCode":f"{code}","platform":0}
    generateUniqueID = rq.post(url="https://webapi.papara.com/login/tfapush",headers=headers3,json=json4)
    passwordtoken = generateUniqueID.json()
    accesstoken = passwordtoken['data']['access_token']
    if accesstoken != 'data':
        informations = {
            "__cflb": cflb,
            "__cfruid": cfruid,
            "__cf_bm": cfbm,
            "accesstoken": accesstoken,
            "success": "true"
        }
    else:
        informations = {
            "success": "is_false"
        }
    return informations



def post_SMS(cflb,cfruid,cfbm,accesstoken,code):
    headers3 = {
                "cookie": f"cookie: __cflb={cflb}; __cfruid={cfruid}; __cf_bm={cfbm}",
                "Accept": "application/json",
                "Authorization": "Bearer "+accesstoken,
                "Content-Type": "application/json; charset=utf-8",
                "Referer": "https://www.papara.com/personal/auth/login/sms-code",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                "access-control-allow-origin": "https://www.papara.com",
                "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "x-papara-app-dark-mode-enabled": "true",
                "x-resource-language": "tr-TR"
            }
    json4 = {"platform":0,"tfaCode":f"{code}"}
    generateUniqueID = rq.post(url="https://webapi.papara.com/login/tfa",headers=headers3,json=json4)
    passwordtoken = generateUniqueID.json()
    accesstoken = passwordtoken['data']['access_token']
    if accesstoken != 'data':
        informations = {
            "__cflb": cflb,
            "__cfruid": cfruid,
            "__cf_bm": cfbm,
            "accesstoken": accesstoken,
            "success": "true"
        }
    else:
        informations = {
            "success": "is_false"
        }
    return informations

def send_SMS(cflb,cfruid,cfbm,accesstoken):
    headers3 = {
                "cookie": f"cookie: __cflb={cflb}; __cfruid={cfruid}; __cf_bm={cfbm}",
                "Accept": "application/json",
                "Authorization": "Bearer "+accesstoken,
                "Content-Type": "application/json; charset=utf-8",
                "Referer": "https://www.papara.com/personal/auth/login/sms-code",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                "access-control-allow-origin": "https://www.papara.com",
                "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "x-papara-app-dark-mode-enabled": "true",
                "x-resource-language": "tr-TR"
            }
    generateUniqueID = rq.get(url="https://webapi.papara.com/login/sendOtp",headers=headers3)
    passwordtoken = generateUniqueID.json()
    print(passwordtoken)
    accesstoken = passwordtoken['data']['access_token']
    if accesstoken != 'data':
        informations = {
            "__cflb": cflb,
            "__cfruid": cfruid,
            "__cf_bm": cfbm,
            "accesstoken": accesstoken,
            "success": "true"
        }
    else:
        informations = {
            "success": "is_false"
        }
    return informations
def checkMail_Confirmations(cflb,cfruid,cfbm,accesstoken):
    headers4 = {
        "cookie": f"cookie: __cflb={cflb}; __cfruid={cfruid}; __cf_bm={cfbm}",
        "Accept": "application/json",
        "Authorization": "Bearer "+accesstoken,
        "Content-Type": "application/json; charset=utf-8",
        "Referer": "https://www.papara.com/personal/auth/login/sms-code",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "access-control-allow-origin": "https://www.papara.com",
        "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "x-papara-app-dark-mode-enabled": "true",
        "x-resource-language": "tr-TR"
    }
    isConfirmed = rq.get(url="https://webapi.papara.com/login/isUserDeviceVerified",headers=headers4)
    passwordtoken = isConfirmed.json()
    print(passwordtoken)
    accesstoken = passwordtoken['data']['access_token']
    headers5 = {
        "cookie": f"cookie: __cflb={cflb}; __cfruid={cfruid}; __cf_bm={cfbm}; access_token={accesstoken}; check_fail_login=true; ",
        "Accept": "application/json",
        "Authorization": "Bearer "+accesstoken,
        "Content-Type": "application/json; charset=utf-8",
        "Referer": "https://www.papara.com/personal/auth/login/sms-code",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            "access-control-allow-origin": "https://www.papara.com",
        "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "x-papara-app-dark-mode-enabled": "true",
        "x-resource-language": "tr-TR"
    }
    UserInfo = rq.get(url="https://webapi.papara.com/user",headers=headers5)
    print(datetime.utcnow().strftime('%B %d %Y - %H:%M:%S')+'  |  '+'User Informations is send by Json.')
    print('Success')
    return UserInfo.json()
            