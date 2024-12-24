from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from shutil import which
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# chrome_options.add_argument("--headless")

driver_path=which("chromedriver")
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://duckduckgo.com")
# 定位搜索框，使用 id 查找元素
search_input = driver.find_element("id", "searchbox_input")
search_input.send_keys("My User Agent")
search_input.send_keys(Keys.ENTER)
print(driver.page_source)
# driver.close()