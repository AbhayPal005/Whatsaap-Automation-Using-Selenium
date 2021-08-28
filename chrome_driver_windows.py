from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome(executable_path='./driver/chromedriver')
driver.get('https://web.whatsapp.com/')

input("please scan qr code and press any key to continue:")

RM=driver.find_element_by_css_selector('span[title="Assignments & CT"]')
RM.click()

testinput=driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]")
time.sleep(10)
testinput.send_keys("Hello friends")
testinput.send_keys(Keys.RETURN)
