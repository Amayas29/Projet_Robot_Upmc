import cv2
from PIL import Image

def get_forme(frame):
    """
    Image -> List * int
    Permet de reccuperer les masks de l'image apres applications de la selection des couleurs ainsi que le nombre de masks non vides
    """

    # On transforme l'image en hvs
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # On boucle sur les quatre couleurs

    hsv_lower = (95, 100, 20)
    hsv_upper = (115, 255, 255)
      
    mask = cv2.inRange(hsv, hsv_lower, hsv_upper)

        # On netoie un peu le mask
    # mask = cv2.erode(mask, None, iterations=4)
    # mask = cv2.dilate(mask, None, iterations=4)

    i = Image.fromarray(mask)
    i.save("m.png")
    
    # On chercher toutes les formes detecter
    elements, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    n = -1
    max_el = None
    for cnt in elements:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        
        m = len(approx)
        if n < m:
            max_el = cnt
            n = m
        
    cv2.drawContours(frame,[max_el],0,(0,255,255),-1)
    return n


img = cv2.imread("image.png")

n = get_forme(img)

img = Image.fromarray(img)
img.save("E.png")
print(n)