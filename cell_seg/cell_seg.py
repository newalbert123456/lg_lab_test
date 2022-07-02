import matplotlib as plt
import numpy as np
import cv2

path = './mouse.tif'
img = cv2.imread(path)

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
twoDimage = img.reshape((-1,3))
twoDimage = np.float32(twoDimage)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 6
attempts=10
ret,label,center=cv2.kmeans(twoDimage,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
#res = center[label.flatten()]
color = np.uint8([[255, 0, 0],
                  [0, 0, 255],
                  [128, 128, 128],
                  [100, 0, 28],
                  [0,100, 28],
                  [0, 255, 0]])
res = color[label.flatten()]
result_image = res.reshape((img.shape))
cv2.imwrite('./cell.jpg',result_image)
