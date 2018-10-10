from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome(executable_path=r"C:\Users\asper\Desktop\web\chromedriver.exe")
browser.get('https://login.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('#enter email id here')
loginbtn=browser.find_element_by_id("login-signin")
loginbtn.click()


passwordElem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "login-passwd"))
)
passwordElem.send_keys('#enter password here')
submitBtn=browser.find_element_by_id("login-signin")
submitBtn.click()
