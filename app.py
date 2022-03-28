
from flask import Flask,render_template,request,redirect,url_for
import attendance
import pandas as pd


app=Flask(__name__)

@app.route("/")
def hello():
   
    return render_template("index.html")
@app.route("/",methods=["POST"])
def submit():
    if request.method=="POST":
       attendance.attend()
       df=pd.read_csv("Attendance.csv")
       df=df[df.Name=="Pratiksha_Solankar"]
       
       return render_template("data.html",data=df.to_html())
     
        #print(marks_pred)
    return render_template("")
@app.route("/back")
def back():
    
    return redirect(url_for('hello'))
if __name__=="__main__":
       app.run(debug=True)
