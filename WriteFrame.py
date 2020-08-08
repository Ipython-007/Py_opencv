#将捕获的视频写入文件

import numpy as np
import cv2

cap = cv2.VideoCapture(0)  #1，表示调用第二个摄像头，也就是usb摄像头
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#out = cv2.VideoWriter(filename, fourcc, fps, size)
#fourcc = cv2.VideoWriter_fourcc('I','4','2','0')  编码解码类型

fourcc = cv2.VideoWriter_fourcc('I','4','2','0')
out = cv2.VideoWriter('output.avi', fourcc, 20, (640,480))
#对象out的大小要与捕获对象cap大小保持一致，否则无法写入

while cap.isOpened():
    ret, frame = cap.read()  #ret, 返回值为True ,表示捕获成功，frame表示捕获帧
    
    #附加一个Canny边缘检测的视频
    frame_canny = cv2.Canny(frame, 100,200)
    if ret == True:
        out.write(frame) #写入下一帧
        cv2.imshow("frame", frame)
        cv2.imshow("frame_canny", frame_canny)
        
        if cv2.waitKey(1) == 27:    #ascii码：27--> Esc键
            break
    else:
        break
        
cap.release()
out.release()
cv2.destroyAllWindows()

