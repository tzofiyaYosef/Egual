import cv2
import dlib
from imutils import face_utils
import imutils
from PIL import Image


def point68Model(image_path):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # טעינת תמונת הקלט, שינוי גודלה והמרה לגווני אפור
    image = cv2.imread(image_path)
    image = imutils.resize(image, width=1000)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # זיהוי פרצופים בתמונה בגווני אפור
    rects = detector(gray, 1)

    points = []
    # לולאה על זיהוי הפנים
    for (i, rect) in enumerate(rects):
        # קבלת ציוני הפנים עבור אזור הפנים באמצעות NumPy
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # ציור ואיחזור ציוני הפנים
        for (j, (x, y)) in enumerate(shape):
            cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
            cv2.putText(image, str(j+1), (x-5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)
            points.append([x, y])

    cv2.imshow("Output", image)
    cv2.waitKey(0)

    return points

# def point468Model(pathImg):
#     # טען את התמונה
#     image = cv2.imread(pathImg)
#     image = imutils.resize(image, width=1000)

#     # טען את המודל לזיהוי הפנים
#     mp_face_mesh = mp.solutions.face_mesh
#     face_mesh = mp_face_mesh.FaceMesh()

#     rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     # ציוני דרך הפנים 
#     result = face_mesh.process(rgb_image)

#     height, width, _ = image.shape
#     points = [[0] * 2 for i in range(468)]

#     for facial_landmarks in result.multi_face_landmarks:
#         for i in range(0, 468):
#          if i > 70 and i < 90: 
#             # if i==7:
#                  pt1 = facial_landmarks.landmark[i]
#                  x = int(pt1.x * width)
#                  y = int(pt1.y * height)
#                  cv2.circle(image, (x, y), 2, (255, 255, 255), -1)
#                  cv2.putText(image, str(i+1), (x-5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0), 1)
#                  points[i] = [x, y]

#     # print(functionPool.topToNose(points))

#     cv2.imshow("Image", image)
#     cv2.waitKey(0)
#     return points
