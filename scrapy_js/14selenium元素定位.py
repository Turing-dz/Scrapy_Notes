from selenium import webdriver#pip install selenium
import time
driver = webdriver.Chrome(executable_path="./_resources/chromedriver.exe")
driver.get("https://www.cheshi.com/")
print(driver.current_url)#url
with open("./cheshi.html","w", encoding="utf-8") as f:
    f.write(driver.page_source)#源码
driver.save_screenshot("cheshi.png")#网页截图
time.sleep(1)
driver.quit()