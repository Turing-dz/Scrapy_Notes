from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import cv2 as cv
from PIL import Image
import numpy
import requests
import re
#1.首先拿到滑块验证码图片
driver = webdriver.Chrome(executable_path="./_resources/chromedriver.exe")
driver.get("https://www.liepin.com/")
time.sleep(3)
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/section[2]/div[2]/div/div/div/div/div[2]/div/div[2]'))
).click()
username = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]'))
)
username.send_keys("hhhhhhhhh")
password = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="pwd"]'))
)
password.send_keys("passworddz!")
checkbox = driver.find_element(By.CLASS_NAME, "ant-checkbox-input")
checkbox.click()
login = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/section[2]/div[2]/div/div/div/div/div[3]/div/form/button'))
)
login.click()
time.sleep(8)
#切换iframe，再拿到验证码图片
driver.switch_to_frame("tcaptcha_iframe")
while driver.current_url=="https://www.liepin.com/":#避免出错,出错重复尝试
    refresh = driver.find_element(By.XPATH, '//*[@id="reload"]/div')
    refresh.click()
    time.sleep(2)
    back_url=driver.find_element(By.XPATH,'//*[@id="slideBg"]').get_attribute("src")
    back=requests.get(back_url)
    with open("./back.png","wb") as f:
        f.write(back.content)
    front_url=driver.find_element(By.XPATH,'//*[@id="slideBlock"]').get_attribute("src")
    front=requests.get(front_url)
    with open("./front.png","wb") as f:
        f.write(front.content)
    #2.opencv计算滑动距离
    back=cv.imread("./back.png",flags=cv.IMREAD_GRAYSCALE)
    front=cv.imread("./front.png",flags=cv.IMREAD_GRAYSCALE)
    front=front[24:front.shape[0]-24,24:front.shape[1]-24]#小滑块图片裁剪处理一下
    thresh,back=cv.threshold(back,110,255,cv.THRESH_BINARY)#图片二值化处理  
    thresh,front=cv.threshold(front,40,255,cv.THRESH_BINARY_INV)
    cv.imwrite("./back_p.png",back)
    cv.imwrite("./front_p.png",front)
    match=cv.matchTemplate(back,front,cv.TM_CCORR_NORMED)
    distance=cv.minMaxLoc(match)[3][0]
    distance=distance*341//680-37#因为前端渲染的图片是经过压缩的，所以这里也做等比例缩小，-37是因为front左边有37
    # print(distance)
    #3.使用selenium模拟滑块滑动
    slider = driver.find_element(By.XPATH, '//*[@id="tcaptcha_drag_thumb"]')
    ActionChains(driver).pause(0.2).click_and_hold(slider).pause(0.2).move_by_offset(distance / 4, 5).perform()#避免被识别，分三次滑动
    ActionChains(driver).pause(0.1).move_by_offset(distance / 2, -2).perform()
    ActionChains(driver).pause(0.1).move_by_offset(distance / 4, 3).release().perform()
    time.sleep(3)
    driver.get("https://www.liepin.com/career/golang/")
driver.quit()