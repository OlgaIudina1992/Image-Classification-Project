import pytesseract
from pytesseract import Output
import PIL.Image
import cv2

myconf = r"--psm 4 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("dip_04.jpg"), config=myconf)
print(text)

img = cv2.imread("dip_04.jpg")
height, width, channels = img.shape

'''
boxes = pytesseract.image_to_boxes(img, config=myconf)
for box in boxes.splitlines():
    box = box.split(" ")
    img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
'''

data = pytesseract.image_to_data(img, config=myconf, output_type=Output.DICT)
box_num = len(data['text'])
for i in range(box_num):
    if float(data['conf'][i]) > 60:
        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x,y), (x+width, y+height), (0,255,0), 1)
        img = cv2.putText(img, data['text'][i], (x, y+height+15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey(0)