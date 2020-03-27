import cv2
from lib.Image import Image
from lib.Hole import Connectivity


mask = cv2.imread('penguin-mask.png', 0)
img = cv2.imread('penguin-img.png', 0)
a = Image(img, mask, Connectivity.four_connectivity)
a.hole.fix_hole()

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
