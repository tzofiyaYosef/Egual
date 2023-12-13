import cv2
import mediapipe as mp
import imutils
import functionPool

def func(path):
    image = cv2.imread(path)
    image = imutils.resize(image, width=700)

# Face Mesh
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Facial landmarks
    result = face_mesh.process(rgb_image)

    height, width, _ = image.shape
    points = [[0] * 2 for i in range(468)]

    for facial_landmarks in result.multi_face_landmarks:
        for i in range(0, 468):
        #  if i > 0 and i < 68: 
            # if i==7:
                 pt1 = facial_landmarks.landmark[i]
                 x = int(pt1.x * width)
                 y = int(pt1.y * height)
                 cv2.circle(image, (x, y), 2, (255, 255, 255), -1)
                 cv2.putText(image, str(i+1), (x-5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)
                 points[i][0] = x
                 points[i][1] = y

    # print(functionPool.topToNose(points))

    cv2.imshow("Image", image)
    cv2.waitKey(0)

func("images/bibi10.jpg")
func("images/bb.jpg")
