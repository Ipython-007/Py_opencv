
#几何变换
import numpy as np
import cv2

lena = cv2.imread("D:/qihangsai/images/lena.jfif", -1)

#放缩
rows, cols = lena.shape[:2]
size = (int(cols*0.6), int(rows*0.5))
Re_lena = cv2.resize(lena, size)
re_lena = cv2.resize(lena, (720,720), interpolation=cv2.INTER_NEAREST)
cv2.imshow("resize_lena", Re_lena)

#翻转
'''
0 绕x轴翻转
正整数 y轴
负整数 x,y 轴
'''
x_lena = cv2.flip(lena, 0)
cv2.imshow("flip_lena",x_lena)

#仿射
'''
仿射后，直线仍然是直线，平行性依然保持
'''
#平移 向右100像素，向下200像素
x = 100
y = 200
M0 = np.float32([[1,0,x],[0,1,y]])
move = cv2.warpAffine(lena, M0, (cols,rows))
cv2.imshow("move_lena", move)

#旋转
M1 = cv2.getRotationMatrix2D((rows/2, cols/2), 45, 0.7)
rotate = cv2.warpAffine(lena, M1, (cols,rows))
cv2.imshow("rotate_lena", rotate)

#复杂仿射
p1 = np.float32([[0,0],[cols-1,0],[0,rows-1]])
p2 = np.float32([[0,rows*0.3],[cols*0.8,rows*0.2],[0,rows]])
M2 = cv2.getAffineTransform(p1,p2) #p1中的点映射到p2中
dst = cv2.warpAffine(lena, M2, (cols,rows))
cv2.imshow("dst", dst)

#透视
'''
仿射可以将矩形映射成为任意平行四边形，
透视变换则可以将矩形映射成为任意四边形
'''
pts1 = np.float32([[rows/2,0],[0, cols/2],[rows/2,cols-1],[rows-1,cols/2]])
pts2 = np.float32([[0,0],[0,cols-1],[rows-1,cols-1],[rows-1,0]])
M3 = cv2.getPerspectiveTransform(pts1,pts2)
dts = cv2.warpPerspective(lena,M3,(cols,rows))
cv2.imshow("dts",dts)

cv2.waitKey()
cv2.destroyAllWindows()
