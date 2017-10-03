import time

import null as null
import selenium
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


baseurl = "https://intertop.ua"
username = "evo4ka@ua.fm"
password = "332332"

xpaths = { 'e-mail' : "//input[@name='username']",
           'Пароль' : "//input[@name='password']",
           'submit' : "//input[@type='submit']"
          }


mydriver = webdriver.Chrome()
mydriver.get(baseurl)
mydriver.maximize_window()
mydriver.find_element_by_class_name('push-notification-prompt-buttons').click()

mydriver.find_element_by_id("auth_block").click()
mydriver.find_element_by_xpath("//input[@name='ENTER-EMAIL'][@type='text']").send_keys(username)
mydriver.find_element_by_xpath("//input[@name='ENTER-PASSWORD'][@type='password']").send_keys(password)
mydriver.find_element_by_class_name('one-log-bt').click()
#time.sleep(5)


#selenium.clickAt("symbolLookupLink","1382,10");		 #  //вызываем твоё окно
#selenium.selectWindow("mywindow");				  # //переключаем фокус на открытое окно
#selenium.type(mydriver.find_element_by_xpath('//*[@name="Password"]'));			 #  //заполняем форму
#selenium.selectWindow(null);										#//возвращаем фокус на главное окно