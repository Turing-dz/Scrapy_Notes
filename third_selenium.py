from selenium import webdriver
browser=webdriver.Chrome("D:\\Softwares\\chromedriver-win64\\chromedriver.exe")
browser.get("http://www.baidu.com")
search_box=browser.find_element_by_id("kw")
search_box.send_keys("python")
search_bbutton=browser.find_element_by_id("su")
search_bbutton.click()