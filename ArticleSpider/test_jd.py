
from urllib import request
from pyppeteer import launch#pip install pyppeteer==1.0.2
import asyncio
import random

import cv2

def get_dis(bg, fg):
    img = cv2.imread(bg)
    temp = cv2.imread(fg)
    res = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)[2][0]  # 滑块需要滑行的距离
    # 如果网页展示对图片有压缩 那滑动距离也需要等比例压缩
    dis = value * 342 / 360
    return dis

async def login():
    browser = await launch({
        'headless': False,
        'args': ['--window-size=1377,789'],
    })

    page = await browser.newPage()
    await page.setViewport({'width': 1377, 'height': 789})

    await page.goto('https://passport.jd.com/new/login.aspx')

    # 点击切换 账户登录
    await page.click('#pwd-login')

    # 填写用户名
    await page.type('#loginname', '123123@qq.com', {
        'delay': random.randint(60, 120)
    })

    # 填写密码
    await page.type('#nloginpwd', '123123123', {
        'delay': random.randint(60, 120)
    })

    # 给他一个延时
    await page.waitFor(2000)
    await page.click('div.login-btn')
    await page.waitFor(2000)
    #进行距离移动 
    img_src =await page.Jeval ('.JDJRV-bigimg> img', 'el=> el.src')
    #下载图片
    request.urlretrieve (img_src,'image.png')
    temp_src =await page.Jeval ('.JDJRV-smallimg>img', 'el => el.src')
    request.urlretrieve (temp_src,'temp.png') 
    #缺口识别
    dis = get_dis ('image.png','temp.png') 
    #拖动滑块
    el =await page.J('div.JDJRV-slide-btn')
    box = await el.boundingBox()
    await page.hover ('div.JDJRV-slide-btn')
    #按下鼠标
    await page.mouse.down()
    await page.mouse.move (box ['x'] + dis + random.uniform (30,33), box ['y'], {'steps':30}) 
    await page.waitFor (random.randint (300,600))
    await page.mouse.move (box ['x'] + dis + 29, box ['y'],{'steps':30})
    await page.mouse.up ()# 松开鼠 
    await page.waitFor (2000) 
    print (' 登陆成功 ')
if __name__=="__main__":
    asyncio.get_event_loop().run_until_complete(login())
