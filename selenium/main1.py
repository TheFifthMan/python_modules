from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D://InstallSoftFolder//chromedriver.exe")
driver.get("https://www.baidu.com")
print(driver.title)
# 最大化
driver.maximize_window()
driver.get("https://www.google.com")

# 设置窗口大小
driver.set_window_size(480,800)
print(driver.title)
# 后退
driver.back()
time.sleep(1)

# 前进
driver.forward()
time.sleep(2)
print(driver.title)
driver.quit()