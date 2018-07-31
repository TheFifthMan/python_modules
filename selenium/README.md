# 示例1
1. 打开谷歌浏览器
2. 打开百度
3. 打印title

chromedriver下载： https://sites.google.com/a/chromium.org/chromedriver/home 
代码：
```
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D://InstallSoftFolder//chromedriver.exe")
driver.get("https://www.baidu.com")
print(driver.title)
driver.quit()
```

# 示例2
1. 打印URL
2. 浏览器最大化: maximize_window()
3. 设置浏览器高，宽: set_window_size()
4. 控制浏览器前进，后退： back() 

代码：
```
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
```
# 示例3
1. 对象定位:xpath,css selector,id,name
```
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D://InstallSoftFolder//chromedriver.exe")
driver.get("https://www.baidu.com")
# id
#driver.find_element_by_id("kw").send_keys("Hello world")
# css selector
#driver.find_element_by_css_selector('input[name="wd"]').send_keys("Hello world")
# xpath
#driver.find_element_by_xpath('//input[@name="wd"]').send_keys("Hello world")
time.sleep(2)
driver.quit()
```
注： 这里出现的都是单个元素，如果是多个元素，find_xxx就是一个列表。

# 示例4
1. 定位select 元素
2. 等待元素出现
3. 执行js

```
driver.find_element_by_tag_name("select")
WebDriverWait(driver,10).until(lambda dr:dr.find_element_by_css_selector('a.dropdown-dou j_wallet').is_displayed())
execute_script(script, *args)
```
# 总结
鉴于网上已经有详细文档，其实也没有必要全部在写一遍，仅记录一些常见的点备用。

# 参考
http://www.testtao.cn/?p=28 