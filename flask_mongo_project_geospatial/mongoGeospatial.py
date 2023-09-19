from flask import Flask, render_template, request, redirect
import pymongo

app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["data"]
mycol = mydb["student"]
@app.route("/")
def intro():
    return render_template("home.html")

# @app.route("/student/<id>")
# def student(id):
#     if mycol.find_one({"_id": int(id)}):
#         return render_template("student.html", data=mycol.find_one({"_id": int(id)}))
#     else:
#         return render_template("noentry.html", id=id)

@app.route("/student")
def student():
    id = request.args.get("id")
    if mycol.find_one({"_id": int(id)}):
        return render_template("student.html", data=mycol.find_one({"_id": int(id)}))
    else:
        return render_template("noentry.html", id=id)

@app.route("/all")
def allStudents():
    if mycol.find():
        return render_template("all.html", data=mycol.find())
    else:
        return render_template("noentry.html")

@app.route("/del/<id>", methods = ["GET"])
def delStudent(id):
    mycol.delete_one({"_id": int(id)})
    return redirect("/all")

@app.route("/addStudent", methods=["GET"])
def addStudent():
    return render_template("StudentForm.html")

@app.route("/enter", methods=["POST"])
def addedDetails():
    val = request.form
    mycol.insert_one({"_id": int(val["id"]), "name": val["name"], "class": val["class"], "marks": {"maths": int(val["maths"]),
                                                                                             "physics": int(val["physics"]),
                                                                                              "chemistry": int(val["chemistry"])}})
    return redirect("/student?id="+val["id"])


if __name__ == "__main__":
    app.run(debug=True)
