from seleniumbase import DriverContext
from selenium.common.exceptions import (
    ElementNotInteractableException,
    ElementClickInterceptedException,
)
from selenium.webdriver.common.alert import Alert
import hcaptcha_challenger as solver
from hcaptcha_challenger import HolyChallenger
from hcaptcha_challenger.exceptions import ChallengePassed
import undetected_chromedriver as uc
import typing
import time
import requests as rq
import random
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc
solver.install()
def hit_challenge(ctx, challenger: HolyChallenger, retries: int = 10) -> typing.Optional[str]:
    """
    Use `anti_checkbox()` `anti_hcaptcha()` to be flexible to challenges
    :param ctx:
    :param challenger:
    :param retries:
    :return:
    """
    if challenger.utils.face_the_checkbox(ctx):
        challenger.anti_checkbox(ctx)
        if res := challenger.utils.get_hcaptcha_response(ctx):
            return res

    for _ in range(retries):
        try:
            if (resp := challenger.anti_hcaptcha(ctx)) is None:
                continue
            if resp == challenger.CHALLENGE_SUCCESS:
                return challenger.utils.get_hcaptcha_response(ctx)
        except ChallengePassed:
            return challenger.utils.get_hcaptcha_response(ctx)
        challenger.utils.refresh(ctx)
        time.sleep(1)

def bytedance(email,password):
    capabilities = DesiredCapabilities.CHROME
     # capabilities["loggingPrefs"] = {"performance": "ALL"}  # chromedriver < ~75
    capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

    with DriverContext(uc=True,locale_code='en-US',cap_string=capabilities,extension_zip='captchaH.zip',extension_dir='captchaH' ) as driver:
        try:
            driver.get('https://config.nocaptchaai.com/?apikey=izzycode-9afa825a-1270-cda3-b129-1779369b31df&plan=PRO') 
            alert = Alert(driver)
            alert.accept()
            time.sleep(1)
            handles = driver.window_handles
            driver.switch_to.window(handles[0])         
            driver.get('https://www.papara.com/')
            text = ''
            print('At The Browser')
            while text != "6 Haneli Şifreni Gir":
                time.sleep(random.uniform(1, 2))
                WebDriverWait(driver, 5, ignored_exceptions=(ElementClickInterceptedException,)).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarContent"]/ul[2]/li[7]/a[2]'))
                ).click()
                time.sleep(random.uniform(1, 2))
                for i in email:
                    time.sleep(random.uniform(0, 1))
                    WebDriverWait(driver, 15, ignored_exceptions=(ElementNotInteractableException,)).until(
                        EC.presence_of_element_located((By.ID, ":r0:-input"))
                    ).send_keys(i)
                WebDriverWait(driver, 5, ignored_exceptions=(ElementClickInterceptedException,)).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[1]/a'))
                ).click()
                # Handling context validation
                time.sleep(20)                          
                # Submit test data ok
                try:
                    text = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[1]/div[1]/div[1]/h2').text
                except:
                    print('Captchayı aşamadık agam')
            cookies = driver.get_cookies()
            logs = driver.get_log("performance")
            token = str(logs).split("P1_")[1].split('\\\\"')[0]
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
                    "token": str(logs).split("P1_")[1].split('\\\\"')[0],
                    "success": "true"
                }
        except Exception as e:
                print(e)
                informations = {
                    "success": "false"
                }
                return informations
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
    json2 = {"phoneNumber":f"{email}","humanVerificationToken":f"P1_{token}","platform":0}
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
            