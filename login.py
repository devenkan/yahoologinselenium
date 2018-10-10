from selenium import webdriver
import time
browser = webdriver.Chrome(executable_path=r"C:\Users\asper\Desktop\web\chromedriver.exe")
browser.get('https://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('#enter the email')
element = browser.find_element_by_id("login-signin")
element.click()
time.sleep(1)
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('#here enter the password')
submit1 = browser.find_element_by_id("login-signin")
submit1.click()
#passwordElem.submit()
