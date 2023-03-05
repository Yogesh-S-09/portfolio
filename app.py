from flask import Flask,render_template , jsonify , request
from script.dic import mean
from script.qr import generate_qrcode

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dict/")
def dict():
    return render_template("dict.html")

@app.route("/qr/")
def qr():
    return render_template("qr.html")

@app.route("/dict/meaning", methods=['post'])
def meaning():
    data=request.form
    Word=mean(data['word'])
    return render_template("dictword.html",word=data['word'],mean=Word)

@app.route("/qr/img", methods=['post'])
def qrimg():
    data=request.form
    Word=generate_qrcode(data['word'])
    return render_template("qrimg.html",mean=Word)

if(__name__ == "__main__"):
    app.run(host="0.0.0.0" ,debug=True)