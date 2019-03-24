import cv2

def take_trash_picture():
	cap = cv2.VideoCapture(0)

	while(True):
	    ret, frame = cap.read()
	    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

	    cv2.imshow('Trash Please', rgb)
	    if cv2.waitKey(1) & 0xFF == ord('t'):
	    	img_name = 'assets/trash_image/trash_image.jpg'
	    	out = cv2.imwrite(img_name, frame)
	    	break

	cap.release()
	cv2.destroyAllWindows()
