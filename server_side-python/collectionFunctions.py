import cv2
import pointModels
import aligneFace
import math

def faceScorePointsArray(path_img):
    global points
    global results
    results = []

    # מיצוב תמונה מיושרת
    aligned_image = aligneFace.align_image(path_img)

    # שמירת התמונה המיושרת
    cv2.imwrite("aligned_image.jpg", aligned_image)

    points = pointModels.point68Model("aligned_image.jpg")

    faceZise()
    # widthRightFace()
    # widthLeftFace()
    noseZise()
    eyes()
    breakingPointInHerBack()
    vertexNosebeginingEyebrow()
    betweenEyebrows()
    return results

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# רוחב וגובה הפנים
def faceZise():
    results.append(distance(points[0], points[16]))
    results.append(distance(points[27], points[8]))

# # רוחב חצי פנים - חלק ימין
# def widthRightFace():
#     results.append(distance(points[27], points[16])) * 100 / results[0]

# # רוחב חצי פנים - חלק שמאל
# def widthLeftFace():
#     results.append(distance(points[0], points[27])) * 100 / results[0]

# רוחב ואורך האף
def noseZise():
    results.append(distance(points[31], points[35]) * 100 / results[0])
    length = 0
    for i in range(27, 30):
        length += distance(points[i], points[i+1])
    results.append(length * 100 / results[1])

# אורך גבה 
def eyebrowLength(j):
    length = 0
    for i in range(j, j + 4):
        length += distance(points[i], points[i+1])
    return length

# כמה העין תופסת מהגבה וכמה מהפנים - לא מומלץ
# def eyes(points):
#     rightEyebrowLength = eyebrowLength(points, 22)
#     leftEyebrowLength = eyebrowLength(points, 17)
#     rightEye = distance(points[42][0], points[42][1], points[45][0], points[45][1])
#     leftEye = distance(points[36][0], points[36][1], points[39][0], points[39][1])
#     print("right eye:", rightEye * 100 / rightEyebrowLength)
#     print("left eye:", leftEye * 100 / leftEyebrowLength)

# קוטר עין
def eyes():
    leftEye = distance(points[36], points[39]) * 100 / results[0]
    rightEye = distance(points[42], points[45]) * 100 / results[0]
    results.append(rightEye)
    results.append(leftEye)

# def distanceMiddle(points):
#     widthFace = widthAllFace(points)
#     d = [0] * 68
#     for i in range(68):
#         d[i] = distance(points[i][0], points[i][1], points[30][0], points[30][1]) * 100 / widthFace
#     return d

# מרחק בין הגבות
def betweenEyebrows():
    results.append(distance(points[21], points[22]))


# הנקודה הגבוהה ביותר בגבה
def maxPoint(start, end):
    min = points[start][0], points[start][1]
    for i in range(start + 1, end):
        if points[i][1] < min[1]:
            min = points[i][0], points[i][1]
    return min

# נקודת שבירה בגבה - תוצאה נהדרת
def breakingPointInHerBack():
    maxRight = maxPoint(22,26)
    maxLeft = maxPoint(17,21)
    lengthRight = eyebrowLength(22)
    lengthLeft = eyebrowLength(17)
    results.append(distance(maxRight, points[22]) * 100 / lengthRight)
    results.append(distance(maxLeft, points[21]) * 100 / lengthLeft)
    # print("A breaking point in the right eyebrow:", distance(maxRight, points[22]) * 100 / lengthRight)
    # print("A breaking point in the left eyebrow:", distance(maxLeft, points[21]) * 100 / lengthLeft)
    
# מרחק מקודקוד האף לתחילת הגבות
def vertexNosebeginingEyebrow():
    results.append(distance(points[30], points[22]) * 100 / results[1]) 
    results.append(distance(points[30], points[21]) * 100 / results[1]) 

# def a():
#     results.append(distance(points[31], points[17]) * 100 / results[1]) 
#     results.append(distance(points[33], points[26]) * 100 / results[1]) 

# matPoints1 = pointModels.point68Model("images/bibi1.jpg")
# matPoints2 = pointModels.point68Model("images/bibi2.jpg")
# print("one:", widthNose(matPoints1))
# print("tow:", widthNose(matPoints2))
# print("widthFace1:", widthAllFace(matPoints1))
# print("widthFace2:", widthAllFace(matPoints2))
# print(distance(matPoints1[0][0], matPoints1[0][1], matPoints1[27][0],matPoints1[27][1]))
# print(distance(matPoints1[16][0], matPoints1[16][1], matPoints1[27][0],matPoints1[27][1]))
# print(distance(matPoints2[0][0], matPoints2[0][1], matPoints2[27][0],matPoints2[27][1]))
# print(distance(matPoints2[16][0], matPoints2[16][1], matPoints2[27][0],matPoints2[27][1]))
# eye(matPoints1)
# eye(matPoints2)
# print("eyebrowLengthRight", eyebrowLength(matPoints1, 22))
# print("eyebrowLengthLeft", eyebrowLength(matPoints1, 17))
# print("eyebrowLengthRight", eyebrowLength(matPoints2, 22))
# print("eyebrowLengthLeft", eyebrowLength(matPoints2, 17))
# print("heghit nose:", noseLength(matPoints1))
# print("heghit nose:", noseLength(matPoints2))
# print("heihgt face:", heightAllFace(matPoints1))
# print("heihgt face:", heightAllFace(matPoints2))
# breakingPointInHerBack(matPoints1)
# breakingPointInHerBack(matPoints2)
# vec = distanceMiddle(matPoints1)
# arr = distanceMiddle(matPoints2)
# sum = 0
# for i in range(68):
#     print(round(abs(vec[i]-arr[i])))
#     print()
#     if abs(vec[i]-arr[i]) > 1:
#         sum+=abs(vec[i]-arr[i])
# print(sum/68)

