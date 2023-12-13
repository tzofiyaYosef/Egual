#נייבא את ספריית openCv
import cv2
import matplotlib.pyplot as plt


#import image
imagePath = "images/bibi4.jpg"

#read image 
img = cv2.imread(imagePath)

#load image and insert to array
# print(img.shape)

#conversion color image to gray image
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ייבוא המסווג שבספריה שמזהה אדם, עיניים, חיוך, פלג גוף עליון ועוד 
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# כעת נבצע זיהוי פנים בתמונה בגווניי האפור באמצעות המסווג שקלטנו
# detectMultiscale - פןנק' המזהה פרצופים בגדלים שונים
# scaleFactor - הקטנת גודל התמונה ב10%
# minNeighbors - מסנן תוצאות שגויות מכל התוצאות שהתקבלו
face = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
# ציור תיבה תוחמת מסביב לאובייקט - לפרצוף
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

# המרת התמונה מפורמט כחול ירוק אדום, לפורמט אדום ירוק כחול
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow("Output", img)
cv2.waitKey(0)
# # הצגת התמונה בעזרת הספריה - Matplotlib
# plt.figure(figsize=(20, 10))
# plt.imshow(img_rgb)
# plt.axis('off')
