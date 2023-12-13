import cv2
import math
import numpy as np
from PIL import Image
from deepface import DeepFace
import matplotlib.pyplot as plt

def align_image(image_path):
    # איתחול מפתחות הזיהוי של OpenCV לזיהוי פנים ועיניים
    face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    eye_detector = cv2.CascadeClassifier("haarcascade_eye.xml")

    # טעינת התמונה והעתקתה
    img = cv2.imread(image_path)
    img_raw = img.copy()

    # זיהוי פנים בתמונה
    faces = face_detector.detectMultiScale(img, 1.3, 5)
    if len(faces) > 0:
        face_x, face_y, face_w, face_h = faces[0]
       
        # חיתוך והקטנת התמונה לאזור הפנים בלבד
        img = img[int(face_y):int(face_y+face_h), int(face_x):int(face_x+face_w)]
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       
        # זיהוי עיניים באזור הפנים
        eyes = eye_detector.detectMultiScale(img_gray)
        print(len(eyes))
        if len(eyes) == 2:
             # מיקום ומסגרות העיניים וציורן על התמונה
            index = 0
            for (eye_x, eye_y, eye_w, eye_h) in eyes:
                if index == 0:
                    eye_1 = (eye_x, eye_y, eye_w, eye_h)
                elif index == 1:
                    eye_2 = (eye_x, eye_y, eye_w, eye_h)
              
                cv2.rectangle(img, (eye_x, eye_y), (eye_x+eye_w, eye_y+eye_h), (255, 0, 0), 2)
                index = index + 1
            
            # קביעת עין שמאלית ועין ימנית לפי המיקום האופטימלי
            if eye_1[0] < eye_2[0]:
                left_eye = eye_1
                right_eye = eye_2
            else:
                left_eye = eye_2
                right_eye = eye_1
            
            # חישוב מרכז העין השמאלית והימנית
            left_eye_center = (int(left_eye[0] + (left_eye[2] / 2)), int(left_eye[1] + (left_eye[3] / 2)))
            left_eye_x = left_eye_center[0]
            left_eye_y = left_eye_center[1]
            
            right_eye_center = (int(right_eye[0] + (right_eye[2] / 2)), int(right_eye[1] + (right_eye[3] / 2)))
            right_eye_x = right_eye_center[0]
            right_eye_y = right_eye_center[1]
            
            # חישוב זוויות פיך ומרקם הפנים
            if left_eye_y > right_eye_y:
                point_3rd = (right_eye_x, left_eye_y)
                direction = -1
            else:
                point_3rd = (left_eye_x, right_eye_y)
                direction = 1
            
            a = euclidean_distance(left_eye_center, point_3rd)
            b = euclidean_distance(right_eye_center, left_eye_center)
            c = euclidean_distance(right_eye_center, point_3rd)
            
            # חישוב זווית פיך
            cos_a = (b**2 + c**2 - a**2) / (2 * b * c)
            angle = np.arccos(cos_a)
            angle = (angle * 180) / math.pi
            
            # סיבוב התמונה לפי הזווית החושבת
            if direction == -1:
                angle = 90 - angle
            
            img = Image.fromarray(cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB))
            img = np.array(img.rotate(direction * angle))
       
    return img

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# תמונה מקורית
# image_path = "images/jon1.png"

# מיצוב תמונה מיושרת
# aligned_image = align_image(image_path)

# שמירת התמונה המיושרת
# cv2.imwrite("aligned_image.jpg", aligned_image)

# הצגת הפנים המיושרות
# plt.imshow(cv2.cvtColor(aligned_image, cv2.COLOR_BGR2RGB))
# plt.show()