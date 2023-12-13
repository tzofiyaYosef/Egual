from flask import Flask, request, jsonify
from flask_cors import cross_origin
from datetime import date
import socket
from flask_cors import CORS
from PIL import Image
import main
import myDB
import os
import cv2
import glob
import numpy as np
import uuid
import shutil

app = Flask(__name__)
CORS(app, resources={r"/compare": {"origins": "http://localhost:3000"}})


# הפעלת פונקציית ההשוואה על התמונות שהתקבלו
@app.route("/compare", methods=["POST"])
@cross_origin()
def compare():
    try:
        image1 = request.files["image1"]
        image2 = request.files["image2"]
        filename1 = temp(image1)
        filename2 = temp(image2)
        path_img1 = Image.open(os.path.join("images", filename1))
        path_img2 = Image.open(os.path.join("images", filename2))
        id = request.form["id"]
        if id == None:
            ip = socket.gethostbyname(socket.gethostname())
            guests = myDB.openDB("guests")
            ip = {"ip": ip}
            existing_guest = guests.find_one(ip)
            if existing_guest:
                if existing_guest["count"] < 3:
                    guests.update_one(
                        {"_id": existing_guest["_id"]},
                        {"$set": {"count": existing_guest["count"] + 1}},
                    )
                else:
                    return "fails"
            else:
                guests.insert_one({"ip": ip, "count": 1})
            result = main.compareImages(path_img1, path_img2)
            return result + "%"
        else:
            result = main.compareImages(path_img1, path_img2)
            # result = round(result,2)
            comparePhotos = myDB.openDB("Compare photos")
            comparePhotos.insert_one(
                {
                    "idUser": id,
                    "path1": os.path.join("images", filename1),
                    "path2": os.path.join("images", filename2),
                    "comparisonResult": result + "%",
                    "comparisonDate": str(date.today()),
                }
            )
            return result + "%"
    except Exception as e:
        return jsonify({"error": str(e)})


def temp(image1):
    pattern = "images/*.jpg"
    fn = str(uuid.uuid4()) + ".jpg"
    image1.save(fn)
    image1 = cv2.imread(fn, cv2.IMREAD_GRAYSCALE)
    image1 = cv2.resize(image1, (256, 256))

    # Loading the images into the array
    image_files = glob.glob(pattern)
    images = []
    image_names = []  # List to store the image names
    for file_name in image_files:
        image2 = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
        image2 = cv2.resize(image2, (256, 256))
        images.append(image2)
        image_names.append(os.path.basename(file_name))  # Get the base name of the file

    flag1 = False
    for i, image2 in enumerate(images):
        if not flag1:
            flag1 = True if isSame(image1, image2) == 0 else False
        if flag1:
            os.remove(fn)
            return image_names[i]

    # Save the image in the "images" folder
    src_path = fn
    dst_path = os.path.join("images", fn)
    
    shutil.copy(src_path, dst_path)
    # cv2.imwrite(filename, image1)
    os.remove(fn)
    return fn


def isSame(img1, img2):
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff**2)
    h, w = img1.shape
    mes = err / (h * w)
    return (mes)

@app.route("/addNewUser", methods=["POST"])
@cross_origin()
def addNewUser():
    user = request.form["newUser"]
    return myDB.addNewUser(user)


@app.route("/userExist", methods=["POST"])
@cross_origin()
def userExist():
    user = request.form["userExist"]
    return myDB.ReturningExistUser(user)


@app.route("/updateUser", methods=["POST"])
@cross_origin()
def updateUser():
    user = request.form["userExist"]
    idUser = request.form["id"]
    return myDB.updateUser(user, idUser)


@app.route("/ReturningtUser", methods=["POST"])
@cross_origin()
def ReturningtUser():
    idUser = request.form["id"]
    return myDB.ReturningtUser(idUser)


@app.route("/viewingArchive", methods=["POST"])
@cross_origin()
def viewingArchive():
    idUser = request.form["id"]
    return myDB.viewingArchive(idUser)


# # Connecting to MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client['mydatabase']

# # Defining the user architecture5
# users = db['users']

# @app.route('/api/create-user', methods=['POST'])
# def create_user():
#   # Decomposing the body of the request from JSON into a Python object
#   data = request.get_json()

#   # Checking if a user with the same email address already exists
#   if users.find_one({'gmail': data['gmail']}) is not None:
#     return jsonify({'success': False, 'message': 'A user with this email address already exists'})

#   # Inserting the new user into Mauchert
#   result = users.insert_one(data)

#   # Return a success message
#   return jsonify({'success': True, 'message': 'The user was successfully created'})

if __name__ == "__main__":
    app.run(debug=True)
