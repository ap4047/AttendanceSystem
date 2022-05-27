from asyncio.windows_events import NULL

from flask import Flask,render_template,request,redirect,url_for
import attendance
import pandas as pd
import urllib.request

import os
from werkzeug.utils import secure_filename
from datetime import datetime
# from flask_pymongo import PyMongo
app=Flask(__name__)
import pymongo
from pymongo import MongoClient
cluster=MongoClient("mongodb+srv://ap4047:4047@cluster0.yhzcb.mongodb.net/attendance_system?retryWrites=true&w=majority")
db=cluster["attendance_system"]
collection=db["studentdata"]
post={"name":"tin","score":5}
# mongodb+srv://patilashish2205:<password>@cluster0.kxiiu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority

# app.config['MONGO_URI']="mongodb+srv://patilashish2205:patil2205@cluster0.kxiiu.mongodb.net/FACE_RECOGNITION_ATTENDANCE_SYSTEM?retryWrites=true&w=majority"
# # from user import routes#
# mongo=PyMongo(app)

@app.route("/")
def hello(): return render_template("home.html")
# @app.route("/dashboard",methods=["GET"])
# def dashboard():
#     return render_template("dashboard.html")
@app.route("/login",methods=["GET"])
def login():
    return render_template("login.html")
@app.route("/login",methods=["POST"])
def student_login():
    if(request.method=="POST"):
        print(request.form.get("email"))
        results=collection.find({"email":request.form.get("email"),"password":request.form.get("password")})
        print(results)


        for result in results:
            print(result)
            print(result["email"])
            if(result["email"]==request.form.get("email") and result["password"]==request.form.get("password")):
                return render_template("dashboard.html")
    
            
            

        print("user not found")
    return render_template("dashboard.html")
@app.route("/register",methods=["GET"])
def register():
   
    return render_template("signup.html")
@app.route("/register",methods=["POST"])
def student_profile():
    if "photo" in request.files:
        print("inside request files",request.form.get('studentname'))
        profile_image=request.files["photo"]
        present=collection.find({"email":request.form.get("email")})
        for result in present:
            if(result["email"]==request.form.get("email")):
                collection.update_one({"_id":result["_id"]},{"$set":{'studentname':request.form.get('studentname'),'password':request.form.get('password'),'reg_id':request.form.get("reg_id"),"photo":request.form.get("photo")}})
                return "registration successfull"

        collection.insert_one({'studentname':request.form.get('studentname'),
       'email':request.form.get('email'),'password':request.form.get('password'),'reg_id':request.form.get("reg_id"),"photo":request.form.get("photo")})
       
        # UPLOAD_FOLDER = 'C:/Users/Admin/facerecog/images/'
        # app.secret_key = "secret key"
        # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        # app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
        # ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
        # def allowed_file(filename):
        #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
       
        # photo=request.files("photo")
        # if photo.filename=="":
        #     print("no images selected for uploading")
        #     return "no image selected"
        # if photo and allowed_file(photo.filename):
        #     filename=secure_filename(photo.filename)
        #     photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     print('Image successfully uploaded and displayed below')
        #     return render_template('login.html')
        # else:
        #     return "allowed image formats are "
    return "insertion successfull"
@app.route("/take_attendance",methods=["POST"])
def take_attendance():
    subject=request.form.get("subject")
    print("subject")
    attendance.attend(subject)
    df=pd.read_csv("Attendance.csv")
    time_now=datetime.now()
    dStr=time_now.strftime('%d/%m/%Y')
    report_df=df.loc[df['Date'] == dStr]
    report_df.sort_values(by="Name")
    result=report_df.to_html()
    return render_template("data.html",data=result)

@app.route("/attendance",methods=["GET"])
def attendance_():
    return render_template("attendance.html")

@app.route("/attendance",methods=["POST"])
def submit():
    if request.method=="POST":
       subject=request.form.get("subject")
       name=request.form["name"]
       name=name.upper()
       df=pd.read_csv("Attendance.csv")
       report_df=df.loc[(df['Name'] == name) & (df['Subject']==subject)]
       report_df.sort_values(by="Name")
       result = report_df.to_html()
       print(result)
       return render_template("data.html",data=result)
     
       #print(marks_pred)
    return render_template("")
@app.route("/todaysAttendance",methods=["POST"])
def todaysattendance():
    if(request.method=="POST"):
        subject=request.form.get("subject")
        date=request.form["date"]
        print(type(date))
        print(date)
        dt = datetime.strptime(date, '%Y-%m-%d')
        dt=dt.strftime('%d/%m/%Y')
        df=pd.read_csv("Attendance.csv")
        report_df=df.loc[(df['Date'] == dt) & (df['Subject']==subject)]
        report_df.sort_values(by="Name")
        result = report_df.to_html()
        print(result)
        return render_template("data.html",data=result)
       
        
    return "error in todyas attenadce"
    
        

@app.route("/dashboard",methods=['GET'])
def dashboard():
    return render_template("dashboard.html ")
@app.route("/back")
def back():
    return redirect(url_for('hello'))
if __name__=="__main__":
       app.run(debug=True)
