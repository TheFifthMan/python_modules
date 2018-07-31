from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="D://InstallSoftFolder//chromedriver.exe")
driver.get("https://tieba.baidu.com/index.html")
time.sleep(2)
driver.find_element_by_css_selector('//a.u_member_wrap').click()
WebDriverWait(driver,10).until(lambda dr:dr.find_element_by_css_selector('a.dropdown-dou j_wallet').is_displayed())
driver.find_element_by_css_selector('a.dropdown-dou j_wallet').click()
time.sleep(1)
driver.quit()