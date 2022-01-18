from asyncio.windows_events import NULL
from flask import Flask
from flask import session
from flask import request
from flask import redirect
from flask import render_template

app=Flask( __name__,static_folder="templates", static_url_path="/" )
app.secret_key="123123123"  



@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/member")
def member():
    if "account" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    msg=request.args.get("massage","")
    return render_template("error.html",errormassage=msg)

@app.route("/signin",methods=["POST"])
def signin():
    account=request.form["account"]
    password=request.form["password"]
    if account==password=="test":
        session["account"]=account;  
        return  redirect("/member")  

    elif account==password=="":
         return redirect("/error?massage=請輸入帳號密碼")

    else:
        return redirect("/error?massage=帳號，或密碼輸入錯誤")

@app.route("/signout")
def signout():
    session.pop("account", None)
    return redirect("/")

app.run(port=3000)    

