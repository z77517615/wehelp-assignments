from flask import Flask
from flask import session
from flask import request
from flask import redirect
from flask import render_template
import mysql.connector 
from mysql.connector import pooling

poolname='mysqlpool'
poolsize=3

dbconfig={'host':'localhost',
        'user':'root',
        'password':'password',
        'database':'website'}

connectionpool=mysql.connector.pooling.MySQLConnectionPool(
                                            pool_name=poolname,
                                            pool_reset_session='True',
                                            pool_size=poolsize,
                                            **dbconfig)
                                            
connection=connectionpool.get_connection()
print(connectionpool.pool_name)
print(connectionpool.pool_size)
mydb = mysql.connector.connect(port='3306',
                                **dbconfig)

mycursor = mydb.cursor()

app=Flask( __name__,static_folder="templates", static_url_path="/" )
app.secret_key="123123123"  




@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/member")
def member():
    if "account" in session:
        name=session["name"]
        return render_template("member.html",namemassage=name)
    else:
        return redirect("/")
    
@app.route("/signup",methods=["POST"])
def signup():
    name=request.form["name"]
    account=request.form["account"]
    password=request.form["password"]
    while True:
        if name=="":
            return redirect("/error?massage=姓名不能為空")
        if account=="":
            return redirect("/error?massage=帳號不能為空")
        if password=="":
            return redirect("/error?massage=密碼不能為空")
           
        sql = "SELECT username FROM member WHERE username = '"+ account + "'"
        mycursor.execute(sql)
        records=mycursor.fetchall()
        if (len(records)) ==0:
            sql="INSERT INTO member (name,username,password) VALUES (%s, %s ,%s )"
            val=(name ,account ,password)
            mycursor.execute(sql,val)
            mydb.commit()
            return redirect("/")       
        else:
            return redirect("/error?massage=帳號已經被註冊")

@app.route("/error")
def error():
    msg=request.args.get("massage","")
    return render_template("error.html",errormassage=msg)

@app.route("/signin",methods=["POST"])
def signin():
    account=request.form["account"]
    password=request.form["password"]
    sql="SELECT name, username, password  FROM member WHERE username ='"+ account + "' AND password ='"+ password + "'"
    mycursor.execute(sql)
    records=mycursor.fetchall()
    if len(records)==1: 
        name=records[0][0]
        session["name"]=name
        session["account"]=account
        return redirect("/member")
    
    elif account==password=="":
        return redirect("/error?massage=請輸入帳號密碼")
    
    else:
        return redirect("/error?massage=帳號，或密碼輸入錯誤")

@app.route("/signout")
def signout():
    session.pop("account", None)
    return redirect("/")


#查詢
@app.route("/api/members")
def api_members():
    if "account" in session:
        username=request.args.get("username")
        sql="SELECT id,name,username FROM member WHERE username = %s"
        val=(username,)
        mycursor.execute(sql,val)
        record=mycursor.fetchone()
        if record:
            data = { "data":{
                "id" : record[0],
                "name" : record[1],
                "username":record[2]
            }}
            return (data)
        else:
            return { "data": None
            }



app.run(port=3000,debug=True)    

