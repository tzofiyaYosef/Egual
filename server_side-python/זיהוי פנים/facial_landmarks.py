from imutils import face_utils
import numpy as np
import argparse # משמש לניתוח ארגומנטים של שורת הפקודה המועברים לסקריפט של פייתון 
import imutils
import dlib
import cv2


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape_predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args()) # ap יוצר מילון מאובייקטים שהוכנסו קודם לאובייקט 
# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor - אתחול גלאי הפנים ולאחר מכן צור ציון דרך הפנים
detector = dlib.get_frontal_face_detector() # יוצרת אובייקט גלאי פנים שיכול לזהות פרצופים בתמונה 
predictor = dlib.shape_predictor(args["shape_predictor"])

# load the input image, resize it, and convert it to grayscale
image = cv2.imread(args["image"]) # opencv פתיחת תמונה בספריית 
print("after open image")
image = imutils.resize(image, width=1300)
print("1234567890-12345678901234567890")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image -  מסמן את כל הפרצופים בתמונה ויוצר רשימה של מלבנים עם קואורדינטות של מיקומי המלבנים
rects = detector(gray, 1)

# loop over the face detections - מעבר על כל זיהוי הפנים שהתגלו
for (i, rect) in enumerate(rects):
	# determine the facial landmarks for the face region, then
	# convert the facial landmark (x, y)-coordinates to a NumPy
	# array
	shape = predictor(gray, rect) # הפונק' מקבלת תמונה בגווני אפור ואת המלבן התוחם ומחזירה אובייקט המכיל את כל 68 ציוני הפנים באזור הספציפי שזוהה
	shape = face_utils.shape_to_np(shape) # ממיר את זה לטופל בעל 68 שורות ו2 עמודות

	# convert dlib's rectangle to a OpenCV-style bounding box 
	# [i.e., (x, y, w, h)], then draw the face bounding box
	(x, y, w, h) = face_utils.rect_to_bb(rect)
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

	# show the face number
	cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

	# loop over the (x, y)-coordinates for the facial landmarks
	# and draw them on the image
	for (x, y) in shape:
		cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

# show the output image with the face detections + facial landmarks
cv2.imshow("Output", image)
cv2.waitKey(0)



