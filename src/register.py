import cv2

def take_picture():
	cap = cv2.VideoCapture(0)

	while(True):
	    ret, frame = cap.read()
	    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

	    cv2.imshow('frame', rgb)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	    	img_name = 'assets/frame.jpg'
	    	out = cv2.imwrite(img_name, frame)
	    	break

	cap.release()
	cv2.destroyAllWindows()

	with open(img_name, 'rb') as binaryfile :
	    myArr = binaryfile.read()

	return myArr