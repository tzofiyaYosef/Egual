import collectionFunctions

def compareImages(path_img1, path_img2):
    result1 = collectionFunctions.faceScorePointsArray(path_img1)
    result2 = collectionFunctions.faceScorePointsArray(path_img2)
    remainder = []
    for i in range(2, len(result1)):
        remainder.append(abs(result1[i] - result2[i]))
    # print(remainder)
    isSame = int(remainder[4]) if int(remainder[4]) == int(remainder[5]) else 0
    sum = count = 0
    for i in range(0, len(remainder)):
        sum += remainder[i]
        if remainder[i] < 1:
            count += 1
    if remainder[-1] > 25:
        sum -= remainder[-1]
    sum =  round(sum, 2)
    # sum = int(sum * 100)
    # sum = float(sum / 100)
    sum -= isSame*2
    # print(sum)
    # print(count)
    # return "nice!!"
    if count >= 3:
        return str(100)
    elif count == 2:
        return str(round(100 - sum / 9, 2))
    elif count == 1 and isSame != 0:
           return str(round(100 - sum * 0.2, 2))
    else:
        return str(0)
