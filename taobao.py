from selenium import webdriver#浏览器驱动
from selenium.common.exceptions import TimeoutException#selenium请求超时错误
from selenium.webdriver.common.by import By#selenium查找元素
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait#设置等待超时时间
from urllib.parse import quote#汉字转义编码成浏览器可以理解的
from pyquery import PyQuery#解析页面
import time
KEYWORD="ipad"
browser=webdriver.Chrome("D:\\Softwares\\chromedriver-win64\\chromedriver.exe")
wait=WebDriverWait(browser,10)#设置等待时间10s

def crawl_page(page):
	try:
		url="https://s.taobao.com/search?q="+quote(KEYWORD)
		browser.get(url)
		time.sleep(10)#这时候扫码登录一下
		# input_account=browser.find_element_by_id("fm-login-id")
		# input_account.send_keys("hhhhhhhhh")
		# input_password=browser.find_element_by_id("fm-login-password")
		# input_password.send_keys("PASSWORDdz")
		# login_button=browser.find_element_by_class("password-login")
		# login_button.click()
		if page >1:
			print(page)
			page_box=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".next-pagination-jump-input input")))#是否存在这个input
			print("page_box")
			submit_button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".next-pagination-jump-go")))#去下一页的确定按钮是不是可以点击
			print("submit_button")
			page_box.clear()
			page_box.send_keys(page)
			submit_button.click()
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='contentInner--']")))#项目列表是否存在,匹配任何包含 contentInner-- 作为类名前缀的元素
		scroll_and_load()  # 模拟滚动加载更多商品(前端使用了懒加载模式)
		get_products()#如果页面存在，则调用下一个函数
	except:
		crawl_page(page)
def get_products():
	html=browser.page_source#先拿到页面的源码
	doc = PyQuery(html.encode('utf-8'))  # 确保以正确的编码方式解析
	items = doc("[class*='doubleCard--']").items()# 获取所有包含 doubleCard-- 的元素
	with open("taobao.txt", "w", encoding="utf-8") as f:
		for item in items:
			img_element = item.find("[class*='mainPic--']")# 获取包含 mainPic-- 前缀的元素，并通过正则匹配筛选出符合要求的类名
			img_url = img_element.attr('src')# 获取图片的 src 属性.procity--wlcT2xH9
			price=item.find("[class*='priceInt--']").text()+item.find("[class*='priceFloat--']").text()
			deal_count=item.find("[class*='realSales--']").text()
			if deal_count:
				deal_count=deal_count[:-3]
			title=item.find("[class*='title--'] span").text()
			shop=item.find("[class*='shopNameText--']").text()
			location=item.find("[class*='procity--'] span").text()
			product = {
			    "img": img_url,
			    "price":price,
			    "deal_count":deal_count,
			    "title":title,
			    "shop":shop,
			    "location":location
			    }
			print(product) 
			f.write("img_url\n{}\nprice\n{}\ndeal_count\n{}\ntitle\n{}\nshop\n{}\nlocation\n{}\n".format(img_url,price,deal_count,title,shop,location))
def scroll_and_load():
    """模拟逐步滚动页面并加载所有商品数据"""
    last_height = browser.execute_script("return document.body.scrollHeight")  # 获取页面当前的高度
    scroll_attempts = 0  # 添加滚动次数控制
    
    while True:
        # 每次滚动500像素，确保能加载更多内容
        browser.execute_script("window.scrollBy(0, 800);")  # 向下滚动500像素
        time.sleep(3)  # 等待页面加载新的商品数据
        new_height = browser.execute_script("return document.body.scrollHeight")  # 获取新的页面高度
        
        # 检查页面高度是否发生变化
        if new_height == last_height:  # 如果页面高度没有变化，说明已经滚动到底部
            scroll_attempts += 1
            if scroll_attempts > 5:  # 如果连续5次没有加载更多商品，则认为页面已加载完成
                break
        else:
            last_height = new_height  # 更新页面高度
        
        # 增加等待时间，确保加载更多商品
        time.sleep(3)  # 等待页面加载完毕			


crawl_page(5)