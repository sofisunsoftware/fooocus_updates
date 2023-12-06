import cv2
im = cv2.imread('test.png')
img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)   # BGR -> RGB
# cv2.imwrite('opncv_kolala.png', img) 

print (img)
print (type(img))