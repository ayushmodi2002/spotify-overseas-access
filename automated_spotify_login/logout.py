from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def logout(driver):
    print("Attempting to logout...........")
    time.sleep(1)
    out=False
    try:
        if driver.find_element(By.CLASS_NAME,"T1xI1RTSFU7Wu94UuvE6") and driver.find_element(By.ID,"config"):
            profileclick=driver.find_element(By.CLASS_NAME,"KdxlBanhDJjzmHfqhP0X").click()
            time.sleep(5)
            logoutclick=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-testid='user-widget-dropdown-logout']"))).click()
            print("waiting 20s for browser to logout")
            time.sleep(20)
    except selenium.common.exceptions.NoSuchElementException:
        print("error report on github")
    
    print("Validating Logout...........")
    time.sleep(1)
    try:
        if WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-testid='login-button']"))):
            out=True
    except selenium.common.exceptions.NoSuchElementException:
        out=False
    
    return out
