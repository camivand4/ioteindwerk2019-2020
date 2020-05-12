from selenium import webdriver
from sense_hat import SenseHat

sense = SenseHat()

sense.show_message("hi")

print("don't forget to fill in your email and password")

driver = webdriver.Chrome()
driver.get('https://facebook.com')

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
enterbtn = driver.find_element_by_xpath('//*[@id="u_0_b"]')

email.send_keys(loginfacebook)
password.send_keys(passwordfacebook)
enterbtn.click()

amountofmessages = driver.find_element_by_xpath
('//*[@id="mercurymessagesCountValue"]').text()
notif = amountofmessages
if notif > 0:
    sense.show_message("You got a message")
else:
    sense.show_message("Error")

