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

X = [255, 255, 255]
O = [91, 110, 225]

facebookpixels = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, X, X, O,
O, O, O, O, X, O, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, X, X, X, O,
O, O, O, O, X, O, O, O,
O, O, O, O, X, O, O, O,
O, O, O, O, X, O, O, O
]

print("don't forget to read the .readme file")

driver = webdriver.Chrome(options=options)
driver.get('https://facebook.com')

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
enterbtn = driver.find_element_by_xpath('//*[@id="u_0_b"]')

email.send_keys(loginfacebook)
password.send_keys(passwordfacebook)
enterbtn.click()

sleep(5)

def facebook_look():
    pyautogui.hotkey('ctrl','r')    
    sleep(10)
    
    messagebtn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/a/div/span/span').text

    if(messagebtn == ""):
        sense.clear()
    else:
        sense.set_pixels(facebookpixels)

    facebook_look()

def facebook_look_first():
    messagebtn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/a/div/span/span').text
    
    if(messagebtn == ""):
        sense.clear()
    else:
        sense.set_pixels(facebookpixels)
    facebook_look()

facebook_look_first()

