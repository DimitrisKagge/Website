<<<<<<< HEAD
        
# BEGIN CODE HERE

import math
from operator import itemgetter
from urllib import request
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import TEXT
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


schema = {
    "ID": str,
    "name":str,
    "productionYear":int,
    "price":float,
    "color":int,
    "size":int
}
=======
# BEGIN CODE HERE
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import TEXT
>>>>>>> 94638b00be0349267de365b3048c41b457169f1e
# END CODE HERE

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/pspi"
CORS(app)
mongo = PyMongo(app)
mongo.db.products.create_index([("name", TEXT)])


<<<<<<< HEAD
# flask --app app --debug run

if __name__ == '__main__':
    app.run(debug=True)


@app.route("/search", methods=["GET"])
def search():
    # BEGIN CODE HERE
    #Getting the name from the search bar
    name = request.args.get("name")
    list1 = []
    #making a list with the products with the name of the input of search bar
    for x in mongo.db.products.find({"$text": {"$search": f"\"{name}\""}}):
        list1.append(x)
        #sorting the list by price
    newlist = sorted(list1, key=itemgetter('price'), reverse=True)
    final_list = []
    for x in newlist:
        final_list.append(str(x))
        print(x)
    return jsonify(final_list)
=======
@app.route("/search", methods=["GET"])
def search():
    # BEGIN CODE HERE
    return ""
>>>>>>> 94638b00be0349267de365b3048c41b457169f1e
    # END CODE HERE


@app.route("/add-product", methods=["POST"])
def add_product():
    # BEGIN CODE HERE
<<<<<<< HEAD

    new_product = request.json()
    exists = mongo.db.products.find_one({"name": new_product["name"]})
    if exists is None:
        mongo.db.products.insert_one(new_product)
        return jsonify({" ": "added"})
    else:
        mongo.db.products.update_one({"name": new_product["name"]}, {"$set": {"ID": new_product["ID"], "productionYear": new_product["productionYear"], "price": new_product["price"], "size": new_product["size"], "color": new_product["color"]}})
        return jsonify({" ": "updated"})

=======
    return ""
>>>>>>> 94638b00be0349267de365b3048c41b457169f1e
    # END CODE HERE


@app.route("/content-based-filtering", methods=["POST"])
def content_based_filtering():
    # BEGIN CODE HERE
<<<<<<< HEAD
    new_product = request.json
    thistuple = (new_product["productionYear"], new_product["price"], new_product["color"], new_product["size"])

    list1 = []
    thisdistance = math.sqrt(thistuple[0]*thistuple[0] + thistuple[1]*thistuple[1] + thistuple[2]*thistuple[2] + thistuple[3]*thistuple[3])

    for x in mongo.db.products.find():
        tuple2 = (x["productionYear"], x["price"], x["color"], x["size"])
        multi2 = sum(p*q for p, q in zip(thistuple, tuple2))
        distance2 = math.sqrt(tuple2[0]*tuple2[0] + tuple2[1]*tuple2[1] + tuple2[2]*tuple2[2] + tuple2[3]*tuple2[3])
        if multi2/(thisdistance*distance2) >= 0.7:
            list1.append(x["name"])

    return list1
=======
    return ""
>>>>>>> 94638b00be0349267de365b3048c41b457169f1e
    # END CODE HERE


@app.route("/crawler", methods=["GET"])
def crawler():
    # BEGIN CODE HERE
<<<<<<< HEAD
    semester = request.args.get("semester1")
    print(semester)
    try:
        url = "https://qa.auth.gr/el/x/studyguide/600000438/current"
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        #taking the table with the specific semester
        str2 = "/html/body/div[2]/div[1]/div/div/div/div/div[2]/table["+semester+"]/tbody"
        print(str2)
        html = str((driver.find_element(By.XPATH, str2)).text)
        #spliting the table into words
        html1 = html.split()
        #making the wanted string and removing all the unwanted words
        string1 = ""
        subjects = []
        for x in html1:
            if x != "Υ" and x != "ΥΚΕ" and x != "Ε" and x != "ΓΕ" and not(str.isdigit(x)) and x.count("-") != 2 and not("," in x):
                if string1 == "":
                    string1 = x
                else:
                    string1 = string1 + " " + x
            else:
                if string1 != "":
                    subjects.append(string1)
                    string1 = ""
        print(subjects)

    except Exception as e:
        print("bad request")

    return subjects



#END CODE HERE

    
=======
    return ""
    # END CODE HERE
>>>>>>> 94638b00be0349267de365b3048c41b457169f1e
