import qrcode
img=qrcode.make("hai tamizha")
img.save("moon.jpg")
#pip install opencv_puyhon
import cv2
qr_img=cv2.imread("moon.jpg")
qr_det=cv2.QRCodeDetector()
val,pts,st_code=qr_det.detectAndDecode(qr_img)
print("Information:",val)