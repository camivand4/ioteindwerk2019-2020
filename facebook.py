from selenium import webdriver
from sense_hat import SenseHat
from env import *
import pyautogui
from time import sleep
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)

sense = SenseHat()

print("don't forget to read the .readme file")

driver = webdriver.Chrome(options=options)
driver.get('https://facebook.com')

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
enterbtn = driver.find_element_by_xpath('//*[@id="u_0_b"]')

email.send_keys(loginfacebook)
password.send_keys(passwordfacebook)
enterbtn.click()

sense.show_message("facebook")

messagebtnreal = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/a/div').text
messagebtn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/a/div/span/span')
#messagebtnreal.click()
print(messagebtn)

