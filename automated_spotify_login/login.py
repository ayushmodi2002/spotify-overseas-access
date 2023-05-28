
import selenium

from selenium.webdriver.common.by import By
import time

def login(username,password,driver):
    log=False
    url="https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F%3F"
    
    
    #driver code
    driver.get(url)
    print("waiting for 20 seconds to ensure that browser loads completely...........")
    time.sleep(20)
    
    print("Entering Login information from Database")
    #inputs data on behalf of user
    emailbox= driver.find_element(By.ID,"login-username").send_keys(username)
    passbox= driver.find_element(By.ID,"login-password").send_keys(password)
    print("waiting 2s to ensure that all details are entered properly...........")
    time.sleep(2)
    print("Attempting to login...........")
    submit=driver.find_element(By.ID,"login-button").click()
    print("waiting for 20s so that page loads completely...........")
    time.sleep(20)
    print("Validating login...........")
    try:
        if driver.find_element(By.CLASS_NAME,"T1xI1RTSFU7Wu94UuvE6") and driver.find_element(By.ID,"config"):
            log=True
    except selenium.common.exceptions.NoSuchElementException:
        log=False
    return log

