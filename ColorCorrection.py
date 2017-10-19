import cv2
import numpy as np

guc_img = cv2.imread('GUC.png')
guc_img_modified = cv2.imread('GUC.png')

for x in range(len(guc_img_modified)):
    for y in range(len(guc_img_modified[0])):
        if guc_img_modified[x][y][0] < 50:
            guc_img_modified[x][y][0] = 0
        else:
            guc_img_modified[x][y][0] -= 50
        if guc_img_modified[x][y][1] < 50:
            guc_img_modified[x][y][1] = 0
        else:
            guc_img_modified[x][y][1] -= 50
        if guc_img_modified[x][y][2] < 50:
            guc_img_modified[x][y][2] = 0
        else:
            guc_img_modified[x][y][2] -= 50

cv2.imshow('GUC', guc_img)
cv2.imshow('GUC_Modified', guc_img_modified)
cv2.waitKey(0)
cv2.destroyAllWindows()

calc_img = cv2.imread('calculator.png')
calc_img_modified = cv2.imread('calculator.png')

for x in range(len(calc_img_modified)):
    for y in range(len(calc_img_modified[0])):
        if calc_img_modified[x][y][0] > 180:
            calc_img_modified[x][y][0] = 180
        if calc_img_modified[x][y][1] > 180:
            calc_img_modified[x][y][1] = 180
        if calc_img_modified[x][y][2] > 180:
            calc_img_modified[x][y][2] = 180

cv2.imshow('Calculator', calc_img)
cv2.imshow('Calculator_Modified', calc_img_modified)
cv2.waitKey(0)
cv2.destroyAllWindows()

cam_img = cv2.imread('cameraman.png')
cam_img_modified = cv2.imread('cameraman.png')

for x in range(len(cam_img_modified)):
    for y in range(len(cam_img_modified[0])):
        if cam_img_modified[x][y][0] < 40:
            cam_img_modified[x][y][0] += 40
        if cam_img_modified[x][y][1] < 40:
            cam_img_modified[x][y][1] += 40
        if cam_img_modified[x][y][2] < 40:
            cam_img_modified[x][y][2] += 40

cv2.imshow('Cameraman', cam_img)
cv2.imshow('Cameraman_Modified', cam_img_modified)
cv2.waitKey(0)
cv2.destroyAllWindows()
