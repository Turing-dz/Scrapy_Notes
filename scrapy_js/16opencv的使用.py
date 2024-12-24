#pip install opencv-python --only-binary=:all:
#pip install numpy
import cv2 as cv
import numpy
# img=cv.imread("../imgs/1984.jpg",flags=cv.IMREAD_COLOR)#BGR（IMREAD_GRAYSCALE单通道灰度图）
# print(img)
# for i in range(len(img)):
#     img[i][100]=[0,0,255]
# cv.imwrite("./writeimg.png",img)
# cv.imshow("myimage",img)
# cv.waitKey(0)
# cv.destroyAllWindows()

#1.nparray的数据可以直接被openv读取
# img2=numpy.zeros((200,300),numpy.uint8)#numpy.uint8范围是0-255的值
# print(img2,type(img2))
# for i in range(200):
#     img2[100][i]=255
# cv.imshow("img2",img2)
# cv.waitKey(0)
# cv.destroyAllWindows()

#2.截取/修改图像部分区域
# part=img[100:300,100:300]
# cv.imshow("part",part)
# img[100:300,100:300]=[255,0,255]
# cv.imshow("part",img)
# cv.waitKey(0)
# cv.destroyAllWindows()



#3.图像数值运算和二值化处理(黑白)
# print(img.shape)#图片长宽通道
# cover=numpy.ones((399,270,3),numpy.uint8)*50 #给每个像素点都BGR值都加50
# print(cover)
# result=cv.add(img,cover)
# result=cv.subtract(img,cover)
#黑白图（二值化）首先要先灰度图（单通道）
# imgh=cv.imread("../imgs/06c3335c-4a7f-4a55-875c-ce8a3a8062f7.jpg",flags=cv.IMREAD_GRAYSCALE)
# thresh,result=cv.threshold(imgh,180,255,cv.THRESH_BINARY)#超过180的都转成255
# cv.imshow("add50",result)


#4.图像平滑处理
# img=cv.imread("../imgs/1984.jpg",flags=cv.IMREAD_COLOR)
# result=cv.blur(img,(5,5))#对图像5*5的像素点求平均值处理
# result=cv.GaussianBlur(img,(5,5),1)#高斯模糊，5*5的像素做高斯处理，中间点像素大，边缘小
# cv.imshow("blur",result)


#5.图像形态学处理（腐蚀，膨胀）
# img1=numpy.zeros((500,500),numpy.uint8)#全黑
# img1[200:300,200:300]=255#白色
# kernel=numpy.ones((20,20),numpy.uint8)
# result=cv.erode(img1,iterations=1,kernel=kernel)#使用kernel大小的核做iterations次腐蚀（kernel区域内有一个0，就都置为0，黑色把白色腐蚀掉了）
# result=cv.dilate(img1,iterations=1,kernel=kernel)#膨胀（有白都白）
# cv.imshow("erode",result)

#6.模板匹配
img = cv.imread('../imgs/1984.jpg', flags=cv.IMREAD_GRAYSCALE)
roi = img[150:250, 150:250]

match = cv.matchTemplate(img, roi, cv.TM_CCORR_NORMED)
info = cv.minMaxLoc(match)
print(info)#(0.887405514717102, 0.9999998807907104, (80, 255), (150, 150))(最小相似度值,最大相似度值,最小值出现在 result 中的位置 ,最大值出现在 result 中的位置,一般是左上角)

cv.imshow('img', img)
cv.imshow('roi', roi)
cv.waitKey(0)
cv.destroyAllWindows()