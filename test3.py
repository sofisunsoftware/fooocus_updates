import cv2
from skimage import io
# im = cv2.imread('test.png')
# img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)   # BGR -> RGB

# print (img)
# print (type(img))

# im = cv2.imread('mask_test.png')
# im = cv2.imread('https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png')


im = io.imread('https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png')
img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)   # BGR -> RGB

print (img[:, :, 0])
print (type(img))