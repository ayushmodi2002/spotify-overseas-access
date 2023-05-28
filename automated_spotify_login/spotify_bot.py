from login import login
import time
from myfirebase import db,cred
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from logout import logout 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from emails import successmail,unsuccessmail
from encryptdecrypt import decrypt,loadkeys
import sys

def spotifylogbot():
    verify_check=False
    print("fetching data from firebase...........")
    users = db.collection('users').get()
    time.sleep(2)

    for user in users:
        log=False
        privatekey,publickey=loadkeys()
        temp=user.to_dict()
        username=temp.get('email')
        pwd=temp.get('password')
        password=decrypt(pwd,privatekey)
        # time.sleep(2)
        def chromeinit():
            try:
                #headless code
                chromeoptions=Options()
                chromeoptions.add_argument('--headless')
                chromeoptions.add_argument('--no-sandbox')
                chromeoptions.add_argument('--disable-dev-shm-usage')
                #creates webdriver for linux
                temp=webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chromeoptions)
            except OSError: 
                #windows chrome web
                options= webdriver.ChromeOptions()
                options.add_experimental_option("detach",True)
                temp=webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

            print("Chrome Driver ready. launching in 5s...........")
            time.sleep(5)
            return temp
        driver=chromeinit()
        log = login(username,password,driver)
        if log==True:
            print("Login Successful")
            print('waiting for 120s to ensure spotify recognizes your ip...........')
            time.sleep(120)
            out=logout(driver)
            if out==True:
                print("logged out successfuly!")
                successmail(username)
                verify_check=True
                driver.close() 
                driver.quit()
            elif out==False:
                print("Unsuccessful Attempt to Logout! report a bug on github if problem persists")
                unsuccessmail(username)
                verify_check=False
                driver.close()
                driver.quit()
        elif log==False:
            print("unsuccessfull attempt! Try again. Maybe invalid credentials")
            unsuccessmail(username)
            verify_check=False

    print("Liked My work ?? support me on github @ayushmodi_2002") 
    return verify_check

