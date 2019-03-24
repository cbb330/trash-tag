import cv2
from Database import db

def take_picture():

	cam = cv2.VideoCapture(0)

	cv2.namedWindow("test")

	while True:
	    ret, frame = cam.read()
	    cv2.imshow("test", frame)
	    if not ret:
	        break
	    k = cv2.waitKey(1)

	    if k%256 == 27:
	        # ESC pressed
	        print("Escape hit, closing...")
	        break
	    elif k%256 == 32:
	        # SPACE pressed
	        img_name = "../assets/opencv_frame.png"
	        cv2.imwrite(img_name, frame)
	        print("{} written!".format(img_name))
	        img_counter += 1

	cam.release()

	cv2.destroyAllWindows()

	with open(img_name, "rb") as binaryfile :
	    myArr = bytearray(binaryfile.read())

	return myArr