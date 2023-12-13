import pymongo
import json
import base64
from PIL import Image


def openDB(mycollection):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["egual"]
    return mydb[mycollection]


# הוספת משתמש חדש
def addNewUser(gson_string):
    data = json.loads(gson_string)
    users = openDB("users")
    query = {"gmail": data["gmail"]}
    existing_user = users.find_one(query)
    if existing_user is None:
        users.insert_one(data)
        existing_user = {
            "userName": data["userName"],
            "firstName": data["firstName"],
            "lastName": data["lastName"],
            "password": data["password"],
            "phone": data["phone"],
            "gmail": data["gmail"],
        }
        return existing_user
    return "failed"


# החזרת משתמש קיים
def ReturningExistUser(gson_string):
    data = json.loads(gson_string)
    users = openDB("users")
    allUsers = users.find()
    for userExist in allUsers:
        if (
            userExist["password"] == data["password"]
            and userExist["userName"] == data["userName"]
        ):
            data = {
                "userName": userExist["userName"],
                "firstName": userExist["firstName"],
                "lastName": userExist["lastName"],
                "password": userExist["password"],
                "phone": userExist["phone"],
                "gmail": userExist["gmail"],
            }
            return data
    return "not exist"


# החזרת משתמש
def ReturningtUser(id):
    data = json.loads(id)
    users = openDB("users")
    allUsers = users.find()
    for userExist in allUsers:
        if userExist["gmail"] == data:
            data = {
                "userName": userExist["userName"],
                "firstName": userExist["firstName"],
                "lastName": userExist["lastName"],
                "password": userExist["password"],
                "phone": userExist["phone"],
                "gmail": userExist["gmail"],
            }
            return data


# עדכון משתמש רשום
def updateUser(gson_string, id):
    data = json.loads(gson_string)
    id_user = json.loads(id)
    user = userSearch(id_user)
    # my_id = json.loads(user)
    if user != "null":
        openDB("users").update_one(
            {"_id": user["_id"]},
            {
                "$set": {
                    "userName": data["userName"],
                    "firstName": data["firstName"],
                    "lastName": data["lastName"],
                    "password": data["password"],
                    "phone": data["phone"],
                    "gmail": data["gmail"],
                }
            },
        )
    return "succes"


# חיפוש משתמש לפי המייל
def userSearch(gmail):
    users = openDB("users")
    allUsers = users.find()
    for user in allUsers:
        if user["gmail"] == gmail:
            return user
    return "null"


# צפייה בארכיון התמונות
def viewingArchive(gmail):
    user = userSearch(gmail)
    if user != "null":
        arr = []
        comparePhotos = openDB("Compare photos")
        allComparePhotos = comparePhotos.find()
        for comparePhoto in allComparePhotos:
            if comparePhoto["idUser"] == gmail:
                # Load images from file
                path1 = Image.open(comparePhoto["path1"])
                path2 = Image.open(comparePhoto["path2"])
                
                # Convert images to base64 strings
                with open(comparePhoto["path1"], "rb") as image_file:
                    path1_encoded = base64.b64encode(image_file.read()).decode('utf-8')
                with open(comparePhoto["path2"], "rb") as image_file:
                    path2_encoded = base64.b64encode(image_file.read()).decode('utf-8')
                
                arr.append(
                    {
                        "idUser": comparePhoto["idUser"],
                        "path1": path1_encoded,
                        "path2": path2_encoded,
                        "comparisonResult": comparePhoto["comparisonResult"],
                        "comparisonDate": comparePhoto["comparisonDate"],
                    }
                )
        return arr


# בדיקה האם האורח הספציפי בזבז את מכסת ההשוואות שלו
# def maximumAmount(ipComputer):
#     data = json.loads(ipComputer)
#     guests = openDB("guests")
#     allGuests = guests.find()
#     for guest in allGuests:
#         if guest["ipComputer"] == data["ipComputer"] and guest["count"] > 3:
#             return False
#         elif guest["count"] < 3:
#             return True
#     newGuest = {"ipComputer": ipComputer, "count": 1}
#     guests._insert_one(newGuest)
#     return True
