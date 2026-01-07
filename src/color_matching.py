#RGB → HSV
import cv2
import numpy as np

def rgb_to_hsv(rgb_color):
    rgb = np.uint8([[rgb_color]])
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    return hsv[0][0]

def match_colors(hsv_color):
    h, s, v = hsv_color
    if h < 10 or h > 170:  # Red
        return ["Black", "White", "Grey"]
    elif 10 <= h < 30:  # Orange
        return ["White", "Navy Blue", "Brown"]
    elif 30 <= h < 60:  # Yellow
        return ["Black", "Grey", "Navy Blue"]
    elif 60 <= h < 90:  # Green
        return ["White", "Beige", "Brown"]
    elif 90 <= h < 130:  # Blue
        return ["White", "Grey", "Beige"]
    else:  # Purple / others
        return ["White", "Grey", "Black"]
