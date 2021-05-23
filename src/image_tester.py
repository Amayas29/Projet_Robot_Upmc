import cv2
from math import atan2, degrees
import sys


def color_profiles(n):
    if n == 0:
        name = "Bleu"
        hsv_lower = (95, 100, 20)
        hsv_upper = (115, 255, 255)
        return (name, hsv_lower, hsv_upper)

    if n == 1:
        name = "Rouge"
        hsv_lower = (0, 100, 50)
        hsv_upper = (10, 255, 255)
        return (name, hsv_lower, hsv_upper)

    if n == 2:
        name = "Vert"
        hsv_lower = (50, 50, 20)
        hsv_upper = (100, 255, 255)
        return (name, hsv_lower, hsv_upper)

    if n == 3:
        name = "Jaune"
        hsv_lower = (10, 100, 50)
        hsv_upper = (50, 255, 255)
        return (name, hsv_lower, hsv_upper)


def get_masks_color(frame):
    masks = []

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    number = 0
    for i in range(4):
        _, hsv_lower, hsv_upper = color_profiles(i)
        mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
        mask = cv2.erode(mask, None, iterations=4)
        mask = cv2.dilate(mask, None, iterations=4)

        elements, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(elements) > 0:
            number += 1

        masks.append(mask)

    return masks, number


def get_position_balise(frame):
    masks, number = get_masks_color(frame)

    if number < 3:
        return -1, -1

    mask = (masks[0] | masks[1]) | (masks[2] | masks[3])

    mask = cv2.erode(mask, None, iterations=4)
    mask = cv2.dilate(mask, None, iterations=4)

    elements, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    c = max(elements, key=cv2.contourArea)

    ((x, y), r) = cv2.minEnclosingCircle(c)

    cv2.circle(frame, (int(x), int(y)), int(r), (0, 255, 255), 2)

    return x, y


def get_angle_orientation_balise(frame):
    (x, y) = get_position_balise(frame)

    if x == -1:
        return 0, 0

    y = frame.shape[1] - y

    sign = x - (frame.shape[0] / 2)

    if y == 0:
        if sign < 0:
            return 90, 1

        return 90, 0

    angle = atan2(abs(sign), y)

    return degrees(angle), 1 if sign < 0 else 0


n = int(sys.argv[1])

frame = cv2.imread("images/{}.png".format(n))
print(get_angle_orientation_balise(frame))


cv2.imshow("Hey", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
