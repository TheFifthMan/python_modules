
import unittest
from common.Base import BaseTest
import time


class TestCase1(BaseTest):
    def test_register(self):
        self.driver.find_element_by_id('com.vipkid.app:id/mSignUpLayout').click()
        self.driver.find_element_by_xpath('//android.widget.EditText[@content-desc="请输入您的手机号码"]').set_value('18850523947')
        self.driver.find_element_by_xpath('//android.widget.EditText[@content-desc="请输入验证码"]').send_keys('12345')
        self.driver.find_element_by_xpath('//android.widget.EditText[@content-desc="请输入推荐人手机号(选填)"]').send_keys('1234567890')
        self.driver.find_element_by_class_name('android.view.View').click()
        


if __name__ == "__main__":
    unittest.main()
