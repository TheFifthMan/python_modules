import unittest
from .config import Config
from appium import webdriver

class BaseTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = Config['platformName']  
        desired_caps['platformVersion'] = Config['platformVersion']  
        desired_caps['deviceName'] = Config['deviceName']  
        desired_caps['appPackage'] = Config['appPackage']   
        desired_caps['appActivity'] = Config['appActivity']  
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
            self.driver.quit()