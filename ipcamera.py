import urllib
import cv2
import numpy as np
import urllib.request

def savescreenipcamera():
    img_counter = 0
    while True:
        with urllib.request.urlopen("http://192.168.1.11:8080/shot.jpg") as imgResp:
            s = imgResp.read()

        imgNp = np.array(bytearray(s), dtype=np.uint8)
        img = cv2.imdecode(imgNp, -1)

        # all the opencv processing is done here
        cv2.imshow('test', img)
        k = cv2.waitKey(1)

        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = "LicPlateImages/plate_{}.png".format(img_counter)
            cv2.imwrite(img_name, img)
            print("{} written!".format(img_name))
            img_counter += 1
            break

