from flask import Flask,render_template,request,redirect
from fun import*
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        registration(request.form["name"],request.form["age"],request.form["address"],request.form["course"])
    data=read_json()
    return render_template("joy.html",student=data["student"])

@app.route("/delete/<id>")
def delete(id):
    deletestud(id)
    return redirect("/")

@app.route("/update/<id>", methods=["POST"])
def update(id):
    updatestud(id,request.form["name"],request.form["address"],request.form["age"],request.form["course"])
    return redirect("/")


if  __name__=="__main__":
    app.run(debug=True , host="0.0.0.0")


