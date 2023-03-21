import matplotlib.pyplot as plt
from matplotlib.image import imread

#이미지 읽어오기(적절한 경로설정 필요)
img=imread('C:/Users/김주환/Desktop/bridge.png')#파일경로 "/"로 절대경로로 가져와야함


plt.imshow(img)
plt.show()