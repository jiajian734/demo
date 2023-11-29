print("hello world")



from selenium import webdriver

from  time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
        # 访问”Login“ 页面
driver.get("http://150.109.156.47:8000/")
driver.maximize_window()
sleep(5)
