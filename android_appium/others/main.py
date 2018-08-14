#!/usr/bin/env python
#-*- coding:utf-8 -*-

# author: johnw

from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'  
desired_caps['platformVersion'] = '6.0'  
desired_caps['deviceName'] = 'Android Emulator'  
desired_caps['appPackage'] = 'com.android.calculator2'  
desired_caps['appActivity'] = '.Calculator'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_id("com.android.calculator2:id/digit_8").click()
driver.find_element_by_id("com.android.calculator2:id/op_mul").click()
driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
driver.find_element_by_id("com.android.calculator2:id/eq").click()
driver.quit()