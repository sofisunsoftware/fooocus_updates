import cv2
# im = cv2.imread('test.png')
# img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)   # BGR -> RGB

# print (img)
# print (type(img))

im = cv2.imread('mask_test.png')
img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)   # BGR -> RGB

print (img[:, :, 0])
print (type(img))