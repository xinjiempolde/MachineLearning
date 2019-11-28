import cv2
import numpy as np
cap = cv2.VideoCapture(0)  # 调整参数实现读取视频或调用摄像头
while 1:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    conv2 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    frame = cv2.filter2D(frame, -1, conv2)
    cv2.imshow("cap", frame)
    if cv2.waitKey(100) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
