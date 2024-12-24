#1.买云上ocr，2.pytesseract
#pip install pytesseract pillow (https://digi.bib.uni-mannheim.de/tesseract/下载，并添加到环境变量，tesseract -v测试)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import cv2 as cv
from PIL import Image
import pytesseract
import re
#1.首先通过xpath，将网页验证码保存下来
driver = webdriver.Chrome(executable_path="./_resources/chromedriver.exe")
driver.get("https://service.cheshi.com/user/login.php")
time.sleep(1)
while driver.current_url=="https://service.cheshi.com/user/login.php":#如果一直在登陆页面，就是识别不正确，再重来
    img=driver.find_element(By.XPATH,"//img[@class='yzm_img']")
    img.screenshot("./captcha.png")
    time.sleep(1)
    # driver.quit()
    #2.对图片进行二值化和形态学操作和去噪点处理等操作
    img2=cv.imread("./captcha.png",flags=cv.IMREAD_GRAYSCALE)
    thresh,binary=cv.threshold(img2,120,255,cv.THRESH_BINARY)
    # 噪点处理
    def interference_point(img):
        h, w = img.shape[:2]
        # 遍历像素点进行处理
        for y in range(0, w):
            for x in range(0, h):
                # 去掉边框上的点
                if y == 0 or y == w - 1 or x == 0 or x == h - 1:
                    img[x, y] = 255
                    continue
                count = 0
                if img[x, y - 1] == 255:
                    count += 1
                if img[x, y + 1] == 255:
                    count += 1
                if img[x - 1, y] == 255:
                    count += 1
                if img[x + 1, y] == 255:
                    count += 1
                if count > 2:
                    img[x, y] = 255
        return img
    # kernel = cv.getStructuringElement(cv.MORPH_RECT, (4, 4))
    # result = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel=kernel)
    # gray = cv.GaussianBlur(result, (5, 5), 0)  # 高斯滤波
    # result = cv.Canny(gray, 75, 250)  # Canny边缘检测


    result=interference_point(binary)
    cv.imwrite("./captcha2.png",result)
    #3.用Tesseract-OCR识别
    pytesseract.pytesseract.tesseract_cmd = r'D:\Softwares\Tesseract-OCR\tesseract.exe'
    textImage = Image.fromarray(result)
    text = pytesseract.image_to_string(textImage)
    print(text)
    #4.对识别结果做进一步处理
    exp=re.compile("[a-zA-Z0-9]")
    out=exp.findall(text)
    out = ''.join([str(i) for i in out])

    print("The result:", out)
    #实现登录
    phone=driver.find_element(By.XPATH,"//input[@class='phone']")
    phone.clear()
    ActionChains(driver).pause(0.5).click(phone).send_keys("hhhhhhhhh").perform()#0.5秒后点击phone的input元素，然后填内容
    yzm=driver.find_element(By.XPATH,"//input[@id='imgyzm']")
    yzm.clear()
    ActionChains(driver).pause(0.5).click(yzm).send_keys(out).perform()
    fsyzm=driver.find_element(By.XPATH,"//span[@class='sendyzm_btn blue']")
    fsyzm.click()
    time.sleep(20)
    login=driver.find_element(By.XPATH,"//input[@name='sub']")
    login.click()
    time.sleep(4)
print(driver.page_source)
time.sleep(4)
driver.quit()
