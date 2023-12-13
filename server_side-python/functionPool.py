import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def widthAllFace(points):
    return distance(points[127][0], points[127][1], points[356][0], points[356][1])
    
def heightAllFace(points):
    return distance(points[10][0], points[10][1], points[152][0], points[152][1])

#נחמד ותו לא!!!    
def eyeball(points):
    sum = 0
    i = 221
    for i in range(5):
        sum += distance(points[i][0], points[i][1], points[i+1][0], points[i+1][1])
    print('top')
    print(round((sum*100)/widthAllFace(points)))
    sum = 0
    i = 228
    for i in range(5):
        sum += distance(points[i][0], points[i][1], points[i+1][0], points[i+1][1])
    sum += distance(points[i][0], points[i][1], points[193][0], points[193][1])
    print('bottom')
    print(round((sum*100)/widthAllFace(points)))
    

#טוב
def half(points):
    a = distance(points[55][0], points[55][1], points[8][0] , points[8][1])
    b = distance(points[8][0] , points[8][1],points[285][0], points[285][1])
    w = widthAllFace(points)
    print(round((a*100)/w), round((b*100)/w))
    # print((a*100)/w, (b*100)/w)
 
#אורך אוזן
#גרוע - לא אומר כלום
def ear(points):
    n = distance(points[132][0], points[132][1], points[127][0] , points[127][1])
    h = heightAllFace(points)
    print(round((n*100)/h))


# לא אומר כלום - מרחק בין הגבות
def eyebrow(points):
    widthEyebrow = distance(points[55][0], points[55][1], points[285][0], points[285][1])
    withFace = widthAllFace(points)
    print("widthEyebrow:{}".format((100*widthEyebrow)/withFace))
    return (100*widthEyebrow)/withFace

# def nose(points):

def topToNose(points):
    d = distance(points[0][0], points[0][1], points[2][0], points[2][1])
    h = heightAllFace(points)
    return round((d*100)/h)
