import cv2

img = cv2.imread('two.jpg', 1)
cv2.imshow("Original image",img)

img2 = cv2.GaussianBlur(img, (0, 0), 3);
img = cv2.addWeighted(img, 1.5, img2, -0.5, 0);


# CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
l, a, b = cv2.split(lab)  # split on 3 different channels

l2 = clahe.apply(l)  # apply CLAHE to the L-channel

lab = cv2.merge((l2,a,b))  # merge channels
img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR
cv2.imshow('Increased contrast', img2)
#cv2.imwrite('sunset_modified.jpg', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()