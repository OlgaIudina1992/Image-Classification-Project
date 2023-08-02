import cv2

image = cv2.imread("dip_03.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, result = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)

adpt_result = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 5)

cv2.imshow("image", adpt_result)
cv2.imwrite("dip_04.jpg", adpt_result)
cv2.waitKey(0)