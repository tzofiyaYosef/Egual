from imutils import face_utils
import imutils
import numpy as np
import dlib
import cv2
import math
import numpy as np



def detect_faces(image_path):
    # ולאחר מכן צור מנבא ציון דרך הפנים(HOG מבוסס) dlib אתחל את גלאי הפנים של  
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("my_predictor.dat")

    # טען את תמונת הקלט, שנה את גודלה והמר אותה לגווני אפור
    image = cv2.imread(image_path)
    image = imutils.resize(image, width=1500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # לזהות פרצופים בתמונה בגווני אפור
    rects = detector(gray, 1)

    # לולאה על זיהוי הפנים
    for (i, rect) in enumerate(rects):
        # NumPy - למערך (x, y) קבע את ציוני הפנים עבור אזור הפנים, אם כן המר את קואורדינטות הפנים  
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        #x, y, width, height :כלומר עם openCV לתיבה תוחמת בסגון dlib המר את המלבן של 
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # מספור הפנים שבתמונה
        cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        points = [[0] * 2 for i in range(68)]
        # עבור ציוני הפנים וצייר אותם על התמונה(x, y) לולאה על קוארדינטות 
      
        for (j, (x, y)) in enumerate(shape):
            cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
            cv2.putText(image, str(j+1), (x-5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)
            points[j][0] = x
            points[j][1] = y

    nose(points)
    # הצג את תמונת הפלט עם זיהוי הפנים + ציוני פנים
    cv2.imshow("Output", image)
    cv2.waitKey(0)
    # a = points[3][0], points[3][1]
    # b = points[9][0], points[9][1]
    # c = points[12][0], points[12][1]
    # # הנקודות הנתונות
    # points = [a, b, c]

    # # חישוב המשוואה המתאימה לפרבולה
    # a, b, c = find_parabola_coefficients(points)

    return(points)

# פונקציית למציאת מרחק בין 2 נקודות 
def distans(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# פונקציה שמקבלת 2 תמונות ובודקת האם זה אותו אדם 
def isSame(image1, image2):
    points1 = detect_faces(image1)
    points2 = detect_faces(image2)
    print('i am in function eyebrow')
    eyebrow(points1)
    eyebrow(points2)
    print('i am in function nose')
    nose(points1)
    nose(points2)

    # sum1 = sum2 = 0
    # face1 = distans(points1[0][0], points1[0][1], points1[16][0], points1[16][1])
    # face2 = distans(points2[0][0], points2[0][1], points2[16][0], points2[16][1])
    # # האורך שבין הסנטר לשפה התחתונה של שתי התמונות
    # d1 = distans(points1[8][0], points1[8][1], points1[27][0], points1[27][1])
    # d2 = distans(points1[8][0], points1[8][1], points1[57][0], points1[57][1])
    # sum1 += (100*d2)/d1
    
    # d1 = distans(points2[8][0], points2[8][1], points2[27][0], points2[27][1])
    # d2 = distans(points2[8][0], points2[8][1], points2[57][0], points2[57][1])
    # sum2 += (100*d2)/d1
    
    
    # # האורך של נחיר לעומת כלל הפנים והאף 
    # d1 = distans(points1[31][0], points1[31][1], points1[33][0], points1[33][1])
    # d2 = distans(points1[33][0], points1[33][1], points1[35][0], points1[35][1])
    # sum1 += (100*(d1+d2))/face1
    # d1 = distans(points2[31][0], points2[31][1], points2[33][0], points2[33][1])
    # d2 = distans(points2[33][0], points2[33][1], points2[35][0], points2[35][1])
    # sum2 += (100*(d1+d2))/face2

    # print('sum1:{}'.format(sum1))
    # print('sum2:{}'.format(sum2))

def toDistans(arr, index1, index2):
    return distans(arr[index1][0], arr[index1][1], arr[index2][0], arr[index2][1])

# לא מדוייק - לפעמים מביא את אותה סטיה של האף
def eye(points):
    widthFace = toDistans(points, 0, 16)
    eye1 = toDistans(points, 36, 39)
    eye2 = toDistans(points, 42, 45)
    print((100*((eye1+eye2)/2))/widthFace)

# מרחק בין הגבות
def eyebrow(points):
    widthEyebrow = toDistans(points, 21, 22)
    withFace = toDistans(points, 0, 16)
    print("widthEyebrow:{}".format((100*widthEyebrow)/withFace))

# !!מדוייק ממש
def nose(points):
    hieghtFace = toDistans(points, 8, 27)
    noseIn = toDistans(points, 30, 27)
    print(round((100*noseIn)/hieghtFace))

def mouth(points):
    hieghtFace = toDistans(points, 8, 27)
    mouthIn = toDistans(points, 8, 57)
    print((100*mouthIn)/hieghtFace)


def find_parabola_coefficients(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    denom = (x1 - x2) * (x1 - x3) * (x2 - x3)
    a = ((x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / denom)
    b = ((x3**2 * (y1 - y2) + x2**2 * (y3 - y1) + x1**2 * (y2 - y3)) / denom)
    c = ((x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / denom)
    print(f"a={a}, b={b}, c={c}")
    print(-b/(2*a))
    return a, b, c


detect_faces("images/bibi1.jpg")
# isSame("images/nir.jpg", "images/bibi1.jpg")